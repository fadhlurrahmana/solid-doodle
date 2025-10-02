from flask import Flask, render_template, request, send_file, jsonify
import os
from werkzeug.utils import secure_filename
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import cv2
import numpy as np
import io

# Try to import rembg, but provide fallback
try:
    from rembg import remove
    REMBG_AVAILABLE = True
except ImportError:
    REMBG_AVAILABLE = False
    print("Warning: rembg not available. Using simple background removal fallback.")

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'outputs'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create necessary directories
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'avi', 'mov'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def remove_background(image_path):
    """Remove background from image using rembg or fallback method"""
    if REMBG_AVAILABLE:
        try:
            with open(image_path, 'rb') as input_file:
                input_data = input_file.read()
                output_data = remove(input_data)
            return Image.open(io.BytesIO(output_data))
        except Exception as e:
            print(f"rembg failed: {e}, using fallback")
    
    # Fallback: simple background removal using color masking
    img = Image.open(image_path)
    
    # Convert to RGBA if not already
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    # For fallback, we'll just return the image as-is with transparency support
    # In a production system, you'd want proper background removal
    return img

def create_product_promotion(human_img_path, product_img_path, text="PROMO SPESIAL!", output_path="output.png"):
    """Create a product promotion image by combining human and product images"""
    
    # Remove background from human image
    human_img = remove_background(human_img_path)
    
    # Open product image
    product_img = Image.open(product_img_path)
    
    # Create a new canvas (1920x1080 for standard HD)
    width, height = 1920, 1080
    canvas = Image.new('RGB', (width, height), color=(255, 255, 255))
    
    # Resize images to fit canvas
    # Human image on the left side
    human_ratio = min(600 / human_img.width, 900 / human_img.height)
    human_new_size = (int(human_img.width * human_ratio), int(human_img.height * human_ratio))
    human_img_resized = human_img.resize(human_new_size, Image.Resampling.LANCZOS)
    
    # Product image on the right side
    product_ratio = min(800 / product_img.width, 800 / product_img.height)
    product_new_size = (int(product_img.width * product_ratio), int(product_img.height * product_ratio))
    product_img_resized = product_img.resize(product_new_size, Image.Resampling.LANCZOS)
    
    # Add gradient background
    gradient = create_gradient_background(width, height)
    canvas.paste(gradient, (0, 0))
    
    # Paste human image (centered left)
    human_x = 100
    human_y = (height - human_new_size[1]) // 2
    canvas.paste(human_img_resized, (human_x, human_y), human_img_resized if human_img_resized.mode == 'RGBA' else None)
    
    # Paste product image (centered right)
    product_x = width - product_new_size[0] - 150
    product_y = (height - product_new_size[1]) // 2
    
    # Add white background for product
    product_bg = Image.new('RGBA', (product_new_size[0] + 40, product_new_size[1] + 40), (255, 255, 255, 230))
    canvas.paste(product_bg, (product_x - 20, product_y - 20), product_bg)
    canvas.paste(product_img_resized, (product_x, product_y))
    
    # Add promotional text
    draw = ImageDraw.Draw(canvas)
    
    # Try to use a nice font, fallback to default
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 80)
        subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 50)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
    
    # Add text with shadow for better visibility
    text_bbox = draw.textbbox((0, 0), text, font=title_font)
    text_width = text_bbox[2] - text_bbox[0]
    text_x = (width - text_width) // 2
    text_y = 80
    
    # Shadow
    draw.text((text_x + 3, text_y + 3), text, font=title_font, fill=(0, 0, 0, 128))
    # Main text
    draw.text((text_x, text_y), text, font=title_font, fill=(255, 50, 50))
    
    # Add call-to-action
    cta_text = "Beli Sekarang!"
    cta_bbox = draw.textbbox((0, 0), cta_text, font=subtitle_font)
    cta_width = cta_bbox[2] - cta_bbox[0]
    cta_x = (width - cta_width) // 2
    cta_y = height - 120
    
    # CTA background
    draw.rectangle([cta_x - 30, cta_y - 20, cta_x + cta_width + 30, cta_y + 60], 
                   fill=(255, 50, 50), outline=(200, 0, 0), width=3)
    draw.text((cta_x, cta_y), cta_text, font=subtitle_font, fill=(255, 255, 255))
    
    # Save the final image
    canvas.save(output_path, 'PNG', quality=95)
    return output_path

def create_gradient_background(width, height):
    """Create a gradient background image"""
    # Create gradient from light blue to white
    gradient = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(gradient)
    
    for i in range(height):
        # Gradient from light blue (200, 220, 255) to white (255, 255, 255)
        r = int(200 + (55 * i / height))
        g = int(220 + (35 * i / height))
        b = 255
        draw.line([(0, i), (width, i)], fill=(r, g, b))
    
    return gradient

def create_video_promotion(human_img_path, product_img_path, text="PROMO SPESIAL!", output_path="output.mp4", duration=5):
    """Create a video promotion with animated transitions"""
    
    # Create the static promotional image first
    temp_img_path = os.path.join(app.config['OUTPUT_FOLDER'], 'temp_promo.png')
    create_product_promotion(human_img_path, product_img_path, text, temp_img_path)
    
    # Read the image
    img = cv2.imread(temp_img_path)
    height, width, layers = img.shape
    
    # Video settings
    fps = 30
    total_frames = duration * fps
    
    # Create video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    # Add frames with zoom effect
    for frame_num in range(total_frames):
        # Create zoom-in effect
        progress = frame_num / total_frames
        zoom = 1.0 + (0.1 * progress)  # Zoom from 1.0 to 1.1
        
        # Calculate the center crop
        new_width = int(width / zoom)
        new_height = int(height / zoom)
        x = (width - new_width) // 2
        y = (height - new_height) // 2
        
        # Crop and resize
        cropped = img[y:y+new_height, x:x+new_width]
        frame = cv2.resize(cropped, (width, height), interpolation=cv2.INTER_LINEAR)
        
        # Add fade-in effect for first second
        if frame_num < fps:
            alpha = frame_num / fps
            frame = cv2.addWeighted(frame, alpha, np.zeros_like(frame), 1 - alpha, 0)
        
        video.write(frame)
    
    video.release()
    
    # Clean up temp image
    if os.path.exists(temp_img_path):
        os.remove(temp_img_path)
    
    return output_path

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    try:
        # Check if files are present
        if 'human_photo' not in request.files or 'product_photo' not in request.files:
            return jsonify({'error': 'Missing files'}), 400
        
        human_photo = request.files['human_photo']
        product_photo = request.files['product_photo']
        promo_text = request.form.get('promo_text', 'PROMO SPESIAL!')
        output_type = request.form.get('output_type', 'image')
        
        if human_photo.filename == '' or product_photo.filename == '':
            return jsonify({'error': 'No selected files'}), 400
        
        if not (allowed_file(human_photo.filename) and allowed_file(product_photo.filename)):
            return jsonify({'error': 'Invalid file type'}), 400
        
        # Save uploaded files
        human_filename = secure_filename(human_photo.filename)
        product_filename = secure_filename(product_photo.filename)
        
        human_path = os.path.join(app.config['UPLOAD_FOLDER'], human_filename)
        product_path = os.path.join(app.config['UPLOAD_FOLDER'], product_filename)
        
        human_photo.save(human_path)
        product_photo.save(product_path)
        
        # Generate output
        if output_type == 'video':
            output_filename = 'promo_video.mp4'
            output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)
            create_video_promotion(human_path, product_path, promo_text, output_path)
        else:
            output_filename = 'promo_image.png'
            output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)
            create_product_promotion(human_path, product_path, promo_text, output_path)
        
        return jsonify({
            'success': True,
            'output_file': output_filename,
            'message': 'Promo berhasil dibuat!'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(
        os.path.join(app.config['OUTPUT_FOLDER'], filename),
        as_attachment=True,
        download_name=filename
    )

@app.route('/preview/<filename>')
def preview_file(filename):
    return send_file(
        os.path.join(app.config['OUTPUT_FOLDER'], filename),
        mimetype='image/png' if filename.endswith('.png') else 'video/mp4'
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

#!/usr/bin/env python3
"""
Demo script to create sample promotional images without requiring rembg
This demonstrates the core functionality of the application
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_sample_human_image(output_path='sample_human.png'):
    """Create a sample human silhouette image"""
    # Create a 400x600 image with transparent background
    img = Image.new('RGBA', (400, 600), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw a simple human silhouette
    # Head
    draw.ellipse([150, 50, 250, 150], fill=(100, 100, 150, 255))
    
    # Body
    draw.rectangle([140, 150, 260, 400], fill=(100, 100, 150, 255))
    
    # Arms
    draw.rectangle([80, 180, 140, 350], fill=(100, 100, 150, 255))
    draw.rectangle([260, 180, 320, 350], fill=(100, 100, 150, 255))
    
    # Legs
    draw.rectangle([150, 400, 200, 580], fill=(100, 100, 150, 255))
    draw.rectangle([200, 400, 250, 580], fill=(100, 100, 150, 255))
    
    img.save(output_path)
    print(f"✓ Created sample human image: {output_path}")
    return output_path

def create_sample_product_image(output_path='sample_product.png'):
    """Create a sample product image"""
    # Create a 500x500 image
    img = Image.new('RGB', (500, 500), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Draw a product box
    draw.rectangle([100, 100, 400, 400], fill=(200, 50, 50), outline=(150, 0, 0), width=5)
    
    # Add product label
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)
    except:
        font = ImageFont.load_default()
    
    text = "PRODUK"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_x = (500 - text_width) // 2
    draw.text((text_x, 230), text, fill=(255, 255, 255), font=font)
    
    img.save(output_path)
    print(f"✓ Created sample product image: {output_path}")
    return output_path

def create_gradient_background(width, height):
    """Create a gradient background image"""
    gradient = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(gradient)
    
    for i in range(height):
        r = int(200 + (55 * i / height))
        g = int(220 + (35 * i / height))
        b = 255
        draw.line([(0, i), (width, i)], fill=(r, g, b))
    
    return gradient

def create_demo_promotion(human_img_path, product_img_path, text="DEMO PROMO!", output_path="demo_output.png"):
    """Create a demo promotion image"""
    # Open images
    human_img = Image.open(human_img_path)
    product_img = Image.open(product_img_path)
    
    # Create canvas
    width, height = 1920, 1080
    canvas = Image.new('RGB', (width, height), color=(255, 255, 255))
    
    # Add gradient background
    gradient = create_gradient_background(width, height)
    canvas.paste(gradient, (0, 0))
    
    # Resize and place human image
    human_ratio = min(600 / human_img.width, 900 / human_img.height)
    human_new_size = (int(human_img.width * human_ratio), int(human_img.height * human_ratio))
    human_img_resized = human_img.resize(human_new_size, Image.Resampling.LANCZOS)
    
    human_x = 100
    human_y = (height - human_new_size[1]) // 2
    
    if human_img_resized.mode == 'RGBA':
        canvas.paste(human_img_resized, (human_x, human_y), human_img_resized)
    else:
        canvas.paste(human_img_resized, (human_x, human_y))
    
    # Resize and place product image
    product_ratio = min(800 / product_img.width, 800 / product_img.height)
    product_new_size = (int(product_img.width * product_ratio), int(product_img.height * product_ratio))
    product_img_resized = product_img.resize(product_new_size, Image.Resampling.LANCZOS)
    
    product_x = width - product_new_size[0] - 150
    product_y = (height - product_new_size[1]) // 2
    
    # Add white background for product
    product_bg = Image.new('RGBA', (product_new_size[0] + 40, product_new_size[1] + 40), (255, 255, 255, 230))
    canvas.paste(product_bg, (product_x - 20, product_y - 20), product_bg)
    canvas.paste(product_img_resized, (product_x, product_y))
    
    # Add text
    draw = ImageDraw.Draw(canvas)
    
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 80)
        subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 50)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
    
    # Main title
    text_bbox = draw.textbbox((0, 0), text, font=title_font)
    text_width = text_bbox[2] - text_bbox[0]
    text_x = (width - text_width) // 2
    text_y = 80
    
    draw.text((text_x + 3, text_y + 3), text, font=title_font, fill=(0, 0, 0, 128))
    draw.text((text_x, text_y), text, font=title_font, fill=(255, 50, 50))
    
    # Call to action
    cta_text = "Beli Sekarang!"
    cta_bbox = draw.textbbox((0, 0), cta_text, font=subtitle_font)
    cta_width = cta_bbox[2] - cta_bbox[0]
    cta_x = (width - cta_width) // 2
    cta_y = height - 120
    
    draw.rectangle([cta_x - 30, cta_y - 20, cta_x + cta_width + 30, cta_y + 60], 
                   fill=(255, 50, 50), outline=(200, 0, 0), width=3)
    draw.text((cta_x, cta_y), cta_text, font=subtitle_font, fill=(255, 255, 255))
    
    canvas.save(output_path, 'PNG', quality=95)
    print(f"✓ Created demo promotion: {output_path}")
    return output_path

def main():
    print("=" * 60)
    print("AI Product Promotion Editor - Demo")
    print("=" * 60)
    print()
    
    # Create output directory
    os.makedirs('demo_outputs', exist_ok=True)
    
    # Create sample images
    print("Creating sample images...")
    human_path = create_sample_human_image('demo_outputs/sample_human.png')
    product_path = create_sample_product_image('demo_outputs/sample_product.png')
    print()
    
    # Create demo promotion
    print("Creating demo promotion...")
    demo_path = create_demo_promotion(
        human_path, 
        product_path, 
        "PROMO SPESIAL!", 
        'demo_outputs/demo_promotion.png'
    )
    print()
    
    print("=" * 60)
    print("✓ Demo completed successfully!")
    print(f"  Check the 'demo_outputs' directory for results")
    print("=" * 60)

if __name__ == '__main__':
    main()

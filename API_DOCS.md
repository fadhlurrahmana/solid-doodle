# API Documentation

## Endpoints

### 1. GET /

**Description**: Render the main application page

**Response**: HTML page with upload interface

**Example**:
```bash
curl http://localhost:5000/
```

---

### 2. POST /upload

**Description**: Upload photos and generate promotional content

**Content-Type**: `multipart/form-data`

**Parameters**:
| Parameter      | Type   | Required | Description                           |
|----------------|--------|----------|---------------------------------------|
| human_photo    | file   | Yes      | Image file of human/model            |
| product_photo  | file   | Yes      | Image file of product                |
| promo_text     | string | No       | Promotional text (default: "PROMO SPESIAL!") |
| output_type    | string | No       | "image" or "video" (default: "image") |

**Accepted File Types**: 
- Images: png, jpg, jpeg, gif
- Videos: mp4, avi, mov (for future use)

**Max File Size**: 16MB per file

**Success Response**:
```json
{
  "success": true,
  "output_file": "promo_image.png",
  "message": "Promo berhasil dibuat!"
}
```

**Error Response**:
```json
{
  "error": "Error message description"
}
```

**Status Codes**:
- `200 OK`: Success
- `400 Bad Request`: Missing files, invalid file type, or validation error
- `500 Internal Server Error`: Processing error

**Example**:
```bash
curl -X POST http://localhost:5000/upload \
  -F "human_photo=@/path/to/human.jpg" \
  -F "product_photo=@/path/to/product.jpg" \
  -F "promo_text=DISKON 50%!" \
  -F "output_type=image"
```

---

### 3. GET /download/<filename>

**Description**: Download generated promotional content

**Parameters**:
| Parameter | Type   | Required | Description                    |
|-----------|--------|----------|--------------------------------|
| filename  | string | Yes      | Name of file to download       |

**Response**: File download with appropriate Content-Type

**Example**:
```bash
curl http://localhost:5000/download/promo_image.png -o promo.png
```

---

### 4. GET /preview/<filename>

**Description**: Preview generated content in browser

**Parameters**:
| Parameter | Type   | Required | Description                    |
|-----------|--------|----------|--------------------------------|
| filename  | string | Yes      | Name of file to preview        |

**Response**: File content with appropriate MIME type
- Image: `image/png`
- Video: `video/mp4`

**Example**:
```bash
curl http://localhost:5000/preview/promo_image.png
```

---

## Python API Usage

### Using the App Programmatically

```python
from app import create_product_promotion, create_video_promotion

# Create image promotion
create_product_promotion(
    human_img_path="path/to/human.jpg",
    product_img_path="path/to/product.jpg",
    text="PROMO SPESIAL!",
    output_path="output.png"
)

# Create video promotion
create_video_promotion(
    human_img_path="path/to/human.jpg",
    product_img_path="path/to/product.jpg",
    text="PROMO SPESIAL!",
    output_path="output.mp4",
    duration=5
)
```

### Function Reference

#### `create_product_promotion()`

Creates a promotional image combining human and product photos.

**Parameters**:
- `human_img_path` (str): Path to human/model image
- `product_img_path` (str): Path to product image
- `text` (str, optional): Promotional text (default: "PROMO SPESIAL!")
- `output_path` (str, optional): Output file path (default: "output.png")

**Returns**: str - Path to generated image

**Output**: PNG image with dimensions 1920x1080

---

#### `create_video_promotion()`

Creates a promotional video with zoom animation.

**Parameters**:
- `human_img_path` (str): Path to human/model image
- `product_img_path` (str): Path to product image
- `text` (str, optional): Promotional text (default: "PROMO SPESIAL!")
- `output_path` (str, optional): Output file path (default: "output.mp4")
- `duration` (int, optional): Video duration in seconds (default: 5)

**Returns**: str - Path to generated video

**Output**: MP4 video with dimensions 1920x1080, 30 FPS

---

#### `remove_background()`

Removes background from an image.

**Parameters**:
- `image_path` (str): Path to input image

**Returns**: PIL.Image - Image with transparent background

**Note**: Uses rembg if available, otherwise returns original image with RGBA mode

---

#### `create_gradient_background()`

Creates a gradient background image.

**Parameters**:
- `width` (int): Width in pixels
- `height` (int): Height in pixels

**Returns**: PIL.Image - Gradient background image

**Colors**: Light blue (#C8DCFF) to white (#FFFFFF)

---

## Configuration

### App Configuration

```python
app.config['UPLOAD_FOLDER'] = 'uploads'  # Upload directory
app.config['OUTPUT_FOLDER'] = 'outputs'  # Output directory
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit
```

### Output Settings

```python
# Image resolution
width, height = 1920, 1080

# Video settings
fps = 30
duration = 5  # seconds

# Effects
zoom_factor = 1.1  # Zoom from 1.0 to 1.1
fade_duration = 1  # seconds
```

---

## Error Handling

### Common Errors

1. **Missing Files**
```json
{
  "error": "Missing files"
}
```
**Solution**: Ensure both human_photo and product_photo are uploaded

2. **Invalid File Type**
```json
{
  "error": "Invalid file type"
}
```
**Solution**: Use supported file formats (png, jpg, jpeg, gif)

3. **File Too Large**
```
413 Request Entity Too Large
```
**Solution**: Reduce file size to under 16MB

4. **Processing Error**
```json
{
  "error": "Error processing images: [detailed error]"
}
```
**Solution**: Check image format and integrity

---

## Rate Limiting

Currently no rate limiting is implemented. For production use, consider:
- Request rate limiting per IP
- Queue system for processing
- Background job processing
- CDN for serving outputs

---

## Security Considerations

1. **File Validation**: All uploads are validated for file type
2. **Filename Sanitization**: Using `werkzeug.utils.secure_filename()`
3. **Size Limits**: 16MB maximum per file
4. **Local Processing**: No data sent to external services
5. **Temporary Storage**: Files stored temporarily during processing

### Recommended Production Settings

```python
# Enable HTTPS
# Set CORS headers if needed
# Add authentication/authorization
# Implement rate limiting
# Add logging and monitoring
# Use secure session management
# Sanitize user inputs
```

---

## Performance Tips

1. **Image Size**: Use images around 1000x1000px for faster processing
2. **Background Removal**: Disable if not needed (remove rembg)
3. **Video Duration**: Shorter videos process faster
4. **Concurrent Requests**: Use async workers for multiple requests
5. **Caching**: Cache frequently used backgrounds and fonts

---

## Testing

### Unit Tests

```python
import unittest
from app import create_product_promotion

class TestPromotion(unittest.TestCase):
    def test_image_creation(self):
        result = create_product_promotion(
            'test_human.jpg',
            'test_product.jpg'
        )
        self.assertTrue(os.path.exists(result))
```

### Integration Tests

```python
import requests

def test_upload_endpoint():
    files = {
        'human_photo': open('human.jpg', 'rb'),
        'product_photo': open('product.jpg', 'rb')
    }
    data = {'promo_text': 'TEST PROMO'}
    
    response = requests.post(
        'http://localhost:5000/upload',
        files=files,
        data=data
    )
    
    assert response.status_code == 200
    assert response.json()['success'] == True
```

---

## Examples

### JavaScript/Fetch API

```javascript
const formData = new FormData();
formData.append('human_photo', humanFile);
formData.append('product_photo', productFile);
formData.append('promo_text', 'DISKON 50%!');
formData.append('output_type', 'image');

fetch('/upload', {
    method: 'POST',
    body: formData
})
.then(response => response.json())
.then(data => {
    console.log('Success:', data);
    // Download or preview the result
    window.location.href = `/download/${data.output_file}`;
})
.catch(error => console.error('Error:', error));
```

### Python Requests

```python
import requests

files = {
    'human_photo': open('human.jpg', 'rb'),
    'product_photo': open('product.jpg', 'rb')
}

data = {
    'promo_text': 'DISKON 50%!',
    'output_type': 'image'
}

response = requests.post(
    'http://localhost:5000/upload',
    files=files,
    data=data
)

if response.ok:
    result = response.json()
    print(f"Created: {result['output_file']}")
    
    # Download the file
    download = requests.get(
        f"http://localhost:5000/download/{result['output_file']}"
    )
    
    with open('promo.png', 'wb') as f:
        f.write(download.content)
```

---

## Version History

### v1.0.0
- Initial release
- Image and video generation
- Background removal support
- Web interface
- REST API

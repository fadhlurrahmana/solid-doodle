# UI Features and Interface Guide

## Interface Aplikasi

### 1. Halaman Utama (Home Page)

```
+------------------------------------------------------------------+
|                                                                  |
|           🎨 AI Product Promotion Editor                         |
|     Buat promosi produk profesional dengan AI -                  |
|         Upload foto manusia dan produk!                          |
|                                                                  |
+------------------------------------------------------------------+
|                                                                  |
|  +------------------------+    +------------------------+        |
|  |        👤              |    |        📦              |        |
|  |   Foto Manusia         |    |    Foto Produk         |        |
|  |                        |    |                        |        |
|  | Klik untuk upload foto |    | Klik untuk upload foto |        |
|  |      model/manusia     |    |        produk          |        |
|  |                        |    |                        |        |
|  |   [Preview Area]       |    |   [Preview Area]       |        |
|  |                        |    |                        |        |
|  +------------------------+    +------------------------+        |
|                                                                  |
|  Teks Promosi:                                                   |
|  +--------------------------------------------------------+      |
|  | PROMO SPESIAL!                                         |      |
|  +--------------------------------------------------------+      |
|                                                                  |
|  Tipe Output:                                                    |
|  +--------------------------------------------------------+      |
|  | Gambar (PNG)                           ▼              |      |
|  +--------------------------------------------------------+      |
|                                                                  |
|  +--------------------------------------------------------+      |
|  |              🚀 Buat Promosi                          |      |
|  +--------------------------------------------------------+      |
|                                                                  |
+------------------------------------------------------------------+
```

### 2. Hasil Promosi (Result Section)

```
+------------------------------------------------------------------+
|                                                                  |
|                   ✨ Hasil Promosi                               |
|                                                                  |
|  +--------------------------------------------------------+      |
|  |                                                        |      |
|  |             [Preview Image/Video]                     |      |
|  |                                                        |      |
|  |  +------------------+  +-------------------+           |      |
|  |  | Model/Manusia    |  |  Produk dengan    |           |      |
|  |  | dengan background|  |  white background |           |      |
|  |  | removed          |  |                   |           |      |
|  |  +------------------+  +-------------------+           |      |
|  |                                                        |      |
|  |          PROMO SPESIAL!                               |      |
|  |                                                        |      |
|  |          [Beli Sekarang!]                             |      |
|  |                                                        |      |
|  +--------------------------------------------------------+      |
|                                                                  |
|  +------------------------+  +-------------------------+         |
|  |   📥 Download         |  |   🔄 Buat Baru         |         |
|  +------------------------+  +-------------------------+         |
|                                                                  |
+------------------------------------------------------------------+
```

## Color Scheme

- **Primary Gradient**: Purple to Blue (#667eea to #764ba2)
- **Background**: White (#ffffff)
- **Text**: Dark Gray (#333333)
- **Accent**: Red for CTA (#ff3232)
- **Borders**: Light Gray (#e0e0e0)

## Responsive Design

### Desktop (1200px+)
- Two-column layout for upload boxes
- Full-width forms and buttons
- Large preview areas

### Mobile (< 768px)
- Single-column stacked layout
- Full-width upload boxes
- Touch-optimized buttons

## Interactive Elements

### Upload Boxes
- **Idle**: Dashed border, light background
- **Hover**: Solid border, darker background, slight lift effect
- **Active**: Shows preview image thumbnail

### Buttons
- **Primary Button**: Gradient background with shadow
- **Hover**: Lifts up with enhanced shadow
- **Disabled**: Reduced opacity, no interaction
- **Loading**: Shows spinner with "Memproses..." text

### Preview Areas
- Displays uploaded image thumbnails
- Rounded corners with shadow
- Max height: 300px
- Maintains aspect ratio

## Features Breakdown

### Upload Section
1. **Dual Upload**: Side-by-side human and product photo upload
2. **Visual Feedback**: Instant image preview after upload
3. **Drag & Drop**: Support for drag and drop (browser dependent)
4. **File Validation**: Checks file type and size

### Customization Options
1. **Promo Text Input**: Customizable promotional text
2. **Output Type Selector**: Choose between image or video output
3. **Real-time Preview**: See selected options before processing

### Result Display
1. **High-Quality Preview**: Full-size preview of generated content
2. **Video Player**: Controls for video playback
3. **Download Button**: One-click download
4. **New Promo Button**: Reset form for next creation

## Technical Features

### Frontend
- Responsive CSS Grid and Flexbox
- Smooth transitions and animations
- AJAX form submission (no page reload)
- Progress indicators
- Error handling with user-friendly messages

### Backend
- RESTful API endpoints
- File upload handling with security checks
- Image processing pipeline
- Video generation with effects
- Error handling and validation

## User Flow

```
Start → Upload Photos → Customize Text → Choose Output Type 
  ↓
Process → Generate Promo → Preview Result
  ↓
Download or Create New
```

## Accessibility Features

- Semantic HTML structure
- Clear labels and instructions
- Keyboard navigation support
- Error messages and success feedback
- Loading indicators for long operations

## Browser Compatibility

- Chrome/Edge (Latest)
- Firefox (Latest)
- Safari (Latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Performance

- Client-side image preview (no server upload until submit)
- Async processing with loading indicators
- Optimized image sizes
- Efficient video encoding
- Caching for repeated operations

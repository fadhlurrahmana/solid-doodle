# Quick Start Guide - AI Product Promotion Editor

## Cara Cepat Memulai

### 1. Instalasi Sederhana (Tanpa Virtual Environment)

```bash
# Clone repository
git clone https://github.com/fadhlurrahmana/solid-doodle.git
cd solid-doodle

# Install dependencies minimal (tanpa rembg)
pip install Flask Pillow opencv-python-headless numpy werkzeug

# Jalankan aplikasi
python app.py
```

### 2. Akses Aplikasi

Buka browser dan kunjungi: `http://localhost:5000`

### 3. Upload dan Buat Promosi

1. Upload foto manusia (JPG/PNG)
2. Upload foto produk (JPG/PNG)  
3. Tulis teks promosi
4. Pilih output: Gambar atau Video
5. Klik "Buat Promosi"
6. Download hasil

## Tips

- **Foto Manusia**: Gunakan foto dengan background yang jelas untuk hasil terbaik
- **Foto Produk**: Foto produk dengan latar belakang putih/bersih lebih bagus
- **Teks Promosi**: Singkat dan menarik (maksimal 3-4 kata)
- **Ukuran File**: Maksimal 16MB per file

## Troubleshooting

### Error: Module 'PIL' not found
```bash
pip install Pillow
```

### Error: Module 'cv2' not found
```bash
pip install opencv-python-headless
```

### Error: Module 'flask' not found
```bash
pip install Flask
```

### Background removal tidak berfungsi
Aplikasi akan menggunakan fallback mode. Untuk AI background removal:
```bash
pip install rembg[cpu]
```

## Fitur yang Tersedia

✅ Upload foto manusia dan produk
✅ Buat gambar promosi (1920x1080)
✅ Buat video promosi (5 detik)
✅ Custom teks promosi
✅ Download hasil
✅ Interface responsive
✅ Gradient background otomatis
✅ Layout profesional

## Docker Alternative

Jika instalasi pip bermasalah, gunakan Docker:

```bash
# Build image
docker build -t promo-editor .

# Run container
docker run -p 5000:5000 promo-editor
```

Atau dengan docker-compose:

```bash
docker-compose up
```

## Dokumentasi Lengkap

Lihat README.md untuk dokumentasi lengkap dan advanced features.

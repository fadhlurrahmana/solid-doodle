# AI Product Promotion Editor

Aplikasi web berbasis AI untuk membuat gambar dan video promosi produk profesional dengan mudah. Upload foto manusia dan foto produk, lalu biarkan AI membuat konten promosi yang menarik!

## ✨ Fitur

- 🎨 **Penghapusan Background Otomatis**: AI menghapus background dari foto manusia secara otomatis (dengan rembg)
- 🖼️ **Komposisi Profesional**: Menggabungkan foto manusia dan produk dengan layout yang menarik
- 📝 **Teks Promosi Custom**: Tambahkan teks promosi sesuai keinginan
- 🎬 **Output Video**: Buat video promosi dengan efek animasi zoom
- 📱 **Responsive Design**: Tampilan yang bagus di desktop maupun mobile
- ⚡ **Proses Cepat**: Hasil instan dengan kualitas tinggi

## 🚀 Cara Instalasi

### Prerequisites

- Python 3.8 atau lebih tinggi
- pip (Python package manager)

### Metode 1: Instalasi Langsung

1. Clone repository ini:
```bash
git clone https://github.com/fadhlurrahmana/solid-doodle.git
cd solid-doodle
```

2. Buat virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # Di Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. (Optional) Install rembg untuk background removal otomatis:
```bash
pip install rembg[cpu]
```

5. Jalankan aplikasi:
```bash
python app.py
```

6. Buka browser dan akses:
```
http://localhost:5000
```

### Metode 2: Menggunakan Docker

1. Clone repository:
```bash
git clone https://github.com/fadhlurrahmana/solid-doodle.git
cd solid-doodle
```

2. Build dan jalankan dengan Docker Compose:
```bash
docker-compose up -d
```

3. Akses aplikasi di:
```
http://localhost:5000
```

4. Stop aplikasi:
```bash
docker-compose down
```

## 📖 Cara Penggunaan

1. **Upload Foto Manusia**: Klik pada kotak "Foto Manusia" dan pilih foto model/manusia
2. **Upload Foto Produk**: Klik pada kotak "Foto Produk" dan pilih foto produk yang ingin dipromosikan
3. **Masukkan Teks Promosi**: Ubah teks promosi sesuai kebutuhan (default: "PROMO SPESIAL!")
4. **Pilih Tipe Output**: 
   - **Gambar (PNG)**: Untuk poster atau konten media sosial
   - **Video (MP4)**: Untuk iklan video dengan efek animasi
5. **Klik "Buat Promosi"**: Tunggu beberapa saat hingga AI memproses
6. **Download Hasil**: Klik tombol download untuk menyimpan hasil

## 🎨 Contoh Hasil

Aplikasi akan menghasilkan:
- **Gambar Promosi**: Resolusi HD (1920x1080) dengan komposisi profesional
- **Video Promosi**: Video 5 detik dengan efek zoom-in yang menarik

## 🛠️ Teknologi yang Digunakan

- **Flask**: Web framework Python untuk backend
- **PIL/Pillow**: Image processing dan manipulation
- **OpenCV**: Video processing dan effects
- **Rembg**: AI-powered background removal (optional)
- **HTML/CSS/JavaScript**: Frontend interface yang responsif

## 📂 Struktur Proyek

```
solid-doodle/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose configuration
├── demo.py              # Demo script untuk testing
├── test_app.py          # Test suite
├── templates/
│   └── index.html        # Main HTML template
├── static/
│   ├── css/
│   │   └── style.css     # Styling
│   └── js/
│       └── main.js       # Frontend JavaScript
├── uploads/              # Temporary uploaded files
└── outputs/              # Generated promotion files
```

## 🎯 Use Cases

- **E-commerce**: Promosi produk untuk toko online
- **Social Media Marketing**: Konten untuk Instagram, Facebook, TikTok
- **Digital Advertising**: Material iklan digital
- **Product Launch**: Campaign peluncuran produk baru
- **Influencer Marketing**: Konten promosi untuk influencer

## 🔧 Konfigurasi

Anda dapat mengubah konfigurasi di `app.py`:

```python
# Ukuran maksimal file upload (default: 16MB)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Resolusi output (default: 1920x1080)
width, height = 1920, 1080

# Durasi video (default: 5 detik)
duration = 5
```

## 🔒 Catatan Keamanan

- File maksimal 16MB untuk menghindari overload
- File diproses secara lokal di server
- Tidak ada data yang dikirim ke server eksternal
- Upload folder dapat dibersihkan secara berkala untuk menghemat space

## 🧪 Testing

Jalankan test suite untuk memverifikasi instalasi:

```bash
python test_app.py
```

Jalankan demo untuk melihat contoh output:

```bash
python demo.py
```

## 📝 License

MIT License - Feel free to use this project for personal or commercial purposes

## 👨‍💻 Author

Developed with ❤️ by fadhlurrahmana

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

### Cara Berkontribusi

1. Fork repository ini
2. Buat branch fitur baru (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 🐛 Known Issues

- Rembg memerlukan model AI yang cukup besar (~170MB) untuk background removal
- Video processing memerlukan waktu beberapa detik untuk video 5 detik
- Fallback background removal tidak secanggih AI (jika rembg tidak terinstall)

## 📧 Support

Jika ada pertanyaan atau masalah:
- Buat issue di GitHub repository
- Email: [Sesuaikan dengan email Anda]

## 🔄 Changelog

### Version 1.0.0 (2024)
- Initial release
- Background removal dengan rembg
- Image dan video generation
- Web interface yang responsif
- Docker support

## 🙏 Acknowledgments

- Flask team untuk web framework yang powerful
- rembg developers untuk AI background removal
- PIL/Pillow untuk image processing capabilities
- OpenCV untuk video processing features
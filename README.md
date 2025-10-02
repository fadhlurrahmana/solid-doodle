# AI Product Promotion Editor

Aplikasi web berbasis AI untuk membuat gambar dan video promosi produk profesional dengan mudah. Upload foto manusia dan foto produk, lalu biarkan AI membuat konten promosi yang menarik!

## ✨ Fitur

- 🎨 **Penghapusan Background Otomatis**: AI menghapus background dari foto manusia secara otomatis
- 🖼️ **Komposisi Profesional**: Menggabungkan foto manusia dan produk dengan layout yang menarik
- 📝 **Teks Promosi Custom**: Tambahkan teks promosi sesuai keinginan
- 🎬 **Output Video**: Buat video promosi dengan efek animasi zoom
- 📱 **Responsive Design**: Tampilan yang bagus di desktop maupun mobile
- ⚡ **Proses Cepat**: Hasil instan dengan kualitas tinggi

## 🚀 Cara Instalasi

### Prerequisites

- Python 3.8 atau lebih tinggi
- pip (Python package manager)

### Langkah Instalasi

1. Clone repository ini:
```bash
git clone https://github.com/fadhlurrahmana/solid-doodle.git
cd solid-doodle
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Jalankan aplikasi:
```bash
python app.py
```

4. Buka browser dan akses:
```
http://localhost:5000
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

## 🛠️ Teknologi yang Digunakan

- **Flask**: Web framework Python
- **PIL/Pillow**: Image processing
- **OpenCV**: Video processing
- **Rembg**: AI-powered background removal
- **HTML/CSS/JavaScript**: Frontend interface

## 📂 Struktur Proyek

```
solid-doodle/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
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

- E-commerce product promotions
- Social media marketing content
- Digital advertising materials
- Instagram/Facebook posts
- Product launch campaigns

## 🔒 Catatan Keamanan

- File maksimal 16MB
- File diproses secara lokal
- Tidak ada data yang dikirim ke server eksternal
- Upload folder dibersihkan secara berkala

## 📝 License

MIT License - Feel free to use this project for personal or commercial purposes

## 👨‍💻 Author

Developed with ❤️ by fadhlurrahmana

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📧 Support

Jika ada pertanyaan atau masalah, silakan buat issue di GitHub repository.
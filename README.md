# NeuStock by NeuroSynth

Aplikasi ini digunakan untuk memprediksi harga penutupan (closing price) saham di masa depan berdasarkan data historis. Aplikasi ini memanfaatkan model Deep Learning khususnya ACO-BiLSTM untuk menganalisis pola pergerakan harga saham sebelumnya dan menghasilkan estimasi harga penutupan pada periode berikutnya.

# Developer:

221111320 - Nadiyah Shofa Salsabila

221110837 - Callisto Carlos

# Arsitektur & Teknologi

[Frontend UI (nodejs)] <-> [Backend API (Flask)] <->  [DevOps (Docker Container)]

Teknologi yang digunakan:
1. Bahasa Pemrograman: Python, JavaScript
2. Framework: Flask (untuk backend), node.js (untuk frontend)
3. Tools dan Pustaka:
   - Flask
   - Flask-Cors
   - tensorflow
   - numpy
   - pandas
   - joblib
   - scikit-learn
5. DevOps: Docker (untuk containerization dan deployment)

# Petunjuk Instalasi Lokal (Wajib via Docker)

### 1. Clone Repository
```bash
git clone https://github.com/NadiyahShofaSalsabila/NeuStock.git
```

### 2. Jalankan Docker
```bash
docker-compose up --build
```

### 3. Jalankan website

http://localhost:3000 (Silahkan akses langsung di browser anda jika sudah berhasil melakukan instalasi lokal)

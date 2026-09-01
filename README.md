# 🏫 Sistem Prediksi Sekolah Unggul (AI Classifier)

Aplikasi web cerdas berbasis **Machine Learning (Decision Tree Classifier)** dan **Streamlit** untuk memprediksi kelayakan serta mutu sekolah berdasarkan 9 indikator utama standar pendidikan.

---

## ✨ Fitur Utama
- **🎨 Modern Pastel Pink & Gold UI**: Desain antarmuka responsif dengan tipografi *Plus Jakarta Sans* dan animasi *floating logo*.
- **⚡ Simulasi Cepat (Quick Presets)**: 4 tombol preset profil sekolah (Sekolah Unggul, Standar, Perlu Peningkatan, Reset).
- **👥 Status Cerdas Rasio Guru & Siswa**: Evaluasi real-time rasio guru terhadap murid berdasar standar Permendikbud.
- **📊 Visualisasi Grafik Interaktif (Plotly)**:
  - 🍩 *Donut Chart* Tingkat Keyakinan Model
  - 🕸️ *Radar Chart* Profil Mutu Sekolah vs Benchmark Standar Unggul
- **💡 Smart Insights & Rekomendasi**: Analisis otomatis poin keunggulan dan area peningkatan mutu.
- **📥 Ekspor Laporan (.txt)**: Download ringkasan hasil evaluasi dan rekomendasi lengkap.

---

## 🚀 Cara Menjalankan Secara Lokal

### 1. Clone Repository
```bash
git clone https://github.com/USERNAME/REPO-NAME.git
cd REPO-NAME
```

### 2. Buat & Aktifkan Virtual Environment (Opsional tapi Direkomendasikan)
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependensi
```bash
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi
```bash
streamlit run app.py
```
Buka browser pada alamat `http://localhost:8501`.

---

## 🛠️ Teknologi yang Digunakan
- **Python 3.10+**
- **Streamlit** (Web Application Framework)
- **Scikit-Learn** & **Joblib** (Machine Learning Decision Tree)
- **Plotly** (Interactive Data Visualizations)
- **Pandas** (Data Manipulation)

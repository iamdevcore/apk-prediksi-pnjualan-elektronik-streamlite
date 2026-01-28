📊 Dashboard Penjualan – Streamlit

Dashboard Penjualan adalah aplikasi berbasis Streamlit yang digunakan untuk menganalisis, memvisualisasikan, dan mengevaluasi data penjualan bulanan berdasarkan target yang telah ditentukan.
Aplikasi ini mendukung upload data Excel/CSV, menampilkan grafik penjualan, ringkasan KPI, serta detail evaluasi bulanan.

📌 Fitur Utama
1️⃣ Upload Data Penjualan

Mendukung file Excel (.xlsx) dan CSV (.csv)

Sistem drag & drop

Validasi format kolom data

2️⃣ Dashboard KPI Penjualan

Menampilkan ringkasan:

Rata-rata Penjualan

Rata-rata Selisih Penjualan vs Target

Rata-rata Persentase Pencapaian

Jumlah Bulan Tercapai & Tidak Tercapai

Bulan Terbaik

Tahun Terbaik

3️⃣ Grafik Penjualan & Target

Grafik garis penjualan bulanan

Perbandingan antara penjualan aktual dan target

Filter berdasarkan tahun

Tampilan dark mode modern

4️⃣ Evaluasi Bulanan

Tabel detail evaluasi penjualan per bulan

Informasi:

Tahun

Bulan

Penjualan

Target

Selisih

Persentase pencapaian

Status (Tercapai / Tidak Tercapai)

Filter status evaluasi
5️⃣ Input Manual (Opsional)

Menambahkan data tanpa upload file

Cocok untuk simulasi atau testing

🗂️ Struktur Folder Project
dashboard-penjualan-streamlit/
│
├── app.py                  # File utama aplikasi Streamlit
├── requirements.txt        # Daftar library yang digunakan
├── data_penjualan.csv      # Contoh data (opsional)
├── README.md               # Dokumentasi project
└── assets/                 # Screenshot aplikasi (opsional)

📄 Format Data yang Digunakan

Contoh struktur data dalam file Excel / CSV:

tahun	bulan	penjualan	target
1777	Jan	10	20
1777	Feb	11	21
1777	Mar	12	22

⚙️ Cara Install & Menjalankan Program
1️⃣ Clone Repository
git clone https://github.com/username/dashboard-penjualan-streamlit.git
cd dashboard-penjualan-streamlit

2️⃣ Install Dependency
pip install -r requirements.txt


Jika terjadi error:

python -m pip install -r requirements.txt

3️⃣ Jalankan Aplikasi Streamlit
streamlit run app.py


Atau:

python -m streamlit run app.py

4️⃣ Buka di Browser

Aplikasi akan berjalan di:

http://localhost:8501
📈 Alur Kerja Aplikasi

User membuka aplikasi Streamlit

Upload file Excel / CSV data penjualan

Sistem membaca dan memproses data

KPI penjualan dihitung otomatis

Grafik penjualan ditampilkan berdasarkan tahun

Evaluasi bulanan ditampilkan dalam tabel

User dapat memfilter status pencapaian

🎯 Tujuan Pembuatan Aplikasi

Membantu analisis performa penjualan

Mempermudah evaluasi pencapaian target

Menyediakan visualisasi data yang informatif

Digunakan sebagai project akademik / tugas kuliah

👨‍🎓 Author

Nama: (Isi Nama Kamu)
Program Studi: (Isi Prodi)
Universitas: (Isi Nama Kampus)
Tahun: 2025

📜 Lisensi

Project ini dibuat untuk keperluan akademik dan pembelajaran.
Bebas digunakan dan dikembangkan lebih lanjut.

🖼️ Screenshot Aplikasi
<img width="1915" height="1021" alt="Screenshot 2026-01-28 164122" src="https://github.com/user-attachments/assets/b397e27a-b211-4450-bf86-743112492e6e" />
<img width="1588" height="823" alt="Screenshot 2026-01-28 164141" src="https://github.com/user-attachments/assets/31e38e23-e5ff-41f4-9d29-684f91c7af1e" />
<img width="1591" height="863" alt="Screenshot 2026-01-28 164231" src="https://github.com/user-attachments/assets/e89455eb-e6e6-4c50-b90c-f869e5cdf98f" />
<img width="1592" height="798" alt="image" src="https://github.com/user-attachments/assets/00314258-813b-4ea8-8bef-4b617e2da933" />
<img width="318" height="926" alt="image" src="https://github.com/user-attachments/assets/56a6aae3-8289-4007-b769-c0ac52aa3e53" />

ANGGOTA KELOMPOK 
-Muhammad Ilham Riyadi (14022300009)
-Ritaju Arrifkiani (14022300007)
-Syanabila Oktaviyani H (14022300098)
-Nisrina Salsabila (14022300048)
-Gilang Maulana S (14022300058)
-Faiz Arizzudin (14022300013)




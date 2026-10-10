# Python Advanced Case Study

Nama: Nazwa Kamila Harati
NIM: 2595114036
Prodi: Teknik Informatika
Kelas: 1125B

Repository ini berisi pengerjaan tugas mandiri Python Advanced Topics yang terdiri dari tiga studi kasus. Setiap studi kasus dibuat dalam folder terpisah sesuai dengan konsep Python yang diterapkan.

## Studi Kasus
### 1 Analisis Nilai Mahasiswa

Program ini digunakan untuk menghitung nilai akhir mahasiswa berdasarkan nilai tugas sebesar 30%, UTS sebesar 30%, dan UAS sebesar 40%. Program juga menampilkan mahasiswa dengan nilai akhir di atas 80, menyusun peringkat berdasarkan nilai tertinggi, dan menentukan mahasiswa terbaik. Konsep yang digunakan meliputi List Comprehension, Lambda Function, Filtering, dan Sorting.

Folder: `case-01-analisis-nilai`

### 2 Streaming Data Sensor IoT

Program ini menyimulasikan pembacaan data suhu dari sensor IoT secara bertahap. Setiap pembacaan suhu dikelompokkan menjadi kategori Dingin, Normal, atau Panas. Program menggunakan Generator Function, `yield`, dan Iterator untuk memproses data satu per satu tanpa harus menyimpan seluruh pembacaan dalam sebuah list besar.

Folder: `case-02-iot-generator`

### 3 Sistem Keamanan Akun dan Audit Log Login

Program ini menerapkan validasi username dan password menggunakan Regular Expression (RegEx). Class `User` dengan `@property` digunakan untuk mengatur akses terhadap atribut username dan password, sedangkan decorator digunakan untuk mencatat waktu percobaan login, username, status login, dan alasan jika login ditolak. Konsep yang digunakan meliputi RegEx, Class dan Object, `@property`, serta Decorator.

Folder: `case-03-login-security`

## Struktur Folder

```text
python-advanced-case-study/
├── README.md
├── case-01-analisis-nilai/
│   ├── analisis_nilai.py
│   ├── output-analsis-nilai.png
│   └── README.md
├── case-02-iot-generator/
│   ├── iot_generator.py
│   ├── output.png
│   └── README.md
└── case-03-login-security/
    ├── main.py
    ├── output.png
    └── README.md
```

## Cara Menjalankan Program

Pastikan Python sudah terpasang di komputer.

Jalankan setiap program melalui terminal dari folder utama repository:

Studi Kasus 1 — Analisis Nilai Mahasiswa

```bash
python case-01-analisis-nilai/main.py
```

Studi Kasus 2 — Streaming Data Sensor IoT

```bash
python case-02-iot-generator/main.py
```

Studi Kasus 3 — Sistem Keamanan Akun dan Audit Log Login

```bash
python case-03-login-security/main.py
```

## Progres Pengerjaan

* [x] Studi Kasus 1: Analisis Nilai Mahasiswa
* [x] Studi Kasus 2: Streaming Data Sensor IoT
* [x] Studi Kasus 3: Sistem Keamanan Akun dan Audit Log Login
* [x] Membuat README untuk setiap studi kasus
* [x] Menyertakan output program pada setiap folder studi kasus
* [ ] Mengunggah seluruh berkas ke GitHub
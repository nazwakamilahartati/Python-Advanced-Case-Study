# Analisis Nilai Mahasiswa
## Deskripsi
Program ini digunakan untuk mengolah nilai lima mahasiswa berdasarkan nilai tugas, UTS, dan UAS. Nilai akhir dihitung dengan bobot tugas 30%, UTS 30%, dan UAS 40%. Program memiliki empat proses utama, yaitu menghitung nilai akhir mahasiswa, menampilkan mahasiswa dengan nilai akhir di atas 80, mengurutkan seluruh mahasiswa berdasarkan nilai tertinggi hingga terendah, serta menampilkan mahasiswa terbaik beserta NIM dan detail nilainya.

## Fitur Program
1. Menghitung Nilai Akhir: Menghitung nilai akhir setiap mahasiswa berdasarkan bobot nilai tugas, UTS, dan UAS yang telah ditentukan.

2. Memfilter Mahasiswa Berprestasi: Menampilkan mahasiswa yang memperoleh nilai akhir lebih dari 80.

3. Membuat Pemeringkatan Mahasiswa: Mengurutkan seluruh mahasiswa berdasarkan nilai akhir dari yang tertinggi hingga terendah.

4. Menampilkan Mahasiswa Terbaik: Menampilkan identitas mahasiswa dengan nilai akhir tertinggi, meliputi nama, NIM, program studi, kelas, nilai tugas, nilai UTS, nilai UAS, dan nilai akhir.

## Konsep Python yang Digunakan
1. List Comprehension: Digunakan untuk menghitung nilai akhir setiap mahasiswa secara ringkas.

2. Lambda Function: Digunakan untuk menentukan kondisi penyaringan mahasiswa dan kunci pengurutan berdasarkan nilai akhir.

3. Filtering: Menggunakan fungsi `filter()` untuk memilih mahasiswa yang memperoleh nilai akhir lebih dari 80.

4. Sorting: Menggunakan fungsi `sorted()` untuk mengurutkan mahasiswa berdasarkan nilai akhir dari yang tertinggi hingga terendah.

5. Dictionary: Digunakan untuk menyimpan data identitas dan nilai setiap mahasiswa dalam bentuk pasangan kunci dan nilai.

## Cara Menjalankan Program
Sebelum menjalankan program, pastikan Python telah terpasang di komputer. Buka terminal pada folder utama repository, kemudian jalankan program menggunakan perintah `python case-01-analisis-nilai/main.py`. Setelah program dijalankan, sistem akan memproses data mahasiswa dan menampilkan hasil perhitungan nilai akhir, daftar mahasiswa berprestasi, pemeringkatan mahasiswa, serta informasi lengkap mahasiswa dengan nilai akhir tertinggi.
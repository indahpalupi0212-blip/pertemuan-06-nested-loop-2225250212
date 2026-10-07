# Pertemuan 06 Nested Loop Python

- Nama: Indah Palupi Kusumaningrum
- NIM: 2225250212
- Kelas: 3F

## Tujuan

Pembelajaran ini bertujuan untuk:

- memahami konsep nested loop;
- membedakan loop luar dan loop dalam;
- membuat pola menggunakan nested loop;
- menggunakan akumulator untuk menghitung jumlah;
- menggunakan counter untuk melakukan pencacahan;
- melakukan tracing terhadap variabel `i` dan `j`;
- menguji program Python menggunakan beberapa test case;
- mengunggah hasil pekerjaan melalui GitHub.

## Cara Menjalankan

Pastikan Python sudah terpasang. Jalankan program melalui terminal VS Code dengan perintah berikut:

```bash
python3 tugas/tabel_perkalian_dan_statistik.py
```

Pada Windows, perintah berikut juga dapat digunakan:

```bash
python tugas/tabel_perkalian_dan_statistik.py
```

Untuk menjalankan latihan:

```bash
python3 latihan/01_pasangan_indeks.py
python3 latihan/02_pola_segitiga.py
python3 latihan/03_jumlah_per_baris.py
python3 latihan/04_hitung_pasangan.py
```

## Algoritma Tugas 3

Program `tabel_perkalian_dan_statistik.py` bekerja dengan langkah-langkah berikut:

1. Menampilkan judul program.
2. Membaca nilai `n` dari pengguna.
3. Memeriksa apakah nilai `n` positif.
4. Jika `n <= 0`, program meminta input ulang sampai nilai valid.
5. Menginisialisasi `total_semua` dengan nilai `0`.
6. Menginisialisasi `count_genap` dengan nilai `0`.
7. Menjalankan loop luar menggunakan variabel `i` dari `1` sampai `n`.
8. Menginisialisasi `total_baris` dengan nilai `0` pada awal setiap baris.
9. Menjalankan loop dalam menggunakan variabel `j` dari `1` sampai `n`.
10. Menghitung nilai perkalian dengan rumus `hasil = i * j`.
11. Menampilkan nilai `hasil` pada tabel.
12. Menambahkan `hasil` ke `total_baris`.
13. Menambahkan `hasil` ke `total_semua`.
14. Memeriksa apakah `hasil` merupakan bilangan genap.
15. Jika `hasil` genap, menambahkan `1` ke `count_genap`.
16. Menampilkan jumlah setiap baris setelah loop dalam selesai.
17. Menampilkan total seluruh hasil dan banyak hasil genap setelah kedua loop selesai.

## Hasil Pengujian

### Test Case 1: `n = 1`

Input:

```text
1
```

Keluaran:

```text
Tabel Perkalian dan Statistik
n: 1
   1 | jumlah baris = 1
Total seluruh hasil = 1
Banyak hasil genap = 0
```

Status: **Berhasil**

### Test Case 2: `n = 2`

Input:

```text
2
```

Keluaran:

```text
Tabel Perkalian dan Statistik
n: 2
   1   2 | jumlah baris = 3
   2   4 | jumlah baris = 6
Total seluruh hasil = 9
Banyak hasil genap = 3
```

Status: **Berhasil**

### Test Case 3: `n = 3`

Input:

```text
3
```

Keluaran:

```text
Tabel Perkalian dan Statistik
n: 3
   1   2   3 | jumlah baris = 6
   2   4   6 | jumlah baris = 12
   3   6   9 | jumlah baris = 18
Total seluruh hasil = 36
Banyak hasil genap = 5
```

Status: **Berhasil**

### Test Case 4: Input Tidak Valid

Input:

```text
0
```

Kemudian input ulang:

```text
2
```

Keluaran:

```text
Tabel Perkalian dan Statistik
n: 0
n harus positif.
n: 2
   1   2 | jumlah baris = 3
   2   4 | jumlah baris = 6
Total seluruh hasil = 9
Banyak hasil genap = 3
```

Status: **Berhasil**

## Tabel Ringkasan Pengujian

| No. | Input `n` | Jumlah Pasangan | Total Semua | Banyak Hasil Genap | Status |
|---:|---:|---:|---:|---:|---|
| 1 | 1 | 1 | 1 | 0 | Berhasil |
| 2 | 2 | 4 | 9 | 3 | Berhasil |
| 3 | 3 | 9 | 36 | 5 | Berhasil |
| 4 | 0 lalu 2 | 4 | 9 | 3 | Berhasil |

## Tracing untuk `n = 3`

Untuk `n = 3`, loop luar berjalan sebanyak `3` kali dan loop dalam berjalan sebanyak `3` kali untuk setiap loop luar.

Jumlah seluruh pasangan:

```text
3 x 3 = 9 pasangan
```

| `i` | `j` | `hasil = i * j` | `total_baris` |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 |
| 1 | 2 | 2 | 3 |
| 1 | 3 | 3 | 6 |
| 2 | 1 | 2 | 2 |
| 2 | 2 | 4 | 6 |
| 2 | 3 | 6 | 12 |
| 3 | 1 | 3 | 3 |
| 3 | 2 | 6 | 9 |
| 3 | 3 | 9 | 18 |

Hasil akhir:

```text
total_semua = 36
count_genap = 5
```

Hasil perkalian yang genap adalah:

```text
2, 2, 4, 6, 6
```

Jadi, banyak hasil genap adalah `5`.

## Analisis Efisiensi

Untuk input `n`, loop luar berjalan sebanyak `n` kali. Loop dalam juga berjalan sebanyak `n` kali pada setiap iterasi loop luar.

Oleh karena itu, badan loop dalam dieksekusi:

```text
n x n = n² kali
```

Contoh:

- untuk `n = 1`, terdapat `1 x 1 = 1` pasangan;
- untuk `n = 2`, terdapat `2 x 2 = 4` pasangan;
- untuk `n = 3`, terdapat `3 x 3 = 9` pasangan;
- untuk `n = 10`, terdapat `10 x 10 = 100` pasangan.

Pernyataan berikut merupakan bagian yang paling sering dieksekusi:

```python
hasil = i * j
```

Untuk input `n`, pernyataan tersebut dieksekusi sebanyak `n²` kali.

## Refleksi

### Mengapa `total_baris` direset pada setiap iterasi loop luar?

`total_baris` direset menjadi `0` pada awal setiap iterasi loop luar karena variabel tersebut hanya digunakan untuk menghitung jumlah pada satu baris. Jika tidak direset, jumlah baris sebelumnya akan ikut terbawa ke baris berikutnya.

### Mengapa `total_semua` tidak direset pada setiap baris?

`total_semua` digunakan untuk menghitung jumlah seluruh hasil perkalian dalam tabel. Oleh sebab itu, variabel ini harus diinisialisasi sebelum kedua loop dan tidak boleh direset pada setiap baris.

### Bagaimana cara membuktikan `count_genap` benar?

Setiap hasil diperiksa menggunakan kondisi:

```python
if hasil % 2 == 0:
```

Jika sisa pembagian hasil dengan `2` sama dengan `0`, berarti hasil tersebut genap dan `count_genap` bertambah satu.

### Kesalahan yang Ditemukan

Kesalahan yang dapat terjadi adalah menempatkan:

```python
total_baris = 0
```

di dalam loop dalam. Jika hal tersebut dilakukan, nilai `total_baris` akan selalu direset pada setiap kolom sehingga jumlah setiap baris menjadi tidak benar.

Perbaikannya adalah menempatkan `total_baris = 0` di dalam loop luar, tetapi sebelum loop dalam:

```python
for i in range(1, n + 1):
    total_baris = 0

    for j in range(1, n + 1):
        total_baris += i * j
```

## Kesimpulan

Nested loop digunakan untuk memproses data dalam bentuk baris dan kolom. Pada program ini, loop luar mengatur baris, sedangkan loop dalam mengatur kolom.

Akumulator `total_baris` digunakan untuk menghitung jumlah setiap baris dan direset pada setiap baris. Akumulator `total_semua` digunakan untuk menghitung jumlah seluruh tabel. Sementara itu, `count_genap` digunakan sebagai counter yang hanya bertambah ketika hasil perkalian merupakan bilangan genap.

## Sumber dan Integritas Akademik

Materi utama berasal dari bahan ajar Pertemuan 06 Algoritma dan Pemrograman tentang nested loop, pola, akumulasi, pencacahan, VS Code, dan GitHub.

Kode harus dipahami dan dapat dijelaskan oleh pemilik repository. Bantuan dari dokumentasi, dosen, teman.
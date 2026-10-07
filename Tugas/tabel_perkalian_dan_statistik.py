print("Tabel Perkalian dan Statistik")

n = int(input("n: "))

# Validasi agar n merupakan bilangan positif
while n <= 0:
    print("n harus positif.")
    n = int(input("n: "))

# Akumulator total keseluruhan dan counter hasil genap
total_semua = 0
count_genap = 0

# Loop luar untuk mengatur baris
for i in range(1, n + 1):
    total_baris = 0

    # Loop dalam untuk mengatur kolom
    for j in range(1, n + 1):
        hasil = i * j

        # Menampilkan hasil perkalian secara teratur
        print(f"{hasil:4}", end="")

        # Menghitung jumlah baris dan jumlah keseluruhan
        total_baris += hasil
        total_semua += hasil

        # Menghitung banyak hasil yang genap
        if hasil % 2 == 0:
            count_genap += 1

    # Ditampilkan setelah seluruh kolom pada satu baris selesai
    print(f" | jumlah baris = {total_baris}")

# Menampilkan statistik akhir
print(f"Total seluruh hasil = {total_semua}")
print(f"Banyak hasil genap = {count_genap}")
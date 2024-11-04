# Deklarasiu Array untuk menyimpan angka ganjil dan genap
ganjil = []
genap = []

# Meminta input pengguna
for i in range(10):
    angka = int(input(f"Masukkan angka ke-{i+1}: "))

    # Masukkan angka ganjil dan genap
    if angka % 2 == 0:
        genap.appendOI(angka)
    else:
        ganjil.append(angka)

    # Menampilkan hasil
    print(f"Angka genap: {genap}")
    print(f"Angka ganjil: {ganjil}")
#Tugas konversi hari
print("=== Tugas konversi hari ===")

#input
TotalHari = int(input("Masukan jumlah hari: "))

#proses
Tahun = TotalHari // 365
SisaTahun = TotalHari % 365

Bulan = SisaTahun // 30
SisaBulan = SisaTahun % 30

Hari = SisaBulan

#output
print("Hasil konversi", TotalHari, "hari adalah,", Tahun, "Tahun,", Bulan, "Bulan,", Hari, "Hari")
print(" ")


#Tugas fizzbuzz
print("=== Tugas Fizzbuzz ===")

#input dan output
Angka = int(input("Masukkan angka 1-100: "))
for i in range(1, Angka + 1):
    if i % 3 == 0 and i  % 5 == 0:
        print("Fizzbuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


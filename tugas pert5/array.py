#data mahasiswa
nama = ["Asep", "Budi", "Cecep"]

nilai = [ [50, 70, 40, 80], 
          [78, 78, 80, 65],
          [57, 88, 67, 69],
]

nama_mk = ["MK1", "MK2", "MK3", "MK4"]

#CARI MAHASISWA TERPINTAR
rata_mhs = []

#mencari rata-rata mahasiswa
for i in range(3):
    jumlah = nilai[i][0] + nilai[i][1] + nilai[i][2] + nilai[i][3]
    rata = jumlah/4
    rata_mhs.append(rata)

#mencari rata-rata tertinggi 
rata_tertinggi = rata_mhs[0]
nama_terpintar = nama[0]

for i in range(3):
    if rata_mhs[i] > rata_tertinggi:
        rata_tertinggi = rata_mhs[i]
        nama_terpintar = nama[i]


#MENCARI RATA-RATA SETIAP MATKUL
rata_mk = []

for i in range(4):
    jumlah = nilai[0][i] + nilai[1][i] + nilai[2][i] 
    rata = jumlah / 3
    rata_mk.append(rata)

#mencari rata-rata terkecil
rata_terkecil = rata_mk[0]
mk_terkecil = nama_mk[0]

for i in range(4):
    if rata_mk[i] < rata_terkecil:
        rata_terkecil = rata_mk[i]
        mk_terkecil = nama_mk[i]

#TAMPILKAN OUTPUT
print("Mahasiswa Terpintar  :", nama_terpintar, "(Nilai  :", rata_tertinggi, ")")
print(f"Mata Kuliah Nilai Terkecil  : {mk_terkecil} (Nilai  : {rata_terkecil:.2f})")



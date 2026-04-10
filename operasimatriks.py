#fungsi input matriks
def input_matriks(baris, kolom):
    matriks = []
    for i in range(baris):
        row = []
        for j in range(kolom):
            nilai = int(input(f"Masukkan nilai [{i}][{j}]: "))
            row.append(nilai)
        matriks.append(row)   
    return matriks

#fungsi tampilkan matriks
def tampilkan(m):
    for row in m:
        print(row)

#penjumlahan
def tambah(A,B,baris,kolom):
    hasil = []
    for i in range(baris):
        row = []
        for j in range(kolom):
            row.append(A[i][j] + B[i][j])  
        hasil.append(row)
    return hasil

#pengurangan
def kurang(A,B,baris,kolom):
    hasil = []
    for i in range(baris):
        row = []
        for j in range(kolom):
            row.append(A[i][j] - B[i][j])
        hasil.append(row)
    return hasil

#perkalian
def kali(A,B,bA,kA,kB):
    hasil = []
    for i in range(bA):
        row = []
        for j in range(kB):
            total = 0
            for k in range(kA):
                total += A[i][k] * B[k][j]                
            row.append(total)
        hasil.append(row)
    return hasil
        
#menu
while True:
    print("\n===== MENU OPERASI MATRIKS =====")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("0. Exit")
    
    pilih = input("Pilih menu: ")

    if pilih == "1":
        baris = int(input("Jumlah baris: "))
        kolom = int(input("Jumlah kolom: "))
        
        print("Matriks A")
        A = input_matriks(baris, kolom)
        
        print("Matriks B")
        B = input_matriks(baris, kolom)
        
        hasil = tambah(A, B, baris, kolom)
        print("Hasil Penjumlahan:")
        tampilkan(hasil)

    elif pilih == "2":
        baris = int(input("Jumlah baris: "))
        kolom = int(input("Jumlah kolom: "))
        
        print("Matriks A")
        A = input_matriks(baris, kolom)
        
        print("Matriks B")
        B = input_matriks(baris, kolom)
        
        hasil = kurang(A, B, baris, kolom)
        print("Hasil Pengurangan:")
        tampilkan(hasil)

    elif pilih == "3":
        bA = int(input("Baris matriks A: "))
        kA = int(input("Kolom matriks A: "))
        bB = int(input("Baris matriks B: "))
        kB = int(input("Kolom matriks B: "))
        
        if kA != bB:
            print("Perkalian tidak bisa dilakukan! kolom dan baris harus sama!")
        else:
            print("Matriks A")
            A = input_matriks(bA, kA)
            
            print("Matriks B")
            B = input_matriks(bB, kB)
            
            hasil = kali(A, B, bA, kA, kB)
            print("Hasil Perkalian:")
            tampilkan(hasil)

    elif pilih == "0":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid!")
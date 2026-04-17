#TUGAS NIM GENAP

def tampilkan_fibonacci(n):
    a, b = 1, 1
    hasil = []
    for i in range(n):
        hasil.append(str(a))
        a, b = b, a + b
    
    print(", ".join(hasil))

#Menu
while True:
    print("\n===== MENU PILIHAN =====")
    print("1. Barisan Fibonacci")
    print("2. M kali N")
    print("0. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == '1':
        jumlah = int(input("Masukan jumlah suku: "))
        print(f"Barisan fibonacci sebanyak {jumlah} suku: ")
        tampilkan_fibonacci(jumlah)
    
    elif pilih == '2':
        m = int(input("Masukkan suatu bilangan bulat: "))
        n = int(input("Masukkan suatu bilangan pengali: "))
        hasil = m * n
        print(f"{m} x {n} = {hasil}")

    elif pilih == '0':
        print("Terimakasih! Program selesai.")
        break

    else:
        print("Coba lagi!")
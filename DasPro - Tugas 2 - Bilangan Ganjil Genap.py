n = int(input("Masukkan angka: "))
angka = n

for i in range(1):
    if angka % 2 == 0:
        print(f"{angka} adalah bilangan genap.")
    else:
        print(f"{angka} adalah bilangan ganjil.")

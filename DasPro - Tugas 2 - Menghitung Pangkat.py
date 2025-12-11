angka = int(input("Masukkan angka: "))
pangkat = int(input("Masukkan pangkat: "))

hasil = 1
for i in range(pangkat):
    hasil *= angka

print(f"{angka} pangkat {pangkat} adalah {hasil}")

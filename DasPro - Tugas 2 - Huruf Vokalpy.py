kata = input("Masukkan kata: ")

vokal = "aeiouAEIOU"
jumlah_vokal = 0
i = 0

while i < len(kata):
    if kata[i] in vokal:
        jumlah_vokal += 1
    i += 1

print(f"Jumlah huruf vokal dalam kata tersebut adalah: {jumlah_vokal}")

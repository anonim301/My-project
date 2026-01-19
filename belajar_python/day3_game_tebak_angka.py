import random

angka = random.randint(1, 10)
kesempatan = 3

print("=== GAME TEBAK ANGKA ===")
print("Tebak angka 1-10")
print("Hanya 3 kesempatan")

for i in range(kesempatan):
        tebakan = int(input(f"Tebakan ke-{i+1}: "))

        if tebakan < angka:
                print("Angka terlalu kecil")
        elif tebakan > angka:
                print("Angka terlalu besar")
        else:
                print("Tebakan BENAR!")
                break
else:
        print("Kesempatan habis, coba lagi! ")

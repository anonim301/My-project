yprint("===KATEGORI UMUR===")
print("=" * 15)

umur = int(input("Masukkan umur: "))

#program
if umur <= 2:
        kategori = "Bayi"
elif umur <= 5:
        kategori = "Balita"
elif umur <= 12:
        kategori = "Anak-anak"
elif umur <= 17:
        kategori = "Remaja"
elif umur <= 25:
        kategori = "Dewasa muda"
elif umur <= 35:
        kategori = "Dewasa"
elif umur <= 55:
        kategori = "Paruh baya"
elif umur <= 65:
        kategori = "Lansia awal"
else:
        kategori = "Lansia"


print(f"Kategori: {kategori}")

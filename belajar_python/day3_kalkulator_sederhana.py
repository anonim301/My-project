print("===KALKULATOR SEDERHANA===")
print("pilih operasi: ")
print("1. Penjumlahan")
print("2. Pengurangan ")
print("3. Perkalian")
print("4. Pembagian")
print("5. Bagi bulat")

pilihan = input("Masukkan pilihan: ")
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

if pilihan == "1":
        hasil = angka1 + angka2
elif pilihan == "2":
        hasil = angka1 - angka2
elif pilihan == "3":
        hasil = angka1 * angka2
elif pilihan == "4":
        hasil = angka1 / angka2
elif pilihan == "5":
        hasil = angka1 // angka2
else:
        print("ERROR, tidak ada di pilihan! ")


print(f"Hasil: {hasil}")

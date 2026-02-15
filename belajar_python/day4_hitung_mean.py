total = 0
jumlah = 0

while True:
        data = input("Masukkan angka: ")
        if data == "selesai":
                break
        try:
                total += int(data)
                jumlah += 1
                rata_rata = (total / jumlah)
        except ValueError:
                print("Harap masukkan angka atau ketik 'selesai'!!! ")

print(f"{'jumlah angka':<15}: {jumlah}")
print(f"{'Total':<15}: {total}")
print(f"{'Mean':<15}: {rata_rata:.2f}")



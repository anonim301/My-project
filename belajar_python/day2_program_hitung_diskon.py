print("===PROGRAM HITUNG DISKON===")
print("#" * 30)

harga = float(input("Total harga barang: "))
jumlah_barang = int(input("Jumlah barang: "))

#diskon:10% jika harga barang > 25000

#hitung
subtotal = harga * jumlah_barang

if subtotal > 25000:
        diskon = subtotal * 0.1
else:
        diskon = 0

total = subtotal - diskon

print(f"{'Subotal':<12}: {subtotal}")
print(f"{'Diskon':<12}: {diskon}")
print(f"{'Total harga':<12}: {total}")

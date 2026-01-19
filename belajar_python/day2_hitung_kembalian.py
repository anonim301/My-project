print("=== HITUNG KEMBALIAN ===")
print("=" * 20)

total_belanja = int(input("Total belanja: "))
bayar = int(input("Uang dibayar: "))

kembalian = bayar - total_belanja

print(f"{'Kembalian':<15}: {kembalian}")
print("\nDalam pecahan: ")

pecahan = [10000, 2000, 500]

for p in pecahan:
        jumlah = kembalian // p
        kembalian %= p
        print(f"- {p:<6}: {jumlah} lembar")

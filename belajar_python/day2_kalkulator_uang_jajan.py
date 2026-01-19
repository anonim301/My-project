print("===KALKULATOR UANG JAJAN===")
uang = float(input("Berapa uangmu per hari: "))
hari = int(input("Berapa hari sekolah dalam seminggu: "))
total_uang = (uang * hari)
nabung = 5000 * hari
sisa_uang = (total_uang - nabung)

print(f"{'Total uang seminggu':<25}: {total_uang}")
print(f"{'Jika nabung 5000 per hari':<25}: {nabung}")
print(f"{'Sisa uang':<25}: {sisa_uang}")

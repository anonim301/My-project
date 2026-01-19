print("===SISTEM PENILAIAN SISWA===")
print("=" * 30)

nama = input("Masukkan nama: ")
nilai_mtk = float(input("Masukkan nilai mtk: "))
nilai_ipa = float(input("Masukkan nilai ipa: "))
nilai_bindo = float(input("Masukkan nilai bahasa indonesia: "))

#hitung rata-rata
rata = (nilai_mtk + nilai_ipa + nilai_bindo) / 3

#grade nilai
if rata >= 90:
  grade = "A"
  predikat = "Istimewa"
elif rata >= 80:
  grade = "B"
  predikat = "Baik"
elif rata >= 70:
  grade = "C"
  predikat = "Cukup"
elif rata >= 60:
  grade = "D"
  predikat = "Kurang"
else:
  grade = "E"
  predikat = "Gagal"

#status
if rata >= 80:
  status = "LULUS"
else:
  status = "TIDAK LULUS"
#hasil
print("=== HASIL ===")
print(f"{'Name':<15}: {nama}")
print(f"{'Rata-rata':<15}: {rata}")
print(f"{'Grade':<15}: {grade}")
print(f"{'Predikat':<15}: {predikat}")
print(f"{'Status':<15}: {status}")

#ucapan
if status == "LULUS":
  print("Selamat anda dinyatakan lulus")
else:
  print("Maaf anda dinyatakan tidak lulus")

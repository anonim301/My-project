print("=== HITUNG RATA RATA NILAI===")
print("#" * 20)

nilai1 = float(input("Masukkan nilai pertama: "))
nilai2 = float(input("Masukkan nilai kedua: "))
nilai3 = float(input("Masukkan nilai ketiga: "))

#program
rata_rata = (nilai1 + nilai2 + nilai3) / 3

if rata_rata >= 85:
        grade = "A"
elif rata_rata >= 75:
        grade = "B"
elif rata_rata >= 55:
        grade = "C"
elif rata_rata >= 40:
        grade = "D"
else:
        grade = "E"

print(f"{'Nilai rata-rata':<25}: {rata_rata:.2f}")
print(f"{'Grade':<25}: {grade}")

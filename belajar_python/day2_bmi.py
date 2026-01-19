print("===HITUNG BMI (Body Max Index)===")

#variabel
tinggi = float(input("Berapa tinggi badanmu (cm): "))
berat_badan = float(input("Berapa berat badanmu (kg): "))

konversi_meter = tinggi / 100
bmi = berat_badan / (konversi_meter ** 2)

if bmi < 18.5:
    kategori = "Kurus"
elif bmi < 25:
    kategori = "Normal"
elif bmi < 30:
    kategori = "Gemuk"
else:
    kategori = "Obesitas"

print(f"{'BMI':<12}: {bmi:.2f}")
print(f"{'Kategori':<12}: {kategori}")

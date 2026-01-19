print("===KONVERSI SUHU===")
print("#" * 20)

celcius = float(input("Masukkan suhu awal dalam (celcius): "))

#Hitung
fahrenheit = (celcius * 9 / 5) + 32
kelvin = celcius + 273.15

print(f"{'Suhu dalam Fahrenheit':<12}: {fahrenheit}")
print(f"{'Suhu dalam Kelvin':<12}: {kelvin}")

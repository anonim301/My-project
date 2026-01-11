name = input("Siapa namamu: ")
kelas = int(input("kamu kelas berapa: "))
sekolah = input("Dimana sekolahmu: ")
hobi = input("Hobimu: ")
uang = float(input("Berapa uang jajanmu: "))

uang_seminggu = (uang * 6)

#teks
print("KARTU NAMA DIGITAL")
print("#" * 10)

print(f"{'Name':<12}: {name}")
print(f"{'Kelas':<12}: {kelas}")
print(f"{'Sekolah':<12}: {sekolah}")
print(f"{'Hobi':<12}: {hobi}")
print(f"{'Uang jajan':<12}: {uang_seminggu}")

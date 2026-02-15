n = int(input("Masukkan bilangan bulat positif: "))

faktor = []

for i in range(1, n + 1):
        if n % 1 == 0:
                faktor.append(i)
print(f"{'Faktor dari {n}':<15}: {", ".join(str(x) for x in faktor)}")

n = int(input("Masukkan bilangan: "))

if n < 2:
        print(f"{n} bukan bilangan prima! ")
else:
        prima = True

        for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                        prima = False
                        break

if prima:
        print(f"{n} adalah bilangan prima")
else:
        print(f"{n} bukan bilangan prima")

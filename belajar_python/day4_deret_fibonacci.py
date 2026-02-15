n = int(input("Masukkan jumlah bilangan fibonacci: "))

a, b = 0, 1
fib_list = []

for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b

print(", ".join(str(num) for num in fib_list))

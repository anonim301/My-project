import math
from datetime import datetime

class AdvancedCalculator:
    def __init__(self):
        self.history = []
        self.memory = 0
        self.variables = {}

    def log_operation(self, operation, result):
        """Catat riwayat perhitungan"""
        self.history.append({
            "waktu": datetime.now().strftime("%H:%M:%S"),
            "operasi": operation,
            "hasil": result
        })

    def show_history(self):
        """Tampilkan riwayat"""
        if not self.history:
            print("Belum ada riwayat")
            return

        print("\n📜 RIWAYAT PERHITUNGAN")
        print("-" * 50)
        for i, log in enumerate(self.history[-10:], 1):  # 10 terakhir
            print(f"{i}. {log['waktu']} - {log['operasi']} = {log['hasil']}")

    # Operasi dasar
    def tambah(self, a, b):
        result = a + b
        self.log_operation(f"{a} + {b}", result)
        return result

    def kurang(self, a, b):
        result = a - b
        self.log_operation(f"{a} - {b}", result)
        return result

    def kali(self, a, b):
        result = a * b
        self.log_operation(f"{a} × {b}", result)
        return result

    def bagi(self, a, b):
        if b == 0:
            raise ValueError("Tidak bisa membagi dengan nol!")
        result = a / b
        self.log_operation(f"{a} ÷ {b}", result)
        return result

    # Operasi advanced
    def pangkat(self, a, b):
        result = a ** b
        self.log_operation(f"{a} ^ {b}", result)
        return result

    def akar(self, a):
        if a < 0:
            raise ValueError("Tidak bisa akar negatif!")
        result = math.sqrt(a)
        self.log_operation(f"√{a}", result)
        return result

    def persen(self, a):
        result = a / 100
        self.log_operation(f"{a}%", result)
        return result

    def faktorial(self, a):
        if a < 0:
            raise ValueError("Tidak bisa faktorial negatif!")
        if a != int(a):
            raise ValueError("Faktorial hanya untuk bilangan bulat!")
        result = math.factorial(int(a))
        self.log_operation(f"{a}!", result)
        return result

    # Memory operations
    def memory_add(self, value):
        self.memory += value
        print(f"✅ M+ : {value} → Memory: {self.memory}")

    def memory_sub(self, value):
        self.memory -= value
        print(f"✅ M- : {value} → Memory: {self.memory}")

    def memory_recall(self):
        print(f"📋 Memory: {self.memory}")
        return self.memory

    def memory_clear(self):
        self.memory = 0
        print("🗑️ Memory cleared!")

    # Variable operations
    def set_var(self, name, value):
        self.variables[name] = value
        print(f"✅ Variabel {name} = {value}")

    def get_var(self, name):
        if name not in self.variables:
            raise KeyError(f"Variabel '{name}' tidak ditemukan!")
        return self.variables[name]

    # Calculator dengan ekspresi sederhana
    def calculate(self, ekspresi):
      try:
        ekspresi = ekspresi.replace('^', '**')
        ekspresi = ekspresi.replace('×', '*')
        ekspresi = ekspresi.replace('÷', '/')

        # Tambahin fungsi yang diizinkan
        allowed_functions = {
            "sqrt": math.sqrt,
            "sin": math.sin,
            "cos": math.cos,
            "log": math.log
        }

        result = eval(ekspresi, {"__builtins__": None}, allowed_functions)

        self.log_operation(ekspresi, result)
        return result

      except Exception as e:
        raise ValueError(f"Ekspresi tidak valid: {e}")

def main():
    calc = AdvancedCalculator()

    print("="*50)
    print("🧮 ADVANCED CALCULATOR")
    print("="*50)
    print("Operasi:")
    print("  +, -, ×, ÷ : Operasi dasar")
    print("  ^          : Pangkat")
    print("  sqrt(x)    : Akar kuadrat")
    print("  %(x)       : Persen")
    print("  !(x)       : Faktorial")
    print("\nMemory:")
    print("  M+(x)      : Tambah ke memory")
    print("  M-(x)      : Kurang dari memory")
    print("  MR         : Recall memory")
    print("  MC         : Clear memory")
    print("\nVariabel:")
    print("  var(nama, nilai) : Set variabel")
    print("  get(nama)        : Ambil variabel")
    print("\nLainnya:")
    print("  history    : Lihat riwayat")
    print("  clear      : Clear screen")
    print("  quit       : Keluar")

    while True:
        try:
            user_input = input("\n>> ").strip().lower()

            if user_input == "quit":
                print("👋 Sampai jumpa!")
                break

            elif user_input == "history":
                calc.show_history()

            elif user_input == "clear":
                print("\n" * 2)

            elif user_input == "mr":
                calc.memory_recall()

            elif user_input == "mc":
                calc.memory_clear()

            elif user_input.startswith("m+(") and user_input.endswith(")"):
                value = float(user_input[3:-1])
                calc.memory_add(value)

            elif user_input.startswith("m-(") and user_input.endswith(")"):
                value = float(user_input[3:-1])
                calc.memory_sub(value)

            elif user_input.startswith("var(") and user_input.endswith(")"):
                # Format: var(nama, nilai)
                content = user_input[4:-1]
                parts = content.split(',')
                if len(parts) == 2:
                    name = parts[0].strip()
                    value = float(parts[1].strip())
                    calc.set_var(name, value)
                else:
                    print("Format: var(nama, nilai)")

            elif user_input.startswith("get(") and user_input.endswith(")"):
                name = user_input[4:-1].strip()
                value = calc.get_var(name)
                print(f"{name} = {value}")

            else:
                # Coba sebagai ekspresi matematika
                try:
                    # Cek apakah ada variabel
                    for var_name, var_value in calc.variables.items():
                        user_input = user_input.replace(var_name, str(var_value))

                    result = calc.calculate(user_input)
                    print(f"= {result}")
                except Exception as e:
                    print(f"❌ Error: {e}")

        except ValueError as e:
            print(f"❌ Error: {e}")
        except KeyError as e:
            print(f"❌ Error: {e}")
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()

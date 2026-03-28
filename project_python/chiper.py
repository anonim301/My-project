import os

# =========================
# CLEAR SCREEN
# =========================
def clear():
    os.system("clear")


# =========================
# ENKRIPSI
# =========================
def enkripsi(teks, key):
    hasil = ""

    for char in teks:
        if char.isalpha():  # hanya huruf
            shift = key % 26

            if char.islower():
                hasil += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                hasil += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            hasil += char  # angka & simbol tetap

    return hasil


# =========================
# DEKRIPSI
# =========================
def dekripsi(teks, key):
    return enkripsi(teks, -key)


# =========================
# MENU
# =========================
def menu():
    while True:
        print("\n=== CAESAR CIPHER ===")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            teks = input("Masukkan teks: ")
            key = int(input("Masukkan key (shift): "))
            hasil = enkripsi(teks, key)
            print(f"🔐 Hasil Enkripsi: {hasil}")

        elif pilih == "2":
            teks = input("Masukkan teks terenkripsi: ")
            key = int(input("Masukkan key (shift): "))
            hasil = dekripsi(teks, key)
            print(f"🔓 Hasil Dekripsi: {hasil}")

        elif pilih == "3":
            print("Keluar...")
            break

        else:
            print("❌ Menu tidak valid")


# =========================
# RUN
# =========================
menu()

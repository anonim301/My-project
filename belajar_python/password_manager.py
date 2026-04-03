import json
import os

DATA_FILE = "password.json"
MASTER_PASSWORD = "admin123"

#ENCRYPT/DECRYPT
def encrypt(text, key=3):
  result = ""
  for char in text:
    result += chr((ord(char) + key) % 236)
  return result

def decrypt(text, key=3):
  return encrypt(text, -key)

#LOAD & SAVE
def load_data():
  if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
      return json.load(f)
  return {}

def save_data(data):
  with open(DATA_FILE, "w") as f:
    json.dump(data, f, indent=4)

#AUTH
def login():
  pw = input("Masukkan master password: ")
  return pw == MASTER_PASSWORD

#TAMBAH AKUN
def add_account(data):
  website = input("Website: ")
  username = input("Username: ")
  password = input("Password: ")

  data[website] = {
    "username": username,
    "password": encrypt(password)
  }

  save_data(data)
  print("[√] Tersimpan")

#LIHAT SEMUA
def view_accounts(data):
  if not data:
    print("Kosong")
    return

  for site, info in data.items():
    print(f"\n[!]{site}")
    print(f"User: {info['username']}")
    print(f"Pass: {decrypt(info['password'])}")

#CARI
def search_account(data):
  key = input("Cari website: ")

  if key in data:
    info = data[key]
    print(f"\n{key}")
    print(f"User: {info['username']}")
    print(f"Pass: {decrypt(info['password'])}")
  else:
    print("[X] Tidak ditemukan")

#HAPUS
def delete_account(data):
  key = input("Website: ")

  if key in data:
    del data[key]
    save_data(data)
    print("[!] Hapus")
  else:
    print("[X] Tidak ditemukan")

# MAIN
def main():
    if not login():
        print("❌ Akses ditolak!")
        return

    data = load_data()

    while True:
        print("\n=== PASSWORD MANAGER ===")
        print("1. Tambah akun")
        print("2. Lihat semua")
        print("3. Cari")
        print("4. Hapus")
        print("0. Keluar")

        pilih = input("Pilih: ")

        if pilih == "1":
            add_account(data)
        elif pilih == "2":
            view_accounts(data)
        elif pilih == "3":
            search_account(data)
        elif pilih == "4":
            delete_account(data)
        elif pilih == "0":
            break
        else:
            print("❌ Salah input")


if __name__ == "__main__":
    main()

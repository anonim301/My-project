import os

#DATA AWAL
buku = {
  "ISBN-001": {
    "judul": "Python Programming",
    "penulis": "John Doe",
    "tahun": 2024,
    "stok": 5,
    "dipinjam": 0
  }
}

#CLEAR
def clear():
  os.system("clear")

#1.TAMBAH BUKU
def tambah_buku():
  isbn = input("Masukkan ISBN: ")

  if isbn in buku:
    print("[X] ISBN sudah ada")
    return

  judul = input("Judul: ")
  penulis = input("Penulis: ")
  tahun = int(input("Tahun: "))
  stok = int(input("Stok: "))

  buku[isbn] = {
    "judul": judul,
    "penulis": penulis,
    "tahun": tahun,
    "stok": stok,
    "dipinjam": 0
  }

  print("[V] buku berhasil ditemukan")

#2.LIHAT SEMUA BUKU
def lihat_buku():
  if not buku:
    print("Belum ada buku")
    return

  print("\n=== DAFTAR BUKU ===")
  for isbn, data in buku.items():
    print(f"""
ISBN   : {isbn}
Judul  : {data['judul']}
Penulis: {data['penulis']}
Tahun  : {data['tahun']}
Stok   : {data['stok']}
Dipinjam: {data['dipinjam']}
--------------------------""")

#3.CARI BUKU
def cari_buku():
  keyword = input("Cari (judul/penulis): ").lower()

  ditemukan = False
  for isbn, data in buku.items():
    if keyword in data['judul'].lower() or keyword in data['penulis'].lower():
            print(f"""
ISBN   : {isbn}
Judul  : {data['judul']}
Penulis: {data['penulis']}
Stok   : {data['stok']}""")
            ditemukan = True

  if not ditemukan:
    print("❌ Buku tidak ditemukan")

# 4. PINJAM BUKU
def pinjam_buku():
    isbn = input("Masukkan ISBN: ")

    if isbn not in buku:
        print("❌ Buku tidak ditemukan")
        return

    if buku[isbn]['stok'] > 0:
        buku[isbn]['stok'] -= 1
        buku[isbn]['dipinjam'] += 1
        print("✅ Buku berhasil dipinjam")
    else:
        print("❌ Stok habis")

# 5. KEMBALIKAN BUKU
def kembalikan_buku():
    isbn = input("Masukkan ISBN: ")

    if isbn not in buku:
        print("❌ Buku tidak ditemukan")
        return

    buku[isbn]['stok'] += 1
    print("✅ Buku dikembalikan")

# 6. BUKU POPULER
def buku_populer():
    if not buku:
        print("Belum ada data")
        return

    max_pinjam = max(b['dipinjam'] for b in buku.values())

    if max_pinjam == 0:
        print("Belum ada buku yang dipinjam")
        return

    print("\n🔥 Buku Terpopuler:")
    for isbn, data in buku.items():
        if data['dipinjam'] == max_pinjam:
            print(f"{data['judul']} ({data['dipinjam']} kali dipinjam)")


# =========================
# MENU
# =========================
def menu():
    while True:
        print("\n=== SISTEM PERPUSTAKAAN ===")
        print("1. Tambah buku")
        print("2. Lihat semua buku")
        print("3. Cari buku")
        print("4. Pinjam buku")
        print("5. Kembalikan buku")
        print("6. Buku populer")
        print("7. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            tambah_buku()
        elif pilih == "2":
            lihat_buku()
        elif pilih == "3":
            cari_buku()
        elif pilih == "4":
            pinjam_buku()
        elif pilih == "5":
            kembalikan_buku()
        elif pilih == "6":
            buku_populer()
        elif pilih == "7":
            print("Keluar...")
            break
        else:
            print("❌ Pilihan tidak valid")


# =========================
# RUN
# =========================
menu()

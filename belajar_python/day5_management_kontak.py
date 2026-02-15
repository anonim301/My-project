#========
# MANAJEMEN KONTAK
#========

kontak = [("Andi", "08123456789"), ("Budi", "082346789")]

def tampilkan_menu():
    print("\nMANAJEMEN KONTAK")
    print("#" * 15)
    print("1. Tambah kontak")
    print("2. Lihat semua kontak")
    print("3. Cari kontak")
    print("4. Hapus kontak")
    print("5. Urutkan kontak berdasarkan nama")
    print("6. Keluar")

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-6): ")

    # 1. Tambah kontak
    if pilihan == "1":
        name = input("Masukkan nama: ")
        number = input("Masukkan nomor telepon: ")
        kontak.append((name, number))
        print("Kontak berhasil ditambahkan!")

    # 2. Lihat semua kontak
    elif pilihan == "2":
        if not kontak:
            print("Kontak kosong")
        else:
            print("\nDaftar kontak:")
            for i, (name, number) in enumerate(kontak, start=1):
                print(f"{i}. {name} - {number}")

    # 3. Cari kontak
    elif pilihan == "3":
        cari = input("Masukkan nama yang dicari: ").lower()
        ditemukan = False

        for name, number in kontak:
            if cari in name.lower():
                print(f"Ditemukan: {name} - {number}")
                ditemukan = True

        if not ditemukan:
            print("Kontak tidak ditemukan")

    # 4. Hapus kontak
    elif pilihan == "4":
        nama_hapus = input("Masukkan nama kontak yang ingin dihapus: ").lower()
        kontak_baru = []
        terhapus = False

        for name, number in kontak:
            if name.lower() != nama_hapus:
                kontak_baru.append((name, number))
            else:
                terhapus = True

        kontak = kontak_baru

        if terhapus:
            print("Kontak berhasil dihapus")
        else:
            print("Kontak tidak ditemukan!")

    # 5. Urutkan kontak
    elif pilihan == "5":
        kontak.sort(key=lambda x: x[0].lower())
        print("Kontak berhasil diurutkan berdasarkan nama")

    # 6. Keluar
    elif pilihan == "6":
        print("Keluar dari program")
        break

    else:
        print("Pilihan tidak valid!")

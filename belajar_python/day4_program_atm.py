# SIMULASI ATM

saldo = 1000000  # saldo awal

while True:
    print("\n=== MENU ATM ===")
    print("1. Cek Saldo")
    print("2. Tarik Tunai")
    print("3. Setor Tunai")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        print(f"Saldo Anda: Rp {saldo:,}")

    elif pilihan == "2":
        try:
            tarik = int(input("Masukkan jumlah tarik: Rp "))
            if tarik <= 0:
                print("Jumlah harus lebih dari 0!")
            elif tarik > saldo:
                print("Saldo tidak cukup!")
            else:
                saldo -= tarik
                print(f"Transaksi berhasil! Saldo sekarang: Rp {saldo:,}")
        except ValueError:
            print("Harap masukkan angka yang valid!")

    elif pilihan == "3":
        try:
            setor = int(input("Masukkan jumlah setor: Rp "))
            if setor <= 0:
                print("Jumlah harus lebih dari 0!")
            else:
                saldo += setor
                print(f"Transaksi berhasil! Saldo sekarang: Rp {saldo:,}")
        except ValueError:
            print("Harap masukkan angka yang valid!")

    elif pilihan == "4":
        print("Terima kasih sudah menggunakan ATM!")
        break

    else:
        print("Pilihan tidak valid! Masukkan 1-4 saja.")

import os

#DATA AWAL
kandidat = ["Andi", "Budi", "Cici", "Dodi"]
votes = {"Andi": 0, "Bufi": 0, "Cici": 0, "Dodi": 0}

#CLEAR SCREEN(TERMUX)
def clear():
  os.system("clear")

#TAMPILKAN KANDIDAT
def tampilkan_kandidat():
  print("=== DAFTSR KANDIDAT ===")
  for i, k in enumerate(kandidat, 1):
    print(f"{i}. {k}")

#VOTING
def voting():
  tampilkan_kandidat()
  try:
    pilihan = int(input("Pilih nomer kandidat: "))
    if 1 <= pilihan <= len(kandidat):
      name = kandidat[pilihan - 1]
      votes[name] += 1
      prin(f"[√] Voted berhasil untik {name}")
    else:
      print("[X] Pilihan tidak vali")
  except:
    print("[X] Input harus angka")

#HASIL REAL TIME
def tampilkan_hasil():
  print("=== HASIL VOTES ===")
  total = sum(votes.values())

  for k, v in votes.items():
    if total > 0:
      person = (v / total) * 100
    else:
      person = 0
    print(f"{k}: {v} suara ({person:.2f}℅)")

  print(f"\nTotal vote: {total}")

#PEMENANG
def tentukan_pemenang():
  max_vote = max(votes.values())
  pemenang = [k for k, v in votes.items() if v == max_vote]

  if max_vote == 0:
    print("Belum ada vote")
  elif len(pemenang) > 1:
    print("Seri antara:",",".join(pemenang))
  else:
    print(f"[√] Pemenang: {pemenang[0]} dengan {max_vote} suara")

# RESET
def reset_voting():
    for k in votes:
        votes[k] = 0
    print("🔄 Voting berhasil di-reset")

# MENU UTAMA
def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Tampilkan kandidat")
        print("2. Vote")
        print("3. Lihat hasil")
        print("4. Pemenang")
        print("5. Reset")
        print("6. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            tampilkan_kandidat()
        elif pilih == "2":
            voting()
        elif pilih == "3":
            tampilkan_hasil()
        elif pilih == "4":
            tentukan_pemenang()
        elif pilih == "5":
            reset_voting()
        elif pilih == "6":
            print("Keluar program...")
            break
        else:
            print("❌ Menu tidak valid")


# =========================
# JALANKAN PROGRAM
# =========================
menu()


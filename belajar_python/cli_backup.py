import os
import zipfile
import shutil
from datetime import datetime

#FOLDER BACKUP
BACKUP_DIR = "backup"

#Pastikan folder backup ada dulu
os.makedirs(BACKUP_DIR, exist_ok=True)

#Helper nama file backup berdasarkan timestamp
def generate_backup_name(folder_path):
  folder_name = os.path.basename(os.path.abspath(folder_path))
  timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
  return f"{folder_name}_backup_{timestamp}.zip"

#Fitur 1 bakcup folder ke zip
def backup_folder():
  folder_path = input("Masukkan folder yang mau dibackup: ").strip()

  if not os.path.exists(folder_path):
    print("[X] Folder tidak ditemukan")
    return

  backup_name = generate_backup_name(folder_path)
  backup_path = os.path.join(BACKUP_DIR, backup_name)

  try:
    with zipfile.ZipFile(backup_path, "w", zipfile.ZIP_DEFLATED) as zipf:
      for root, dirs, files in os.walk(folder_path):
        for file in files:
          file_path = os.path.join(root, file)
          zipf.write(file_path, os.path.relpath(file_path, folder_path))
    print(f"[V] Backup succes! FILE: {backup_path}")
  except Exception as e:
    print(f"[X] Gagal backup: {e}")

#Fitur 2 restore dari zip
def restore_backup():
  backups = os.listdir(BACKUP_DIR)
  if not backups:
    print("[X] Belum ada backup!")
    return

  print("\nDaftar backup tersedia: ")
  for i, b in enumerate(backups, start=1):
    print(f"{i}.  {b}")

  pilihan = input("Pilih nomer backup untuk restore: ")
  if not pilihan.isdigit() or int(pilihan) < 1 or int(pilihan) > len(backups):
    print("[X] Pilihan tidak valid!")
    return

  backup_file = os.path.join(BACKUP_DIR, backups[int(pilihan) - 1])
  restore_path = input("Masukkan folder tujuan restore: ").strip()
  os.makedirs(restore_path, exist_ok=True)

  try:
    with zipfile.ZipFile(backup_file, 'r') as zipf:
      zipf.extractall(restore_path)
    print(f"[√] Restore berhasil difolder: {restore_path}")
  except Exception as e:
    print(f"[X] Gagal restore: {e}")

#Fitur 4 lihat semua backups
def list_backups():
  backups = os.listdir(BACKUP_DIR)
  if not backups:
    print("[X] Belum ada bakcup!")
    return

  print("\nDaftar semua backup: ")
  for b in backups:
    print(f"- {b}")

#Fitur 5 hapus backup lama
def delete_backup():
  list_backups()
  backups = os.listdir(BACKUP_DIR)
  if not backups:
    return

  pilihan = input("Masukkan nama file backup yang ingin dihapus: ").strip()
  backup_path = os.path.join(BACKUP_DIR, pilihan)

  if not os.path.exists(backup_path):
    print("[X] Backup tidak ditemukan")
    return

  os.remove(backup_path)
  print(f"[√] Backup '{pilihan}' berhasil dihapus!")

# Menu utama
def main():
    while True:
        print("\n=== BACKUP & RESTORE SYSTEM ===")
        print("1. Backup folder ke ZIP")
        print("2. Restore dari ZIP")
        print("3. Lihat semua backup")
        print("4. Hapus backup lama")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            backup_folder()
        elif pilihan == "2":
            restore_backup()
        elif pilihan == "3":
            list_backups()
        elif pilihan == "4":
            delete_backup()
        elif pilihan == "0":
            print("👋 Terima kasih telah menggunakan sistem backup!")
            break
        else:
            print("❌ Pilihan tidak valid!")

if __name__ == "__main__":
    main()


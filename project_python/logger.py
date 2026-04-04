import os
import time
import random
import csv
from datetime import datetime

FILE_NAME = "data_log.csv"
logging_active = False

#SIMULASI SENSOR
def read_sensor():
  suhu = round(random.uniform(20, 35), 2)
  kelembaban = round(random.uniform(40, 80), 2)
  return suhu, kelembaban

#SIMPAN DATA
def log_data():
  global logging_active
  logging_active = True

  print("[!] Logging dimulai...(CTRL+C untuk stop)\n")
  if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as f:
      writer = csv.writer(f)
      writer.writerow(["timestamp", "suhu", "kelembaban"])

  try:
    while logging_active:
      suhu, kelembaban = read_sensor()
      timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

      with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, suhu, kelembaban])

      print(f"{timestamp} | 🌡️ {suhu}°C | 💧 {kelembaban}%")
      time.sleep(1)

  except KeyboardInterrupt:
      print("\n[!] Logging dihentikan")

#LIHAT DATA
def view_data():
  if not os.path.exists(FILE_NAME):
    print("[X] Belum ada data")
    return

  with open(FILE_NAME, "r") as f:
    reader = csv.reader(f)
    for row in reader:
      print(" | ".join(row))

#ANALISIS
def analyze_data():
  if not os.path.exists(FILE_NAME):
    print("[X] Belum ada data")
    return

  suhu_list = []
  hum_list = []

  with open(FILE_NAME, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
      suhu_list.append(float(row["suhu"]))
      hum_list.append(float(row["kelembaban"]))

  if not suhu_list:
    print("❌ Data kosong")
    return

  print("\n=== ANALISIS ===")
  print(f"Suhu min: {min(suhu_list)}")
  print(f"Suhu max: {max(suhu_list)}")
  print(f"Suhu rata-rata: {sum(suhu_list)/len(suhu_list):.2f}")
  print(f"Kelembaban min: {min(hum_list)}")
  print(f"Kelembaban max: {max(hum_list)}")
  print(f"Kelembaban rata-rata: {sum(hum_list)/len(hum_list):.2f}")


# =========================
# MAIN
# =========================
def main():
    while True:
        print("\n=== DATA LOGGER ===")
        print("1. Mulai logging")
        print("2. Lihat data")
        print("3. Analisis data")
        print("0. Keluar")

        pilih = input("Pilih: ")

        if pilih == "1":
            log_data()
        elif pilih == "2":
            view_data()
        elif pilih == "3":
            analyze_data()
        elif pilih == "0":
            break
        else:
            print("❌ Salah input")


if __name__ == "__main__":
    main()

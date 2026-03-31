import json
import os
from datetime import datetime

DATA_FILE = "notes.json"


# =========================
# UTIL
# =========================
def load_notes():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}


def save_notes(notes):
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(notes, f, indent=4)
        return True
    except Exception as e:
        print("❌ Gagal simpan:", e)
        return False


def generate_id(notes):
    return str(max([int(i) for i in notes.keys()], default=0) + 1)


def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# =========================
# CREATE
# =========================
def create_note(notes):
    print("\n=== BUAT NOTE ===")

    judul = input("Judul: ").strip()
    if not judul:
        print("❌ Judul kosong")
        return

    print("Isi (END untuk selesai):")
    isi = []
    while True:
        line = input()
        if line == "END":
            break
        isi.append(line)

    if not isi:
        print("❌ Isi kosong")
        return

    nid = generate_id(notes)
    notes[nid] = {
        "judul": judul,
        "isi": "\n".join(isi),
        "created": now(),
        "updated": now()
    }

    save_notes(notes)
    print("✅ Note dibuat!")


# =========================
# READ ALL
# =========================
def list_notes(notes):
    if not notes:
        print("📭 Tidak ada note")
        return

    print("\n=== LIST NOTE ===")
    for nid, note in notes.items():
        print(f"[{nid}] {note['judul']}")


# =========================
# READ ONE
# =========================
def read_note(notes):
    list_notes(notes)
    nid = input("ID: ")

    if nid not in notes:
        print("❌ Tidak ditemukan")
        return

    n = notes[nid]
    print(f"\n=== {n['judul']} ===")
    print(n["isi"])


# =========================
# UPDATE
# =========================
def edit_note(notes):
    list_notes(notes)
    nid = input("ID edit: ")

    if nid not in notes:
        print("❌ Tidak ditemukan")
        return

    note = notes[nid]

    judul = input(f"Judul baru ({note['judul']}): ").strip()
    if judul:
        note["judul"] = judul

    print("Isi baru (END untuk selesai):")
    isi = []
    while True:
        line = input()
        if line == "END":
            break
        isi.append(line)

    if isi:
        note["isi"] = "\n".join(isi)

    note["updated"] = now()
    save_notes(notes)

    print("✅ Updated!")


# =========================
# DELETE
# =========================
def delete_note(notes):
    list_notes(notes)
    nid = input("ID hapus: ")

    if nid not in notes:
        print("❌ Tidak ditemukan")
        return

    del notes[nid]
    save_notes(notes)

    print("🗑️ Dihapus!")


# =========================
# SEARCH
# =========================
def search_notes(notes):
    keyword = input("Keyword: ").lower()

    for nid, note in notes.items():
        if keyword in note["judul"].lower() or keyword in note["isi"].lower():
            print(f"[{nid}] {note['judul']}")


# =========================
# EXPORT
# =========================
def export_notes(notes):
    filename = input("Nama file: ").strip() or "notes.txt"

    with open(filename, "w") as f:
        for nid, note in notes.items():
            f.write(f"[{nid}] {note['judul']}\n")
            f.write(note["isi"] + "\n")
            f.write("=" * 40 + "\n")

    print("✅ Export selesai!")


# =========================
# MAIN
# =========================
def main():
    notes = load_notes()

    while True:
        print("\n=== NOTES APP ===")
        print("1. Create")
        print("2. List")
        print("3. Read")
        print("4. Edit")
        print("5. Delete")
        print("6. Search")
        print("7. Export")
        print("0. Exit")

        pilih = input("Pilih: ")

        if pilih == "1":
            create_note(notes)
        elif pilih == "2":
            list_notes(notes)
        elif pilih == "3":
            read_note(notes)
        elif pilih == "4":
            edit_note(notes)
        elif pilih == "5":
            delete_note(notes)
        elif pilih == "6":
            search_notes(notes)
        elif pilih == "7":
            export_notes(notes)
        elif pilih == "0":
            break
        else:
            print("❌ Salah input")


if __name__ == "__main__":
    main()

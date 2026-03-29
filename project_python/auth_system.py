import datetime
import getpass


# =========================
# DATABASE
# =========================
users = {
    "admin": {
        "password": "admin123",
        "nama": "Administrator",
        "email": "admin@system.com",
        "tanggal_registrasi": "2024-01-01",
        "level": "admin"
    }
}


# =========================
# HELPER FUNCTIONS
# =========================
def hash_password(password):
    return password  # simulasi (real project pakai hashlib)


def validate_password(password):
    return len(password) >= 6


def validate_email(email):
    return "@" in email and "." in email


# =========================
# REGISTER
# =========================
def register():
    print("\n=== REGISTRASI ===")

    username = input("Username: ").strip()
    if username in users:
        print("❌ Username sudah digunakan!")
        return

    nama = input("Nama lengkap: ").strip()

    while True:
        email = input("Email: ").strip()
        if validate_email(email):
            break
        print("❌ Email tidak valid!")

    while True:
        password = getpass.getpass("Password: ")
        if validate_password(password):
            break
        print("❌ Password minimal 6 karakter!")

    konfirmasi = getpass.getpass("Konfirmasi password: ")
    if password != konfirmasi:
        print("❌ Password tidak cocok!")
        return

    users[username] = {
        "password": hash_password(password),
        "nama": nama,
        "email": email,
        "tanggal_registrasi": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "level": "user"
    }

    print("✅ Registrasi berhasil!")


# =========================
# LOGIN
# =========================
def login():
    print("\n=== LOGIN ===")

    username = input("Username: ").strip()
    password = getpass.getpass("Password: ")

    if username not in users:
        print("❌ Username tidak ditemukan!")
        return None

    if users[username]["password"] != hash_password(password):
        print("❌ Password salah!")
        return None

    print(f"✅ Selamat datang, {users[username]['nama']}!")
    return username


# =========================
# GANTI PASSWORD
# =========================
def ganti_password(username):
    print("\n=== GANTI PASSWORD ===")

    lama = getpass.getpass("Password lama: ")
    if users[username]["password"] != hash_password(lama):
        print("❌ Password salah!")
        return

    baru = getpass.getpass("Password baru: ")
    if not validate_password(baru):
        print("❌ Minimal 6 karakter!")
        return

    konfirmasi = getpass.getpass("Konfirmasi: ")
    if baru != konfirmasi:
        print("❌ Tidak cocok!")
        return

    users[username]["password"] = hash_password(baru)
    print("✅ Password berhasil diubah!")


# =========================
# LUPA PASSWORD
# =========================
def lupa_password():
    print("\n=== LUPA PASSWORD ===")

    username = input("Username: ").strip()
    if username not in users:
        print("❌ Username tidak ditemukan!")
        return

    email = input("Masukkan email: ").strip()
    if email != users[username]["email"]:
        print("❌ Email tidak cocok!")
        return

    print("✅ Verifikasi berhasil!")

    baru = getpass.getpass("Password baru: ")
    if not validate_password(baru):
        print("❌ Minimal 6 karakter!")
        return

    users[username]["password"] = hash_password(baru)
    print("✅ Password berhasil direset!")


# =========================
# ADMIN - LIHAT USER
# =========================
def lihat_semua_user(username):
    if users[username]["level"] != "admin":
        print("❌ Akses ditolak!")
        return

    print("\n=== DAFTAR USER ===")
    for u, data in users.items():
        print(f"""
Username : {u}
Nama     : {data['nama']}
Email    : {data['email']}
Level    : {data['level']}
------------------------""")


# =========================
# PROFIL
# =========================
def profil(username):
    data = users[username]

    print("\n=== PROFIL ===")
    print(f"Username : {username}")
    print(f"Nama     : {data['nama']}")
    print(f"Email    : {data['email']}")
    print(f"Level    : {data['level']}")
    print(f"Daftar   : {data['tanggal_registrasi']}")


# =========================
# MAIN LOOP
# =========================
current_user = None

while True:
    print("\n====================")

    if current_user:
        print(f"Halo, {users[current_user]['nama']}!")
        print("1. Profil")
        print("2. Ganti Password")
        print("3. Lihat Semua User")
        print("4. Logout")
        print("0. Keluar")

        pilihan = input("Pilih: ")

        if pilihan == "1":
            profil(current_user)
        elif pilihan == "2":
            ganti_password(current_user)
        elif pilihan == "3":
            lihat_semua_user(current_user)
        elif pilihan == "4":
            current_user = None
        elif pilihan == "0":
            break
        else:
            print("❌ Salah input!")

    else:
        print("1. Login")
        print("2. Register")
        print("3. Lupa Password")
        print("0. Keluar")

        pilihan = input("Pilih: ")

        if pilihan == "1":
            current_user = login()
        elif pilihan == "2":
            register()
        elif pilihan == "3":
            lupa_password()
        elif pilihan == "0":
            break
        else:
            print("❌ Salah input!")

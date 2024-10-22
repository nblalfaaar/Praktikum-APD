print(
"""
==========================================
---MANAJEMEN DAFTAR DRAMA KOREA NETFLIX---
==========================================
"""
)

admin_netflix = {
    "username" : "admin_netflix",
    "password" : "netflixdisini"
}
pengguna = {}
daftar_drakor = {}
total_drakor = 0

def registrasi_pengguna():
    global pengguna
    print("\nSilakan register pengguna baru!")
    username = input("Masukkan nama pengguna (nama depan/panggilan) : ").lower()
    password = input("Masukkan password Anda : ")

    pengguna[username] = {"password" : password}
    print("Berhasil registrasi pengguna baru!")

def validasi_angka(pesan):
    try:
        pilihan = int(input(pesan))
        return pilihan
    except ValueError:
        print("Input harus berupa angka!")
        return validasi_angka(pesan)
    
def login():
    print("\nSilakan login menggunakan username dan password!")
    username = input("Username : ").lower()
    password = input("Password : ")

    if username == admin_netflix["username"] and password == admin_netflix["password"]:
        print(f"Berhasil login sebagai admin! Selamat datang, {username}")
        return "admin"
    
    elif username in pengguna and pengguna[username]["password"] == password:
        print(f"Berhasil login sebagai pengguna! Selamat datang, {username}")
        return "pengguna"
    
    else:
        print("Gagal login! Tolong periksa kembali username dan password Anda!")
        return None
    
def tambah_drakor():
    global daftar_drakor, total_drakor
    judul = input("Judul : ")
    genre = input("Genre : ")
    tahun_rilis = input("Tahun Rilis : ")
    status = input("Status : ")
    daftar_drakor[judul] = {
        "genre" : genre,
        "tahun_rilis" : tahun_rilis,
        "status" : status
    }
    total_drakor += 1
    print("Drakor berhasil ditambahkan!")

def lihat_drakor():
    if not daftar_drakor:
        print("\nBelum ada drakor yang tersedia.")
    else:
        print(f"\nTotal Drakor : {total_drakor}")
        for i, (judul, detail) in enumerate(daftar_drakor.items(), 1):
            print(f"\nDaftar Drakor Ke-{i}")
            print(f"Judul : {judul}")
            print(f"Genre : {detail['genre']}")
            print(f"Tahun Rilis : {detail['tahun_rilis']}")
            print(f"Status : {detail['status']}")

def update_drakor(judul_lama):
    if judul_lama in daftar_drakor:
        judul_baru = input("Judul baru (kosongkan jika tidak ingin mengubah) : ") or judul_lama
        genre_baru = input("Genre baru (kosongkan jika tidak ingin mengubah) : ") or daftar_drakor[judul_lama]['genre']
        tahun_rilis_baru = input("Tahun rilis baru (kosongkan jika tidak ingin mengubah) : ") or daftar_drakor[judul_lama]['tahun_rilis']
        status_baru = input("Status baru (kosongkan jika tidak ingin mengubah) : ") or daftar_drakor[judul_lama]['status']

        daftar_drakor[judul_baru] = {
            "genre" : genre_baru,
            "tahun_rilis" : tahun_rilis_baru,
            "status" : status_baru
        }
        if judul_baru != judul_lama:
            del daftar_drakor[judul_lama]
        print("Drakor berhasil diupdate!")
        return daftar_drakor
    else:
        print("Judul drakor tidak ditemukan!")
        return None

def hapus_drakor(judul_hapus):
    global total_drakor
    if judul_hapus in daftar_drakor:
        konfirmasi = input("Apakah Anda yakin ingin menghapus drakor ini? (ya/tidak) : ").lower()
        if konfirmasi == "ya":
            del daftar_drakor[judul_hapus]
            total_drakor -= 1
            print("Drakor berhasil dihapus!")
            return True
        else:
            print("Penghapusan dibatalkan")
            return False
    else:
        print("Judul drakor tidak ditemukan!")
        return False

def menu_admin():
    while True:
        print(
        """
        =======================
           ---MENU ADMIN---
        1. TAMBAH DRAKOR
        2. LIHAT DAFTAR DRAKOR
        3. UPDATE DRAKOR
        4. HAPUS DRAKOR
        5. KELUAR
        =======================
        """
        )
        pilihan_admin = validasi_angka("Pilih menu (1/2/3/4/5) : ")

        if pilihan_admin == 1:
            tambah_drakor()

        elif pilihan_admin == 2:
            lihat_drakor()

        elif pilihan_admin == 3:
            lihat_drakor()
            judul_lama = input("Judul drakor yang ingin diupdate : ")
            update_drakor(judul_lama)

        elif pilihan_admin == 4:
            lihat_drakor()
            judul_hapus = input("Judul drakor yang ingin dihapus : ")
            hapus_drakor(judul_hapus)

        elif pilihan_admin == 5:
            print("Berhasil Logout!")
            break

        else:
            print("Pilihan tidak valid!")

def menu_pengguna():
    while True:
        print(
        """
        ======================
          ---MENU PENGGUNA---
        1. LIHAT DAFTAR DRAKOR
        2. KELUAR
        ======================
        """
        )

        pilihan_pengguna = validasi_angka("Pilih menu (1/2) : ")

        if pilihan_pengguna == 1:
            lihat_drakor()

        elif pilihan_pengguna == 2:
            print("Berhasil Logout!")
            break

        else:
            print("Pilihan tidak valid!")

while True:
    print(
    """
    ================================
    HALO! SELAMAT DATANG DI NETFLIX
    1. REGISTER
    2. LOGIN
    3. KELUAR
    ================================
    """
    )

    pilihan = validasi_angka("Pilih menu (1/2/3) : ")

    if pilihan == 1:
        registrasi_pengguna()

    elif pilihan == 2:
        peran = login()
        if peran == "admin":
            menu_admin()
        elif peran == "pengguna":
            menu_pengguna()

    elif pilihan == 3:
        print("Terima kasih telah menggunakan aplikasi ini!")
        break

    else:
        print("Pilihan tidak valid!")
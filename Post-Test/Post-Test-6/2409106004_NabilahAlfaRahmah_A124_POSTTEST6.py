print("Manajemen Daftar Drama Korea di Netflix")

daftar_pengguna = {
    "admin" : {"password" : "passwordadmin", "peran" : "admin"},
    "pengguna" : {"password" : "passwordpengguna", "peran" : "pengguna"}
}
daftar_drakor = {}

while True:
    print("\nHalo!Selamat datang di Netflix!")
    print("1. Register\n2. Login\n3. Keluar")

    try:
        pilih = int(input("Pilih menu (1/2/3) : "))
    except ValueError:
        print("Input harus berupa angka 1/2/3!")
        continue

    if pilih == 1:
        print("\nSilakan register terlebih dahulu!")
        username = input("Masukkan nama pengguna (nama depan/panggilan) : ").lower()
        password = input("Masukkan tiga digit NIM terakhir (tanpa angka 0) : ")
        peran = input("Siapa kamu? (admin/pengguna) : ").lower()

        if peran in ["admin", "pengguna"]:
            if username in daftar_pengguna:
                print("Username sudah terdaftar!")
            else:
                daftar_pengguna[username] = {"password" : password, "peran" : peran}
                print("Berhasil registrasi!")
        else:
            print("Peran tidak valid. Hanya bisa memilih 'admin' atau 'pengguna'.")

    elif pilih == 2:
        print("\nSilakan login menggunakan username dan password!")
        username = input("Username : ").lower()
        password = input("Password : ")

        if username in daftar_pengguna and daftar_pengguna[username]["password"] == password:
            print(f"Berhasil login! Selamat datang, {username}")

            if daftar_pengguna[username]["peran"] == "admin":
                while True:
                    print("\nMenu Admin")
                    print("1. Tambah Drakor\n2. Lihat Daftar Drakor\n3. Update Drakor\n4. Hapus Drakor\n5. Keluar")

                    try:
                        pilihan_admin = int(input("Pilih menu (1/2/3/4/5) : "))
                    except ValueError:
                        print("Input harus berupa angka 1/2/3/4/5!")
                        continue

                    if pilihan_admin == 1:
                        judul = input("Judul : ")
                        genre = input("Genre : ")
                        tahun_rilis = input("Tahun Rilis : ")
                        status = input("Status (sudah ditonton/belum ditonton) : ")
                        daftar_drakor[judul] = {
                            "genre" : genre,
                            "tahun_rilis" : tahun_rilis,
                            "status" : status
                        }
                        print("Drakor berhasil ditambahkan!")

                    elif pilihan_admin == 2:
                        if not daftar_drakor:
                            print("Belum ada drakor yang tersedia.")
                        else:
                            for i, (judul, detail) in enumerate(daftar_drakor.items(), 1):
                                print(f"\nDaftar Drakor Ke-{i}")
                                print(f"Judul : {judul}")
                                print(f"Genre : {detail['genre']}")
                                print(f"Tahun Rilis : {detail['tahun_rilis']}")
                                print(f"Status : {detail['status']}")

                    elif pilihan_admin == 3:
                        judul_lama = input("Judul lama : ")
                        if judul_lama in daftar_drakor:
                            judul_baru = input("Judul baru : ")
                            genre_baru = input("Genre baru : ")
                            tahun_rilis_baru = input("Tahun rilis baru : ")
                            status_baru = input("Status baru : ")
                            daftar_drakor[judul_baru] = {
                                "genre" : genre_baru,
                                "tahun_rilis" : tahun_rilis_baru,
                                "status" : status_baru
                            }
                            if judul_baru != judul_lama:
                                del daftar_drakor[judul_lama]
                            print("Drakor berhasil diupdate!")
                        else:
                            print("Judul drakor tidak ditemukan!")

                    elif pilihan_admin == 4:
                        judul_hapus = input("Judul yang ingin dihapus : ")
                        if judul_hapus in daftar_drakor:
                            del daftar_drakor[judul_hapus]
                            print("Drakor berhasil dihapus!")
                        else:
                            print("Judul drakor tidak ditemukan!")

                    elif pilihan_admin == 5:
                        print("Berhasil Logout!")
                        break

                    else:
                        print("Pilihan tidak valid!")

            elif daftar_pengguna[username]["peran"] == "pengguna":
                while True:
                    print("\nMenu Pengguna")
                    print("1. Lihat Daftar Drakor\n2. Keluar")

                    try:
                        pilihan_pengguna = int(input("Pilih menu (1/2) : "))
                    except ValueError:
                        print("Input harus berupa angka 1/2!")
                        continue
                    
                    if pilihan_pengguna == 1:
                        if not daftar_drakor:
                            print("Belum ada drakor yang tersedia.")
                        else:
                            for i, (judul, detail) in enumerate(daftar_drakor.items(), 1):
                                print(f"\nDaftar Drakor Ke-{i}")
                                print(f"Judul : {judul}")
                                print(f"Genre : {detail['genre']}")
                                print(f"Tahun Rilis : {detail['tahun_rilis']}")
                                print(f"Status : {detail['status']}")

                    elif pilihan_pengguna == 2:
                        print("Berhasil Logout!")
                        break

                    else:
                        print("Pilihan tidak valid!")

        else:
            print("Gagal login! Tolong periksa kembali username dan password Anda!")

    elif pilih == 3:
        print("Terima kasih telah menggunakan aplikasi ini!")
        break

    else:
        print("Pilihan tidak valid!")
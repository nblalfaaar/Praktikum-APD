print("Manajemen Daftar Drama Korea di Netflix")
daftar_pengguna = [["admin", "passwordadmin", "peranadmin"], ["pengguna", "passwordpengguna", "peranpengguna"]]
daftar_drakor = []

while True:
    print("\nHalo! Selamat datang di Netflix")
    print("1. Register\n2. Login\n3. Keluar")
    pilih = input("Pilih menu : ")

    if pilih == "1":
        print("\nSilakan register terlebih dahulu!")
        username = input("Masukkan nama pengguna (nama depan/panggilan) : ").lower()
        password = int(input("Masukkan tiga digit NIM terakhir (tanpa angka 0) : "))
        peran = input("Siapa kamu? (admin/pengguna) : ").lower()
        if peran in ["admin", "pengguna"]:
            daftar_pengguna.append([username, password, peran])
            print("Berhasil registrasi!")
        else:
            print("Peran tidak valid. Hanya bisa memilih 'admin' atau 'pengguna'.")
    
    elif pilih == "2":
        print("\nSilakan login menggunakan username dan password (jika sudah register)!")
        username = input("Username : ").lower()
        password = int(input("Password : "))
        ditemukan = False

        for pengguna in daftar_pengguna:
            if pengguna[0] == username and pengguna[1] == password:
                ditemukan = True
                print(f"Berhasil login! Selamat datang, {username}")
                if pengguna:
                    while True:
                        if pengguna[2] == "admin":
                            print("\nMenu Admin")
                            print("1. Tambah Drakor\n2. Lihat Daftar Drakor\n3. Update Drakor\n4. Hapus Drakor\n5. Keluar")
                            pilihan_admin = input("Pilih menu : ")
                            
                            if pilihan_admin == "1":
                                judul = input("Judul : ")
                                genre = input("Genre : ")
                                tahun_rilis = input("Tahun : ")
                                status = input("Status (sudah ditonton/belum ditonton) : ")
                                daftar_drakor.append([judul, genre, tahun_rilis, status])
                                print("Drakor berhasil ditambahkan")

                            elif pilihan_admin == "2":
                                if len(daftar_drakor) == 0:
                                    print("Belum ada drakor yang tersedia.")
                                else:
                                    for i, drakor in enumerate(daftar_drakor):
                                        print(f"\nDaftar Drakor ke-{i+1}\nJudul : {drakor[0]}\nGenre : {drakor[1]}\nTahun Rilis : {drakor[2]}\nStatus : {drakor[3]}")

                            elif pilihan_admin == "3":
                                judul_lama = input("Judul lama : ")
                                for i in range(len(daftar_drakor)):
                                    if daftar_drakor[i][0] == judul_lama:
                                        judul_baru = input("Judul : ")
                                        genre_baru = input("Genre : ")
                                        tahun_rilis_baru = input("Tahun rilis : ")
                                        status_baru = input("Status (sudah ditonton/belum ditonton) : ")
                                        daftar_drakor[i][0] = judul_baru
                                        daftar_drakor[i][1] = genre_baru
                                        daftar_drakor[i][2] = tahun_rilis_baru
                                        daftar_drakor[i][3] = status_baru
                                        print("Drakor berhasil diupdate!")

                            elif pilihan_admin == "4":
                                judul_lama = input("Judul yang ingin dihapus : ")
                                for i in range(len(daftar_drakor)):
                                    if daftar_drakor[i][0] == judul_lama:
                                        del daftar_drakor[i]
                                        print("Drakor berhasil dihapus!")
                                        break
                                else:
                                    print("Judul drakor tidak ditemukan!")

                            elif pilihan_admin == "5":
                                print("Berhasil Logout!")
                                break

                            else:
                                print("Anda Salah Input")
                        
                        elif pengguna[2] == "pengguna":
                            print("\nMenu Pengguna")
                            print("1. Lihat Daftar Drakor\n2. Keluar")
                            pilihan_pengguna = input("Pilih menu : ")
                            if pilihan_pengguna == "1":
                                if len(daftar_drakor) == 0:
                                    print("Belum ada drakor yang tersedia.")
                                else:
                                    for i, drakor in enumerate(daftar_drakor):
                                        print(f"\nDaftar Drakor ke-{i+1}\nJudul : {drakor[0]}\nGenre : {drakor[1]}\nTahun Rilis : {drakor[2]}\nStatus : {drakor[3]}")

                            elif pilihan_pengguna == "2":
                                print("Berhasil Logout!")
                                break

                            else:
                                print("Pilihan tidak valid!")

            if ditemukan:
                break             
        else:
            print("Gagal login! Tolong periksa kembali username dan password Anda!")
    
    elif pilih == "3":
        print("Terima kasih telah menggunakan aplikasi ini!")
        break
    else:
        print("Pilihan tidak valid.")
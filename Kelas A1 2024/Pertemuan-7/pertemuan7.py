# def salam():
#     print("selamat datang mahasiswa baru 2024")

# salam()

# def salam():
#     print(iso)
# iso = "salam iso"
# salam()

# def salam(salam):
#     print(salam)
# iso = "salam iso"
# salam()

# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas

# print(luas_persegi(3))


# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas
# luas = luas_persegi(2)
# print(luas)

# Nama = "Informatika"
# Mata_Kuliah = "Algoritma dan Pemrograman Dasar"
# # membuat variabel lokal
# def info():
#     Nama = "Teknik Elektro"
#     Mata_Kuliah = "Pengantar Teknik ELektro"
#     print("Prodi:", Nama)
#     print("Mata Kuliah:", Mata_Kuliah)
# # mengakses variabel global
# print("Prodi:", Nama)
# print("Mata Kuliah:", Mata_Kuliah)
# # memanggil fungsi info
# info()

# # fungsi untuk menampilkan semua data
# buku =[]
# def show_data():
#     if len(buku) <= 0:
#         print ("Belum Ada data")
#     else:
#         print("ID", "Nama Buku")
#         for indeks in range(len(buku)):
#             print (indeks, buku[indeks])

# # fungsi untuk menambah data
# def insert_data():
#     buku_baru = input("Judul Buku : ")
#     buku.append(buku_baru)

# # fungsi untuk edit data
# def edit_data():
#     show_data()
#     indeks = int(input("Inputkan ID buku: "))
#     if(indeks >= len(buku) or indeks < 0):
#         print ("ID salah")
#     else:
#         judul_baru = input("Judul baru: ")
#         buku[indeks] = judul_baru

# # fungsi untuk menghapus data
# def delete_data():
#     show_data()
#     indeks = int(input("Inputkan ID buku: "))
#     if(indeks >= len(buku) or indeks < 0):
#         print ("ID salah")
#     else:
#         buku.remove(buku[indeks])

# # fungsi untuk menampilkan menu
# def show_menu():
#     print ("\n")
#     print ("----------- MENU---------- ")
#     print ("[1] Show Data")
#     print ("[2] Insert Data")
#     print ("[3] Edit Data")
#     print ("[4] Delete Data")
#     print ("[5] Exit")
#     menu = input("PILIH MENU> ")
#     print ("\n")
#     if menu == "1":
#         show_data()
#     elif menu == "2":
#         insert_data()
#     elif menu == "3":
#         edit_data()
#     elif menu == "4":
#         delete_data()
#     elif menu == "5":
#         exit()
#     else:
#         print ("Salah pilih!")

# if __name__ == "__main__":
#     while(True):
#         show_menu()


# def luas_segitiga():
#     alas = float(input("masukkan alas : "))
#     tinggi = float(input("masukkan tinggi : "))
#     luas = 0.5 * alas * tinggi
#     return luas

# print(luas_segitiga())

# def luas_persegi_panjang():
#     panjang = float(input("masukkan panjang : "))
#     lebar = float(input("masukkan lebar : "))
#     luas = panjang * lebar
#     return luas

# print(luas_persegi_panjang())
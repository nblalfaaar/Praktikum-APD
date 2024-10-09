# daftar_buku = {
#     "buku1" : "harry potter",
#     "buku2" : "percy jackson",
#     "buku3" : "twilligt"
# }
# print(daftar_buku["buku1"])

# daftar_buku = {
#     "buku1" : "harry potter",
#     "buku2" : "percy jackson",
#     "buku3" : "twilligt"
# }
# print(daftar_buku)

# daftar_buku = {
#     "buku1" : "harry potter",
#     "buku1" : "percy jackson", 
#     "buku3" : "twilligt"
# }
# print(daftar_buku)

# Biodata = {
#     "Nama" : "Aldy Ramadhan Syahputra",
#     "NIM" : 2109106079,
#     "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" :True,
#     "Social Media" : {
#         "Instagram" : "@aldyrmdhns_",
#         "Discord" : "\'Izanami#6848"
#         }
# }

# games = dict(Sekiro = "Action", Pokemon = "Adventure", Valorant = "FPS")
# print(games)


# Biodata = {
#     "Nama" : "Aldy Ramadhan Syahputra",
#     "NIM" : 2109106079,
#     "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" :True,
#     "Social Media" : {
#         "Instagram" : "@aldyrmdhns_",
#         "Discord" : "\'Izanami#6848"
#         }
# }
# print(Biodata["KRS"][1])
# print(Biodata.get("Nama"))

# print(Biodata['alamat'])
# print(Biodata.get('alamat'))

# print(Biodata.get["alamat"])

# Biodata = {
#     "Nama" : "Aldy Ramadhan Syahputra",
#     "NIM" : 2109106079,
#     "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" :True,
#     "Social Media" : {
#         "Instagram" : "@aldyrmdhns_",
#         "Discord" : "\'Izanami#6848"
#         }
# }
# for i, j in Biodata.items():
#     print(f"Key = {i} dan Value = {j}")

# for i in Biodata:
#     print(Biodata[i])

# Film = {
#     "Avenger Endgame" : "Action",
#     "Sherlock Holmes" : "Mystery",
#     "The Conjuring" : "Horror"
# }
# print(Film)

# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller"})
# print(Film)

# Film = {
#     "Avenger Endgame" : "Action",
#     "Sherlock Holmes" : "Mystery",
#     "The Conjuring" : "Horror"
# }
# print(Film)
# del Film("The Conjuring")
# print(Film)
# print(Film.get("The Conjuring"))

# print(Film)
# Film.clear()
# print(Film)

# Biodata = {
#     "Nama" : "Aldy Ramadhan Syahputra",
#     "NIM" : 2109106079,
#     "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" :True,
#     "Social Media" : {
#         "Instagram" : "@aldyrmdhns_",
#         "Discord" : "\'Izanami#6848"
#         }
# }

# print("jumlah data dalam dict Biodata = ", len(Biodata))
# pinjamdict = Biodata.copy()
# print(pinjamdict)

# key = "apel", "jeruk", "mangga"
# value = 1
# buah = dict.fromkeys(key, value)
# print(buah)

# Film = {
#     "Avenger Endgame" : "Action",
#     "Sherlock Holmes" : "Mystery",
#     "The Conjuring" : "Horror"
# }
# for i in Film.keys():
#     print(i)

# for i in Film.values():
#     print(i)

# Film = {
#     "Avenger Endgame" : "Action",
#     "Sherlock Holmes" : "Mystery",
#     "The Conjuring" : "Horror"
# }
# print("Film : ", Film.setdefault('Oldbook', 'Horror'))
# print(Film)

# Musik = {
#     "The Chainsmoker" : ["All we Know", "The Paris"], 
#     "Alan Walker" : ["Alone", "Lily"], 
#     "Neffex" : ["Best of Me", "Memories"]
# }
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for lagu in j:
#         print(lagu)
#     print("")

# mahasiswa = {
#     101 : {"Nama" : "Aldy", "Umur" : 19},
#     111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# print(f"sebelum : {mahasiswa}")
# mahasiswa[101]["Angkatan"] = 2023
# print(f"sesudah : {mahasiswa}")

# print(f"sebelum : {mahasiswa}")
# del mahasiswa[111]["Umur"]
# print(f"sesudah : {mahasiswa}")

# for i, j in mahasiswa.items():
#     print("ID Mahasiswa : ", i)
#     for i_a, j_a in j.items():
#         print (i_a, " : ", j_a)
#     print("")

# biodata = {
#     "Nama" : "Nabilah",
#     "Umur" : "18",
#     "NIM" : "2409106004",
#     "Jurusan" : "Informatika",
#     "Angkatan" : "2024"
# }
# print(biodata.get("NIM"))
# biodata.update({"Umur" : "20"})
# print(biodata)

Biodata = {}

while True:
    print("1. Tambah")
    print("2. Tampilakan")
    print("3. Exit")
    pilihan =  int(input("(1/2/3) : "))

    if pilihan == 1:
        nama = input("Masukkan nama :")
        umur = input("Masukkan umur :")
        alamat = input("Masukkan alamat :")

        Biodata[nama] = { 
            'Umur' : umur,
            'Alamat' : alamat
        }

    elif pilihan == 2:
        for nama, info in Biodata.items():
            print(f"Nama : {nama}")
            print(f"Umur : {info['Umur']}")
            print(f"Alamat : {info['Alamat']}")

    elif pilihan == 3:
        print("exit ...")
        break

    else:
        print("Invalid ... ... ")
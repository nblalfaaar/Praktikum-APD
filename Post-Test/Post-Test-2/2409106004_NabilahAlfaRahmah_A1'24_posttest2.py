Nama_Lengkap = input("Nama lengkap : ")
Nama_Panggilan = input("Nama panggilan : ")
Prodi = input("Prodi : ")
Fakultas = input("Fakultas : ")
Universitas = input("Universitas : ")
NIM = int(input("NIM : "))
Berat_Badan = float(input("Berat badan (dalam kg) : "))

Tiga_Angka_Terakhir_NIM = NIM % 1000
print(f"Tiga angka terakhir NIM : {Tiga_Angka_Terakhir_NIM}")
Modulus = Tiga_Angka_Terakhir_NIM % 6

print(f'''\nHalo semuanya, perkenalkan nama saya {Nama_Lengkap} biasa dipanggil {Nama_Panggilan} 
dengan NIM {NIM}. Saya berasal dari Prodi {Prodi} Fakultas {Fakultas} Universitas {Universitas}. 
Berat badan saya {Berat_Badan} kg.''')

print(f"Tiga Angka Terakhir NIM saya yang Dimoduluskan dengan 6 adalah {Modulus}")
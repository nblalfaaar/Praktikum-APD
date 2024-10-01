print("Belum punya akun? Silakan buat akun!")
Nama = input("Masukkan nama depan/panggilan sebagai username : ")
NIM_Terakhir = int(input("Masukkan 3 digit NIM terakhir tanpa 0 di depan angka sebagai password Anda : "))
print(f"\nUsername = {Nama}")
print(f"Password = {NIM_Terakhir}")

i = 0
while i < 3:
    print("\nSilakan Login")
    username = input("Username : ")
    password = int(input("Password : "))
    
    if username == Nama and password == NIM_Terakhir:
        print("Berhasil Login")
    
        while True:
            print("\nKalkulator Kebutuhan Kalori Harian (TDEE)")
            Berat_Badan = float(input("Berat badan (gr) : ")) / 1000
            Tinggi_Badan = float(input("Tinggi badan (km) : ")) * 100000
            Umur = float(input("Umur (tahun) = "))
            
            print("\nPilih Jenis Kelamin")
            print("1. Pria")
            print("2. Wanita")
            Jenis_Kelamin = int(input("Masukkan pilihan (1/2) : "))
            
            if Jenis_Kelamin == 1:
                print("#Menghitung BMR Pria")
                BMR = (10 * Berat_Badan) + (6.25 * Tinggi_Badan) - (5 * Umur) + 5
                print(f"BMR Pria = {BMR}")
            elif Jenis_Kelamin == 2:
                print("\n#Menghitung BMR Wanita")
                BMR = (10 * Berat_Badan) + (6.25 * Tinggi_Badan) - (5 * Umur) - 161
                print(f"BMR Wanita = {BMR}")
            else:
                print("Pilihan tidak valid")
                break

            print("\nLevel Aktivitas Harian")
            print("1. Aktivitas Harian (jarang bergerak)")
            print("2. Aktivitas Sedang (olahraga 1-3 kali seminggu)")
            print("3. Aktivitas Tinggi (olahraga 4-7 kali seminggu)")
            
            Aktivitas_Harian = int(input("Masukkan pilihan (1/2/3) : "))
            
            if Aktivitas_Harian == 1:
                Level_Aktivitas_Harian = 1.25
                TDEE = BMR * Level_Aktivitas_Harian
                print(f"TDEE = {TDEE}")
            elif Aktivitas_Harian == 2:
                Level_Aktivitas_Harian = 1.36
                TDEE = BMR * Level_Aktivitas_Harian
                print(f"TDEE = {TDEE}")
            elif Aktivitas_Harian == 3:
                Level_Aktivitas_Harian = 1.72
                TDEE = BMR * Level_Aktivitas_Harian
                print(f"TDEE = {TDEE}")
            else:
                print("Pilihan tidak valid")
                break
            
            Ulang = input("Apakah Anda masih ingin menghitung? (ya atau tidak) : ")
            if Ulang != "ya":
                break
        break
    else:
        i += 1
        print("Gagal Login! Silakan Coba lagi!")

if i == 3:
    print("Terjadi kesalahan, program berhenti!")
print("Kalkulator Kebutuhan Kalori Harian (TDEE)")

Berat_Badan = float(input("Berat badan (gr) : ")) / 1000
Tinggi_Badan = float(input("Tinggi badan (km) : ")) * 100000
Umur = int(input("Umur (tahun) : "))

print("Pilih Jenis Kelamin")
print("1. Pria")
print("2. Wanita")
Jenis_Kelamin = int(input("Masukkan pilihan (1/2) : "))

if Jenis_Kelamin == 1:
    print("\n#Menghitung BMR Pria")
    BMR = (10 * Berat_Badan) + (6.25 * Tinggi_Badan) - (5 * Umur) + 5
    print(f"BMR Pria = {BMR}")
elif Jenis_Kelamin == 2:
    print("\n#Menghitung BMR Wanita")
    BMR = (10 * Berat_Badan) + (6.25 * Tinggi_Badan) - (5 * Umur) - 161
    print(f"BMR Wanita = {BMR}")
else:
    print("Pilihan tidak valid")
    BMR = None

if BMR is not None:
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
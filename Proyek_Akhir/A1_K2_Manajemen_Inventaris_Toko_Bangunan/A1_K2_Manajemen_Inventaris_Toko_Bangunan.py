import csv        # Untuk membaca dan menulis file dalam bentuk csv
import datetime   # Untuk menambahkan cap waktu di riwayat aktivitas
import os         # untuk menjalankan perintah sistem operasi seperti clear dan cls
import platform   #  untuk mendapatkan informasi tentang platform yang sedang digunakan.
from prettytable import PrettyTable # Untuk membuat tabel pada tampilan

# Data awal inventaris toko bangunan dalam dictionary
inventory = {
        "Semen 40kg": {"stok": 150, "harga": 52000, "added_by": "admin"},
        "Pasir 1 Karung": {"stok": 300, "harga": 35000, "added_by": "admin"},
        "Batu Bata Merah 1000": {"stok": 100, "harga": 550000, "added_by": "admin"},
        "Cat Tembok 5kg": {"stok": 75, "harga": 125000, "added_by": "admin"},
        "Besi Beton 12mm 12m": {"stok": 50, "harga": 120000, "added_by": "admin"},
        "Paku 3 Inch (1kg)": {"stok": 200, "harga": 18000, "added_by": "admin"},
        "Kayu Balok 4x6 4m": {"stok": 80, "harga": 65000, "added_by": "admin"},
        "Triplek 9mm 122x244c": {"stok": 120, "harga": 95000, "added_by": "admin"},
        "Genteng Tanah Liat": {"stok": 500, "harga": 5000, "added_by": "admin"}

    }

inventory_user = {}    # Inventaris khusus untuk user

# Variabel users dengan satu akun admin bawaan
users = [
    {"username": "admin", "password": "admin123", "role": "admin"}
]

riwayat_aktivitas = []  # Menyimpan riwayat aktivitas

# Prosedur untuk menyimpan inventaris ke file CSV
def simpan_inventory(filename, inventory):
    try:
        with open(filename, "w", newline='', encoding='utf-8') as file:
            fieldnames = ["item", "stok", "harga", "added_by"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            
            # Menulis setiap barang ke file
            for item, data in inventory.items():
                row = {"item" : item, "stok" : data['stok'], "harga" : data["harga"], "added_by" : data["added_by"]}
                writer.writerow(row)
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan inventaris: {e}")

# Fungsi untuk memuat inventaris dari file CSV
def muat_inventory(filename):
    inventory = {}
    try:
        with open(filename, "r", encoding='utf-8') as filename:
            csvdata = csv.DictReader(filename)
            for row in csvdata:
                try:
                    inventory[row["item"]] = {
                        "stok" : int(row["stok"]),
                        "harga" : int(row["harga"]),
                        "added_by" : row["added_by"]
                        }
                except (ValueError, KeyError) as e:
                    print(f"Kesalahan membaca baris: {row} - {e}")
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan. Membuat data inventaris baru.")
    except Exception as e:
        print(f"Kesalahan umum saat memuat inventaris: {e}")
    return inventory

# Prosedur untuk menyimpan inventaris user ke file CSV
def simpan_inventory_user(filename, inventory_user):
    try:
        with open(filename, "w", newline='', encoding='utf-8') as file:
            fieldnames = ["item", "stok", "harga", "added_by"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            
            # Menulis setiap barang user ke file
            for item, data in inventory_user.items():
                row = {"item" : item, "stok" : data["stok"], "harga" : data["harga"], "added_by" : data["added_by"]}
                writer.writerow(row)
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan inventaris user: {e}")

# Fungsi untuk memuat inventaris user dari file CSV
def muat_inventory_user(filename):
    inventory_user = {}
    try:
        with open(filename, "r", encoding='utf-8') as filename:
            csvdata = csv.DictReader(filename)
            for row in csvdata:
                try:
                    inventory_user[row["item"]] = {
                        "stok" : int(row["stok"]),
                        "harga" : int(row["harga"]),
                        "added_by" : row["added_by"]
                        }
                except (ValueError, KeyError) as e:
                    print(f"Kesalahan membaca baris: {row} - {e}")
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan. Membuat data inventaris baru.")
    except Exception as e:
        print(f"Kesalahan umum saat memuat inventaris user: {e}")
    return inventory_user

# Prosedur untuk menyimpan data user ke file CSV
def simpan_users(filename, users):
    try:
        with open(filename, "w", newline='', encoding='utf-8') as file:
            fieldnames = ["username", "password", "role"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()       
            
            # Menulis setiap user ke file
            for user in users:
                writer.writerow(user)
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan data pengguna: {e}")

# Fungsi untuk memuat data user dari file CSV
def muat_users(filename):
    users = []
    try:
        with open(filename, "r", encoding='utf-8') as filename:
            csvdata = csv.DictReader(filename)
            for row in csvdata:
                try:
                    users.append({
                        "username" : row["username"],
                        "password" : row["password"],
                        "role" : row["role"]
                        })
                except KeyError as e:
                    print(f"Kesalahan membaca data pengguna:{e}")
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan. Membuat data pengguna baru.")
    except Exception as e:
        print(f"Kesalahan umum saat memuat data pengguna:{e}")
    return users

# Prosedur untuk menyimpan riwayat aktivitas ke file CSV
def simpan_riwayat_aktivitas(filename, riwayat_aktivitas):
    try:
        with open(filename, "w", newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["waktu", "aktivitas"])
            
            # Menulis setiap riwayat aktivitas ke file
            for aktivitas in riwayat_aktivitas:
                writer.writerow(aktivitas)
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan riwayat aktivitas:{e}")

# Fungsi untuk memuat riwayat aktivitas dari file CSV
def muat_riwayat_aktivitas(filename):
    riwayat_aktivitas = []
    try:
        with open(filename, "r", encoding='utf-8') as filename:
            csvdata = csv.reader(filename)
            next(csvdata)    # Lewati header
            for row in csvdata:
                riwayat_aktivitas.append(row)
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan. Membuat riwayat aktivitas baru.")
    except Exception as e:
        print(f"Kesalahan umum saat memuat riwayat aktivitas: {e}")
    return riwayat_aktivitas

# Memuat data awal dari file CSV
inventory = muat_inventory("inventory.csv")
inventory_user = muat_inventory_user("inventory_user.csv")
users = muat_users("users.csv")
riwayat_aktivitas = muat_riwayat_aktivitas("riwayat_aktivitas.csv")

# Prosedur untuk menyimpan semua data ke file CSV
def simpan_data():
    simpan_inventory("inventory.csv", inventory)
    simpan_inventory_user("inventory_user.csv", inventory_user)
    simpan_users("users.csv", users)
    simpan_riwayat_aktivitas("riwayat_aktivitas.csv", riwayat_aktivitas)

# Prosedur untuk menclear terminal
def clear_terminal():
    if platform.system() == "Windows":
        os.system("cls") # Perintah untuk Windows
    else:
        os.system("clear") # Perintah untuk Linux dan macOS

# Prosedur untuk menambahkan cap waktu pada aktivitas
def tambah_riwayat(aktivitas):
    try:
        waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        riwayat_aktivitas.append([waktu, aktivitas])
        simpan_riwayat_aktivitas("riwayat_aktivitas.csv", riwayat_aktivitas)
    except Exception as e:
        print(f"Terjadi kesalahan saat menambahkan riwayat aktivitas: {e}")


print("""
▒█▀▀▀█ ▒█▀▀▀ ▒█░░░ ░█▀▀█ ▒█▀▄▀█ ░█▀▀█ ▀▀█▀▀   ▒█▀▀▄ ░█▀▀█ ▀▀█▀▀ ░█▀▀█ ▒█▄░▒█ ▒█▀▀█ 
░▀▀▀▄▄ ▒█▀▀▀ ▒█░░░ ▒█▄▄█ ▒█▒█▒█ ▒█▄▄█ ░▒█░░   ▒█░▒█ ▒█▄▄█ ░▒█░░ ▒█▄▄█ ▒█▒█▒█ ▒█░▄▄ 
▒█▄▄▄█ ▒█▄▄▄ ▒█▄▄█ ▒█░▒█ ▒█░░▒█ ▒█░▒█ ░▒█░░   ▒█▄▄▀ ▒█░▒█ ░▒█░░ ▒█░▒█ ▒█░░▀█ ▒█▄▄█
      
▀█▀ █▀█ █▄▀ █▀█   █▄▄ ▄▀█ █▄░█ █▀▀ █░█ █▄░█ ▄▀█ █▄░█   ░░█ ▄▀█ █▄█ ▄▀█   █▀ █▀▀ █░░ ▄▀█ █░░ █░█
░█░ █▄█ █░█ █▄█   █▄█ █▀█ █░▀█ █▄█ █▄█ █░▀█ █▀█ █░▀█   █▄█ █▀█ ░█░ █▀█   ▄█ ██▄ █▄▄ █▀█ █▄▄ █▄█
""")

# Fungsi untuk login untuk admin dan user
def login(users):
    try:
        print("=== Login ===")
        username = input("Username: ")
        password = input("Password: ")
        
        user_found = None
        for user in users:
            if user['username'] == username and user['password'] == password:
                user_found = user
                break
            
        if user_found:
            print(f"Selamat datang, {username}!")
            return user_found  # Mengembalikan objek user yang ditemukan
        else:
            print("Username atau password salah. Silakan coba lagi.")
            return None  # Jika user tidak ditemukan
    except Exception as e:
        print(f"Terjadi kesalahan saat login: {e}")
        return None

# Prosedur untuk registrasi akun user baru
def registrasi_pengguna(users):
    try:
        print("=== Register Akun User Baru ===")
        while True:
            # Input username dengan validasi
            username = input("Masukkan username (5-20 karakter): ").strip()

            if not username:
                print("Error: Username tidak boleh kosong.Silakan coba lagi.")
                continue

            if len(username) < 5 or len(username) > 20:
                print("Error: Username harus memiliki panjang 5-20 karakter.")
                continue

            # Cek apakah username sudah ada
            user_exists = any(user['username'] == username for user in users)
            if user_exists:
                print("Username sudah ada. Silakan coba dengan username lain.")
                continue

            break # Username valid dan unik
        
        while True:
            # Input password dengan validasi
            password = input("Masukkan password (8-20 karakter): ").strip()
            
            if not password:
                print("Error: Password tidak boleh kosong. Silakan coba lagi.")
                continue

            if len(password) < 8 or len(password) > 20:
                print("Error: Password harus memiliki panjang 8-20 karakter.")
                continue

            break # Password valid
        
        role = "user"  # Semua registrasi pengguna biasa sebagai "user"
        users.append({"username": username, "password": password, "role": role})
        print(f"Pengguna {username} berhasil didaftarkan dengan role {role}!")
        
        simpan_data()   # Simpan data setelah registrasi

    except Exception as e:
        print(f"Terjadi kesalahan saat registrasi pengguna: {e}")

# Fungsi khusus untuk admin menambah akun admin lain
def tambah_admin(users, current_user):
    try:
        if current_user['role'] != "admin":
            print("Hanya admin yang bisa menambahkan admin baru.")
            return
        
        print("=== Tambah Admin Baru ===")

        # Validasi username
        while True:
            username = input("Masukkan username admin baru (5-20 karakter): ").strip()

            if not username:
                print("Error: Username tidak boleh kosong. Silakan coba lagi")
                continue

            if len(username) < 5 or len(username) > 20:
                print("Error: Username harus memiliki panjang 5-20 karakter.")
                continue

            # Cek apakah username sudah ada
            user_exists = any(user['username'] == username for user in users)
            if user_exists:
                print("Username sudah ada. Silakan coba dengan username lain.")
                continue
        
            break # Username valid dan unik

        # Validasi password
        while True:
            password = input("Masukkan password admin baru(8-20 karakter): ").strip()

            if not password:
                print("Error: Password tidak boleh kosong. Silakan coba lagi.")
                continue

            if len(password) < 8 or len(password) > 20:
                print("Error: Password harus memiliki panjang 8-20 karakter.")
                continue

            break # Password valid
        
        # Menambahkan admin baru
        users.append({"username": username, "password": password, "role": "admin"})
        tambah_riwayat(f"Admin baru '{username}' ditambahkan oleh '{current_user['username']}'.")
        print(f"Admin {username} berhasil didaftarkan!")

        simpan_data()    # Simpan perubahan

    except Exception as e:
        print(f"Terjadi kesalahan saat menambahkan admin: {e}")

# Fungsi untuk menampilkan inventaris
def tampilkan_inventaris(inventory):
    try:
        if not inventory:
            print("\n=== Inventaris Kosong ===")
            return  # Tidak perlu lanjut jika inventaris kosong
        
        table = PrettyTable()
        table.field_names = ["Nama Barang", "Stok", "Harga (Rp)"]
        for nama_barang, detail in inventory.items():
            try:
                table.add_row([
                    nama_barang,
                    detail['stok'],
                    f"{detail['harga']:,}"
                ])
            except KeyError as ke:
                print(f"Data barang '{nama_barang}' tidak lengkap: {ke}")
                continue
        
        print("\n=== Daftar Inventaris Toko Bangunan ===")
        print(table)
    except Exception as e:
        print(f"Terjadi kesalahan saat menampilkan inventaris: {e}")

# Fungsi untuk menampilkan inventaris user
def tampilkan_inventaris_user(inventory):
    try:
        if not inventory:
            print("\n=== Inventaris User Kosong ===")
            return  # Tidak perlu lanjut jika inventaris kosong
        
        table = PrettyTable() # Untuk menggunakan pretty table
        table.field_names = ["Nama Barang", "Stok", "Harga (Rp)"]
        for nama_barang, detail in inventory.items():
            try:
                table.add_row([
                    nama_barang,
                    detail['stok'],
                    f"{detail['harga']:,}"
                ])
            except KeyError as ke:
                print(f"Data barang '{nama_barang}' tidak lengkap: {ke}")
                continue
        
        print("\n=== Daftar Inventaris Toko Bangunan (khusus user) ===")
        print(table)
    except Exception as e:
        print(f"Terjadi kesalahan saat menampilkan inventaris user: {e}")

# Fungsi untuk menangani pilihan user dalam menu
def menu_user(inventory_user, inventory, current_user):
    while True:
        try:
            clear_terminal()
            print("""
                      

█▀▄▀█ █▀▀ █▄░█ █░█   █▀█ █▀▀ █▄░█ █▀▀ █▀▀ █░█ █▄░█ ▄▀█
█░▀░█ ██▄ █░▀█ █▄█   █▀▀ ██▄ █░▀█ █▄█ █▄█ █▄█ █░▀█ █▀█
─────────────────────── ⋆⋅☆⋅⋆ ───────────────────────── 
                1. Lihat Inventaris  
                2. Tambah Barang  
                3. Update Barang
                4. Hapus Barang
                5. Logout                       
""")
            pilihan_user = input("Pilih menu: ").strip()
            if pilihan_user == "1":
                clear_terminal()
                tampilkan_inventaris_user(inventory_user)
                tampilkan_inventaris(inventory)
                input("\nTekan Enter...")
            
            elif pilihan_user == "2":
                clear_terminal()
                tambah_barang_user(inventory_user, current_user)
                input("\nTekan Enter...")
                
            elif pilihan_user == "3":
                clear_terminal()
                update_barang_user(inventory_user, current_user)
                input("\nTekan Enter...")
                
            elif pilihan_user == "4":
                clear_terminal()
                hapus_barang_user(inventory_user, current_user)
                input("\nTekan Enter...")
                
            elif pilihan_user == "5":
                clear_terminal()
                print("Keluar dari menu.")
                input("\nTekan Enter...")
                return "Logout"
            
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
                input("\nTekan Enter...")
        except Exception as e:
            print(f"Terjadi kesalahan dalam menu: {e}")
            input("\nTekan enter untuk kembali ke menu...")

# Fungsi untuk menambah inventaris user
def tambah_barang_user(inventory_user, current_user):
    try:
        print("=== Tambah Barang Baru ===")
        nama_barang = input("Masukkan nama barang: ").strip()
        if not nama_barang:
            print("Nama barang tidak boleh kosong.")
            return
        
        try:
            stok = int(input("Masukkan stok barang: "))
            if stok < 0:
                print("Stok tidak boleh negatif. Silakan coba lagi.")
                return

            harga = int(input("Masukkan harga barang: "))
            if harga < 0:
                print("Harga tidak boleh negatif. Silakan coba lagi.")
                return
        except ValueError:
            print("Stok dan harga harus berupa angka. Silakan coba lagi.")
            return
        
        # Menambahkan barang ke inventaris
        inventory_user[nama_barang] = {"stok": stok, "harga": harga, "added_by": current_user['username']}
        
        # Menambah riwayat aktivitas
        tambah_riwayat(f"Barang baru '{nama_barang}' ditambahkan oleh {current_user['username']} dengan stok {stok} dan harga Rp{harga:,}")
        
        print(f"Barang {nama_barang} berhasil ditambahkan!")
        
        # Simpan data setelah penambahan
        simpan_data()  

    except Exception as e:
        print(f"Terjadi kesalahan saat menambah barang: {e}")

# Fungsi untuk meng-update inventaris user
def update_barang_user(inventory_user, current_user):
    try:
        tampilkan_inventaris_user(inventory_user)
        print("\n=== Update Barang User ===")
        nama_barang = input("Masukkan nama barang yang ingin diupdate: ").strip()

        if not nama_barang:
            print("Nama barang tidak boleh kosong.")
            return
        
        if nama_barang in inventory_user and inventory_user[nama_barang]['added_by'] == current_user['username']:
            stok_lama = inventory_user[nama_barang]["stok"]
            harga_lama = inventory_user[nama_barang]["harga"]

            try:
                stok_baru = int(input(f"Masukkan stok baru (sebelumnya: {stok_lama}): "))
                if stok_baru < 0:
                    print("Stok tidak boleh negatif. Silakan coba lagi.")
                    return

                harga_baru = int(input(f"Masukkan harga baru (sebelumnya: Rp{harga_lama:,}): "))
                if harga_baru < 0:
                    print("Harga tidak boleh negatif. Silakan coba lagi.")
                    return

            except ValueError:
                print("Stok dan harga harus berupa angka. Silakan coba lagi.")
                return
            
            # Update data barang
            inventory_user[nama_barang]["stok"] = stok_baru
            inventory_user[nama_barang]["harga"] = harga_baru
            tambah_riwayat(f"Barang '{nama_barang}' diperbarui oleh {current_user['username']} dari stok {stok_lama} ke {stok_baru} dan harga Rp{harga_lama:,} ke Rp{harga_baru:,}")
            print(f"Barang {nama_barang} berhasil diperbarui!")
        
        else:
            print("Anda hanya bisa mengupdate barang yang Anda tambahkan sendiri.")
        
        # Simpan data setelah update
        simpan_data()  

    except Exception as e:
        print(f"Terjadi kesalahan saat memperbarui barang: {e}")

# Fungsi untuk menghapus inventaris user
def hapus_barang_user(inventory_user, current_user):
    try:
        tampilkan_inventaris_user(inventory_user)
        print("\n=== Hapus Barang User ===")
        nama_barang = input("Masukkan nama barang yang ingin dihapus: ").strip()

        if not nama_barang:
            print("Nama barang tidak boleh kosong.")
            return
        
        if nama_barang in inventory_user and inventory_user[nama_barang]['added_by'] == current_user['username']:
            stok_barang = inventory_user[nama_barang]["stok"]
            del inventory_user[nama_barang]
            tambah_riwayat(f"Barang '{nama_barang}' dihapus oleh {current_user['username']} dengan stok {stok_barang} dihapus dari inventaris.")
            print(f"Barang {nama_barang} berhasil dihapus!")
        else:
            print("Anda hanya bisa menghapus barang yang Anda tambahkan sendiri.")
        simpan_data() # Memanggil fungsi simpan_data() untuk menyimpan data setelah dihapus
    except Exception as e:
        print(f"Terjadi kesalahan saat menghapus barang: {e}")

# Prosedur untuk menangani pilihan admin dalam menu
def menu_admin(inventory, inventory_user, users, current_user):
    while True:
        try:
            clear_terminal()
            print("""
                      
█▀▄▀█ █▀▀ █▄░█ █░█   ▄▀█ █▀▄ █▀▄▀█ █ █▄░█
█░▀░█ ██▄ █░▀█ █▄█   █▀█ █▄▀ █░▀░█ █ █░▀█
──────────────── ⋆⋅☆⋅⋆ ─────────────────── 
          1. Lihat Inventaris   
          2. Tambah Barang                
          3. Update Barang      
          4. Hapus Barang  
          5. Tambah Admin Baru        
          6. Tampilkan User
          7. Hapus akun user
          8. Lihat Riwayat Aktivitas
          9. Logout             
""")
            pilihan_admin = input("Pilih menu: ").strip()
            
            if pilihan_admin == "1":
                clear_terminal()
                tampilkan_inventaris(inventory)
                tampilkan_inventaris_user(inventory_user)
                input("\nTekan Enter...")
                
            elif pilihan_admin == "2":
                clear_terminal()
                tambah_barang(inventory, inventory_user, current_user)
                input("\nTekan Enter...")
                
            elif pilihan_admin == "3":
                clear_terminal()
                update_barang(inventory, inventory_user, current_user)
                input("\nTekan Enter...")
                
            elif pilihan_admin == "4":
                clear_terminal()
                hapus_barang(inventory, inventory_user, current_user)
                input("\nTekan Enter...")
                
            elif pilihan_admin == "5":
                clear_terminal()
                tambah_admin(users, current_user)
                input("\nTekan Enter...")
                
            elif pilihan_admin == "6":
                clear_terminal()
                tampilkan_users(users)
                input("\nTekan Enter...")
                
            elif pilihan_admin == "7":
                clear_terminal()
                hapus_user(users, current_user)
                input("\nTekan Enter...")
                
            elif pilihan_admin == "8":
                clear_terminal()
                tampilkan_riwayat_aktivitas()
                input("\nTekan Enter...")
                
            elif pilihan_admin == "9":
                clear_terminal()
                print("Keluar dari menu.")
                input("\nTekan Enter...")
                break
            
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
                input("\nTekan Enter...")
        except Exception as e:
            print(f"Terjadi kesalahan dalam menu: {e}")
            input("Tekan enter untuk kembali ke menu...")

# Fungsi untuk menambah barang inventaris
def tambah_barang(inventory, inventory_user, current_user):
    if current_user['role'] != "admin":
        print("Hanya admin yang bisa menambahkan barang ke inventaris.")
        return
    
    print("=== Tambah Barang Baru ===")
    pilihan = input("Tambahkan ke: 1. Inventory Utama | 2. Inventory User (Masukkan angka 1 atau 2) : ").strip()

    try:
        if pilihan == "1":  # Fungsi untuk menambahkan barang di inventory utama
            nama_barang = input("Masukkan nama barang: ").strip()
            if not nama_barang:
                print("Nama barang tidak boleh kosong.")
                return

            try:
                stok = int(input("Masukkan stok barang: "))
                if stok < 0:
                    print("Stok tidak boleh negatif. Silakan coba lagi.")
                    return
            except ValueError:
                print("Stok harus berupa angka. Silakan coba lagi.")
                return

            try:
                harga = int(input("Masukkan harga barang: "))
                if harga < 0:
                    print("Harga tidak boleh negatif. Silakan coba lagi.")
                    return
            except ValueError:
                print("Harga harus berupa angka. Silakan coba lagi.")
                return

            if nama_barang in inventory:
                print("Barang sudah ada di inventory utama, gunakan update barang untuk mengubah datanya.")
            else:
                inventory[nama_barang] = {"stok": stok, "harga": harga, "added_by": "admin"}
                tambah_riwayat(f"Admin '{current_user['username']}' menambahkan barang '{nama_barang}' ke inventory utama dengan stok {stok} dan harga Rp{harga:,}.")
                print(f"Barang '{nama_barang}' berhasil ditambahkan ke inventory utama!")

        elif pilihan == "2":  # Fungsi untuk menambahkan barang di inventory user
            nama_barang = input("Masukkan nama barang: ").strip()
            try:
                stok = int(input("Masukkan stok barang: "))
                if stok < 0:
                    print("Stok tidak boleh negatif. Silakan coba lagi.")
                    return
            except ValueError:
                print("Stok harus berupa angka. Silakan coba lagi.")
                return

            try:
                harga = int(input("Masukkan harga barang: "))
                if harga < 0:
                    print("Harga tidak boleh negatif. Silakan coba lagi.")
                    return
            except ValueError:
                print("Harga harus berupa angka. Silakan coba lagi.")
                return

            if nama_barang in inventory_user:
                print("Barang sudah ada di inventory user, gunakan update barang untuk mengubah datanya.")
            else:
                inventory_user[nama_barang] = {"stok": stok, "harga": harga, "added_by": "admin"}
                tambah_riwayat(f"Admin '{current_user['username']}' menambahkan barang '{nama_barang}' ke inventory user dengan stok {stok} dan harga Rp{harga:,}.")
                print(f"Barang '{nama_barang}' berhasil ditambahkan ke inventory user!")

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
    except ValueError:
        print("Input tidak valid. Pastikan semua input berupa angka yang benar.")

    simpan_data()  # Memanggil fungsi simpan_data() untuk menyimpan data setelah ditambah

# Fungsi untuk mengupdate barang
def update_barang(inventory, inventory_user, current_user):
    tampilkan_inventaris(inventory)
    tampilkan_inventaris_user(inventory_user)
    print("\n=== Update Barang ===")
    nama_barang = input("Masukkan nama barang yang ingin diupdate: ").strip()
    if not nama_barang:
        print("Nama barang tidak boleh kosong.")
        return
    
    try:
        if nama_barang in inventory:  # Untuk mengupdate barang di inventory utama
            stok_lama = inventory[nama_barang]["stok"]
            harga_lama = inventory[nama_barang]["harga"]

            try:
                stok_baru = int(input(f"Masukkan stok baru (sebelumnya: {stok_lama}): "))
                if stok_baru < 0:
                    print("Stok tidak boleh negatif. Silakan coba lagi.")
                    return

                harga_baru = int(input(f"Masukkan harga baru (sebelumnya: Rp{harga_lama:,}): "))
                if harga_baru < 0:
                    print("Harga tidak boleh negatif. Silakan coba lagi.")
                    return

            except ValueError:
                print("Stok dan harga harus berupa angka. Silakan coba lagi.")
                return

            inventory[nama_barang]["stok"] = stok_baru
            inventory[nama_barang]["harga"] = harga_baru
            tambah_riwayat(f"Barang '{nama_barang}' diperbarui oleh {current_user['username']} dari stok {stok_lama} ke {stok_baru} dan harga Rp{harga_lama:,} ke Rp{harga_baru:,}")
            print(f"Barang {nama_barang} berhasil diperbarui!")

        elif nama_barang in inventory_user:  # Untuk mengupdate barang di inventory user
            if current_user['role'] == 'admin' or inventory_user[nama_barang]["added_by"] == current_user["username"]:
                stok_lama = inventory_user[nama_barang]["stok"]
                harga_lama = inventory_user[nama_barang]["harga"]

                try:
                    stok_baru = int(input(f"Masukkan stok baru (sebelumnya: {stok_lama}): "))
                    if stok_baru < 0:
                        print("Stok tidak boleh negatif. Silakan coba lagi.")
                        return

                    harga_baru = int(input(f"Masukkan harga baru (sebelumnya: Rp{harga_lama:,}): "))
                    if harga_baru < 0:
                        print("Harga tidak boleh negatif. Silakan coba lagi.")
                        return

                except ValueError:
                    print("Stok dan harga harus berupa angka. Silakan coba lagi.")
                    return

                inventory_user[nama_barang]["stok"] = stok_baru
                inventory_user[nama_barang]["harga"] = harga_baru
                tambah_riwayat(f"Barang '{nama_barang}' diperbarui oleh {current_user['username']} dari stok {stok_lama} ke {stok_baru} dan harga Rp{harga_lama:,} ke Rp{harga_baru:,}")
                print(f"Barang {nama_barang} berhasil diperbarui!")

            else:
                print("Anda tidak memiliki izin untuk mengupdate barang ini.")

        else:
            print("Nama barang tidak ditemukan.")
    except ValueError:
        print("Terjadi kesalahan saat mengupdate barang. Pastikan stok dan harga berupa angka yang valid.")

    simpan_data()  # Memanggil fungsi simpan_data() untuk menyimpan data setelah di-update


# Fungsi untuk menghapus barang inventaris
def hapus_barang(inventory, inventory_user, current_user):
    tampilkan_inventaris(inventory)
    tampilkan_inventaris_user(inventory_user)
    print("\n=== Hapus Barang ===")
    nama_barang = input("Masukkan nama barang yang ingin dihapus: ").strip()
    if not nama_barang:
        print("Nama barang tidak boleh kosong.")
        return
    
    try:
        if nama_barang in inventory: # Untuk menghapus barang di inventory utama
            stok_barang = inventory[nama_barang]["stok"]
            del inventory[nama_barang]
            tambah_riwayat(f"Barang '{nama_barang}' dengan stok {stok_barang} dihapus dari inventaris.")
            print(f"Barang {nama_barang} berhasil dihapus!")

        elif nama_barang in inventory_user: # Untuk menghapus barang di inventory user
            if current_user['role'] == 'admin' or inventory_user[nama_barang]["added_by"] == current_user["username"]:
                del inventory_user[nama_barang]
                tambah_riwayat(f"Barang '{nama_barang}' dihapus oleh {current_user['username']} dari inventory pengguna.")
                print(f"Barang {nama_barang} berhasil dihapus!")
            else:
                print("Anda tidak memiliki izin untuk menghapus barang ini.")

        else:
            print("Nama barang tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")

    simpan_data() # Memanggil fungsi simpan_data() untuk menyimpan data setelah dihapus

# Fungsi untuk menghapus akun user
def hapus_user(users, current_user):
    if current_user['role'] != "admin":
        print("Hanya admin yang bisa menghapus akun user.")
        return

    print("=== Hapus Akun User ===")
    tampilkan_users(users)
    username = input("Masukkan username yang ingin dihapus: ").strip()

    if not username:
        print("Username tidak boleh kosong.")
        return

    # Cek apakah username yang ingin dihapus ada di daftar user
    user_to_delete = None
    try:
        for user in users:
            if user['username'] == username:
                user_to_delete = user
                break

        if user_to_delete:
            if user_to_delete['role'] == "admin":
                print("Anda tidak dapat menghapus akun admin lain.")
            else:
                users.remove(user_to_delete)
                tambah_riwayat(f"Akun '{username}' dihapus oleh admin")
                print(f"Akun {username} berhasil dihapus.")
        else:
            print("Username tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menghapus user: {e}")

    simpan_data() # Memanggil fungsi simpan_data() untuk menyimpan data setelah dihapus

# Fungsi untuk menampilkan daftar pengguna dengan pemisahan peran
def tampilkan_users(users):
    print("\n=== Daftar Pengguna Terdaftar ===")

    # Pastikan list users tidak kosong
    if not users:
        print("Tidak ada pengguna terdaftar.")
        return

    try:
        # Filter pengguna berdasarkan peran
        admins = [user for user in users if user['role'] == 'admin']
        regular_users = [user for user in users if user['role'] == 'user']

        # Buat tabel PrettyTable
        table = PrettyTable()
        table.field_names = ["Username", "Role"]

        # Tampilkan daftar admin
        if admins:
            print("\n-- Admin --")
            for user in admins:
                table.add_row([user['username'], user['role']])
            print(table)
        else:
            print("\n-- Tidak ada admin terdaftar --")

        # Tampilkan daftar pengguna biasa
        if regular_users:
            print("\n-- Pengguna Biasa --")
            table.clear_rows()  # Menghapus baris sebelumnya
            for user in regular_users:
                table.add_row([user['username'], user['role']])
            print(table)
        else:
            print("\n-- Tidak ada pengguna biasa terdaftar --")
    except Exception as e:
        print(f"Terjadi kesalahan saat menampilkan daftar pengguna: {e}")

# Prosedur untuk menampilkan riwayat aktivitas
def tampilkan_riwayat_aktivitas():
    print("\n=== Riwayat Aktivitas ===")
    try:
        if riwayat_aktivitas:
            table = PrettyTable() 
            table.field_names = ["Waktu", "Aktivitas"]
            for waktu, aktivitas in riwayat_aktivitas:
                table.add_row([waktu, aktivitas])
            print(table)
        else:
            print("Belum ada aktivitas yang tercatat.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menampilkan riwayat aktivitas: {e}")

# Menu utama untuk menangani pilihan menu user atau registrasi pengguna
def menu_utama():
    while True:
        try:
            pilihan = input("Pilih menu: \n1. Login\n2. Registrasi Akun User Baru\n3. Keluar\nPilihan: ").strip()

            # Cek jika input kosong
            if not pilihan:
                print("Pilihan tidak boleh kosong. Silakan coba lagi.")
                continue

            if pilihan == "1":
                clear_terminal()
                try:
                    current_user = login(users)  # Memanggil fungsi login
                    input("\nTekan Enter...")
                    if current_user:
                        # Jika user adalah admin
                        if current_user['role'] == 'admin':
                            menu_admin(inventory, inventory_user, users, current_user)  # Memanggil menu admin

                        # Jika user adalah user biasa
                        elif current_user['role'] == 'user':
                            menu_user(inventory_user, inventory, current_user)  # Memanggil menu user
                        
                        else:
                            print("Login gagal. Username atau password salah.")
                except Exception as e:
                    print(f"Terjadi kesalahan saat login: {e}")

            elif pilihan == "2":
                clear_terminal()
                try:
                    registrasi_pengguna(users)  # Memanggil fungsi registrasi untuk user
                except Exception as e:
                    print(f"Terjadi kesalahan saat registrasi: {e}")
                input("\nTekan Enter untuk melanjutkan...")

            elif pilihan == "3":
                clear_terminal()
                print("""
              
▀▀█▀▀ ▒█▀▀▀ ▒█▀▀█ ▀█▀ ▒█▀▄▀█ ░█▀▀█ ▒█░▄▀ ░█▀▀█ ▒█▀▀▀█ ▀█▀ ▒█░▒█ 
░▒█░░ ▒█▀▀▀ ▒█▄▄▀ ▒█░ ▒█▒█▒█ ▒█▄▄█ ▒█▀▄░ ▒█▄▄█ ░▀▀▀▄▄ ▒█░ ▒█▀▀█ 
░▒█░░ ▒█▄▄▄ ▒█░▒█ ▄█▄ ▒█░░▒█ ▒█░▒█ ▒█░▒█ ▒█░▒█ ▒█▄▄▄█ ▄█▄ ▒█░▒█
             
               TELAH MENGGUNAKAN SISTEM INI
""")
                break

            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        except Exception as e:
            print(f"Terjadi kesalahan umum: {e}")

# Memanggil menu utama
menu_utama()
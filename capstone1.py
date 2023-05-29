# Program Rental Mobil
import time 

# List > Dict Informasi Data Mobil
daftar_mobil = [
    {
    "nama": "Honda",
    "tahun": 2019,
    "kondisi": "Baik",
    "harga": 65000,
    "status": "Kosong"
    },
    {
    "nama": "Daihatsu",
    "tahun": 2022,
    "kondisi": "Baik",
    "harga": 85000,
    "status": "Tersedia"
    },
    {
    "nama": "Toyota",
    "tahun": 2015,
    "kondisi": "Baik",
    "harga": 50000,
    "status": "Tersedia" 
    }
    ]

# Untuk Menu Review
done_rental = False
counter = 0
id_rev = ["agus12", "sinta32", "fauzi15"]
review = ["sangat bagus dan cepat", "murah dan oke", "mantaap"]

# Untuk Daftar Login
id_ver = None
password_ver = None

def daftar_login():
    global id_ver, password_ver
    print("\nMasukkan ID dan Password yang ingin didaftarkan (minimal 6 karakter berupa huruf atau angka)")
    id_ver = input("ID: ")
    password_ver = input("Password: ")
    if len(id_ver) < 6 or len(password_ver) < 6:
        print("ID dan Password minimal 6 karakter!")
        daftar_login()
    elif id_ver.isalnum() == False or password_ver.isalnum() == False:
        print("ID dan Password hanya boleh berisi huruf dan angka saja!")
        daftar_login()
    else:
        print("Tekan \"1\" untuk melanjutkan atau \"2\" untuk mengisi ulang input")

def tampil_daftar_mobil():
    print("\nDaftar Mobil Rental")
    print("No.\t| Mobil  \t| Tahun\t| Kondisi  \t| Harga Rental/Hari  \t| Status")
    for i in range(len(daftar_mobil)):
        print(f'{i+1}\t| {daftar_mobil[i]["nama"]}  \t| {daftar_mobil[i]["tahun"]}\t| {daftar_mobil[i]["kondisi"]}  \t| Rp {daftar_mobil[i]["harga"]}  \t\t| {daftar_mobil[i]["status"]}')

def tampil_daftar_mobil_satuan(nama_mobil):
    print("No.\t| Mobil  \t| Tahun\t| Kondisi  \t| Harga Rental/Hari  \t| Status")
    for i in range(len(daftar_mobil)):
        if daftar_mobil[i]["nama"] == nama_mobil:
            print(f'{i+1}\t| {daftar_mobil[i]["nama"]}  \t| {daftar_mobil[i]["tahun"]}\t| {daftar_mobil[i]["kondisi"]}  \t| Rp {daftar_mobil[i]["harga"]}  \t\t| {daftar_mobil[i]["status"]}')
            break

def read_menu():
    global counter
    while True:
        print('''
    Pilihan Menu Untuk Melihat Data (tanpa menggunakan titik):
    1. Melihat semua data 
    2. Melihat salah satu data saja
    3. Kembali ke menu utama 
        ''')
        cek = input("Masukkan Pilihan: ")
        if cek == "1":
            if len(daftar_mobil) > 0:
                counter += 1
                tampil_daftar_mobil()
            else:
                print("Tidak ada data yang dapat ditampilkan. Silahkan tambah data terlebih dahulu")
        elif cek == "2":
            if len(daftar_mobil) > 0:
                pilih = input("Masukkan nama mobil yang ingin ditampilkan: ")
                present = False
                for i in range(len(daftar_mobil)):
                    if daftar_mobil[i]["nama"] == pilih:
                        present = True
                        counter += 1
                        tampil_daftar_mobil_satuan(pilih)
                        break
                if present == False:
                    print("Data tidak ditemukan. Silahkan coba kembali")
            else:
                print("Tidak ada data yang dapat ditampilkan. Silahkan tambah data terlebih dahulu")
        elif cek == "3":
            break
        else:
            print("Input tidak valid. Isi dengan pilihan 1-3")

def create_menu():
    global counter
    while True:
        print('''
    Pilihan Menu Untuk Menambah Data (tanpa menggunakan titik):
    1. Menambah data ke dalam daftar mobil
    2. Kembali ke menu utama
        ''')
        cek = input("Masukkan Pilihan: ")
        if cek == "1":
            new_mobil = input("Masukkan nama mobil yang ingin ditambahkan: ")
            present = False
            for i in range(len(daftar_mobil)):
                if daftar_mobil[i]["nama"] == new_mobil:
                    present = True
                    break
            if present == True:
                print("Data mobil tersebut sudah ada")
            else:
                new_tahun = int(input("Masukkan informasi tahun mobil: "))
                new_kondisi = input("Masukkan informasi kondisi mobil: ")
                new_harga = int(input("Masukkan informasi harga rental mobil per hari: Rp "))
                while True:
                    new_status = input("Masukkan informasi status rental (Tersedia/Kosong): ")
                    if new_status == "Tersedia" or new_status == "Kosong":
                        break
                    else:
                        print("Isi status rental dengan \"Tersedia\" atau \"Kosong\"")
                print("Tekan 1 untuk menyimpan data atau Tekan 2 untuk membatalkan")
                cek = input("Pilihan: ")
                if cek == "1":
                    daftar_mobil.append(dict(nama = new_mobil, tahun = new_tahun, kondisi = new_kondisi, harga = new_harga, status = new_status))
                    counter += 1
                    tampil_daftar_mobil_satuan(new_mobil)
                    print("Data berhasil disimpan")
                elif cek == "2":
                    print("Data tidak disimpan")
                else:
                    print("Input tidak valid. Isi dengan pilihan 1-2")
        elif cek == "2":
            break
        else:
            print("Input tidak valid. Isi dengan pilihan 1-2")

def delete_menu():
    global counter
    while True:
        print('''
    Pilihan Menu Untuk Menghapus Data (tanpa menggunakan titik):
    1. Menghapus data dalam daftar mobil
    2. Kembali ke menu utama
        ''')
        cek = input("Masukkan Pilihan: ")
        if cek == "1":
            del_mobil = input("Masukkan nama mobil yang ingin dihapus: ")
            index = 0
            present = False
            for i in range(len(daftar_mobil)):
                if daftar_mobil[i]["nama"] == del_mobil:
                    index = i
                    present = True
                    break
            if present == False:
                print("Data mobil tersebut tidak ditemukan")
            else:
                tampil_daftar_mobil_satuan(del_mobil)
                print(f"Semua informasi mobil {del_mobil} akan dihapus")
                print("Tekan 1 untuk melanjutkan atau Tekan 2 untuk membatalkan")
                cek = input("Pilihan: ")
                if cek == "1":
                    del daftar_mobil[index]
                    counter += 1
                    print(f"Data mobil {del_mobil} berhasil dihapus")
                elif cek == "2":
                    print(f"Data mobil {del_mobil} tidak dihapus")
                else:
                    print("Input tidak valid. Isi dengan pilihan 1-2")
        elif cek == "2":
            break
        else:
            print("Input tidak valid. Isi dengan pilihan 1-2")

def update_menu():
    global counter
    while True:
        print('''
    Pilihan Menu Untuk Mengupdate Data (tanpa menggunakan titik):
    1. Mengupdate data dalam daftar mobil
    2. Kembali ke menu utama
        ''')
        cek = input("Masukkan Pilihan: ")
        if cek == "1":
            up_mobil = input("Masukkan nama mobil yang ingin diupdate: ")
            index = 0
            present = False
            for i in range(len(daftar_mobil)):
                if daftar_mobil[i]["nama"] == up_mobil:
                    index = i
                    present = True
                    break
            if present == False:
                print("Data mobil tersebut tidak ditemukan")
            else:
                tampil_daftar_mobil_satuan(up_mobil)
                print("Tekan 1 untuk melanjutkan update atau Tekan 2 untuk membatalkan")
                cek = input("Pilihan: ")
                if cek == "1":
                    up_col = input("Masukkan nomor kolom yang ingin diubah (1-4, dimulai dari kolom tahun): ")
                    if up_col == "1":
                        up_tahun = int(input("Masukkan tahun yang baru: "))
                        print("Tekan 1 untuk mengupdate data tahun atau Tekan 2 untuk membatalkan")
                        cek = input("Pilihan: ")
                        if cek == "1":
                            daftar_mobil[index]["tahun"] = up_tahun
                            counter += 1
                            tampil_daftar_mobil_satuan(up_mobil)
                            print("Data tahun berhasil diupdate")
                        elif cek == "2":
                            print("Data tahun tidak diupdate")
                        else:
                            print("Input tidak valid. Isi dengan pilihan 1-2")
                    elif up_col == "2":
                        up_kondisi = input("Masukkan kondisi yang baru: ")
                        print("Tekan 1 untuk mengupdate data kondisi atau Tekan 2 untuk membatalkan")
                        cek = input("Pilihan: ")
                        if cek == "1":
                            daftar_mobil[index]["kondisi"] = up_kondisi
                            counter += 1
                            tampil_daftar_mobil_satuan(up_mobil)
                            print("Data kondisi berhasil diupdate")
                        elif cek == "2":
                            print("Data kondisi tidak diupdate")
                        else:
                            print("Input tidak valid. Isi dengan pilihan 1-2")
                    elif up_col == "3":
                        up_harga = int(input("Masukkan harga rental/hari yang baru: Rp  "))
                        print("Tekan 1 untuk mengupdate data harga rental/hari atau Tekan 2 untuk membatalkan")
                        cek = input("Pilihan: ")
                        if cek == "1":
                            daftar_mobil[index]["harga"] = up_harga
                            counter += 1
                            tampil_daftar_mobil_satuan(up_mobil)
                            print("Data harga rental/hari berhasil diupdate")
                        elif cek == "2":
                            print("Data harga rental/hari tidak diupdate")
                        else:
                            print("Input tidak valid. Isi dengan pilihan 1-2")
                    elif up_col == "4":
                        while True:
                            up_status = input("Masukkan status rental yang baru (Tersedia/Kosong): ")
                            if up_status == "Tersedia" or up_status == "Kosong":
                                break
                            else:
                                print("Isi status rental dengan \"Kosong\" atau \"Tersedia\"")
                        print("Tekan 1 untuk mengupdate data status rental atau Tekan 2 untuk membatalkan")
                        cek = input("Pilihan: ")
                        if cek == "1":
                            daftar_mobil[index]["status"] = up_status
                            counter += 1
                            tampil_daftar_mobil_satuan(up_mobil)
                            print("Data status rental berhasil diupdate")
                        elif cek == "2":
                            print("Data status rental tidak diupdate")
                        else:
                            print("Input tidak valid. Isi dengan pilihan 1-2")
                    else:
                        print("Input tidak valid. Isi dengan pilihan 1-4")
                elif cek == "2":
                    print("Proses update dibatalkan")
                else:
                    print("Input tidak valid. Isi dengan pilihan 1-2")
        elif cek == "2":
            break
        else:
            print("Input tidak valid. Isi dengan pilihan 1-2")

def rental_menu():
    global counter
    global done_rental
    while True:
        print('''
    Pilihan Menu Untuk Merental mobil (tanpa menggunakan titik):
    1. Merental mobil
    2. Kembali ke menu utama
        ''')
        cek = input("Masukkan Pilihan: ")
        if cek == "1":
            tampil_daftar_mobil()
            index = 0
            present = False
            ren_mobil = input("Masukkan nama mobil yang ingin anda rental: ")
            for i in range(len(daftar_mobil)):
                if daftar_mobil[i]["nama"] == ren_mobil:
                    index = i
                    present = True
                    break
            if present == False:
                print("Mobil tidak ada dalam daftar")
            elif daftar_mobil[index]["status"] == "Kosong":
                print("Mobil sedang kosong, silahkan pilih mobil lainnya")
            else:
                while True:
                    lama_rental = int(input(f"Berapa lama anda ingin merental mobil {ren_mobil}? (dalam satuan hari): "))
                    if lama_rental > 30:
                        print("Durasi rental antara 1-30 hari saja")
                    elif lama_rental <= 0:
                        print("Minimal rental selama 1 hari")
                    else:
                        break
                biaya = daftar_mobil[index]["harga"] * lama_rental
                print(f"Biaya rental mobil {ren_mobil} selama {lama_rental} hari adalah sebesar Rp {biaya}")
                print("Tekan 1 untuk melanjutkan rental atau tekan 2 untuk membatalkan rental")
                cek = input("Pilihan: ")
                if cek == "1":
                    while True:
                        bayar = int(input("Masukkan pembayaran anda: Rp "))
                        if bayar < biaya:
                            print(f"Pembayaran anda kurang sebesar Rp {biaya - bayar}")
                        elif bayar > biaya:
                            print(f"Terima kasih! Kembalian anda sebesar Rp {bayar - biaya}")
                            daftar_mobil[index]["status"] = "Kosong"
                            counter += 1
                            done_rental = True
                            break
                        else:
                            print("Terima kasih!")
                            daftar_mobil[index]["status"] = "Kosong"
                            counter += 1
                            done_rental = True
                            break
                elif cek == "2":
                    print("Proses rental dibatalkan")
                else:
                    print("Input tidak valid. Isi dengan pilihan 1-2")
        elif cek == "2":
            break
        else:
            print("Input tidak valid. Isi dengan pilihan 1-2")

def review_menu():
    if len(review) > 0:
        print("Beberapa Review user untuk program ini")
        for i,j in zip(id_rev, review):
            print(f"User {i}\t: {j}")
    while True:
        if id_ver not in id_rev:
            print("\nTuliskan review anda mengenai program ini untuk peningkatan kualitas program ini di masa mendatang:")
            new_rev = input()
            if len(new_rev) > 100:
                print("Review tidak dapat lebih dari 100 karakter")
            else:
                id_rev.append(id_ver)
                review.append(new_rev)
                print("Terima kasih untuk review anda!")
                break
        else:
            print("\nAnda sudah melakukan review. Apakah anda ingin mengedit review anda?")
            print("Tekan 1 untuk melanjutkan atau Tekan 2 untuk membatalkan")
            cek = input("Pilihan: ")
            if cek == "1":
                while True:
                    print("\nTuliskan review anda mengenai program ini untuk peningkatan kualitas program ini di masa mendatang:")
                    new_rev = input()
                    if len(new_rev) > 100:
                        print("Review tidak dapat lebih dari 100 karakter")
                    else:
                        for i in range(len(id_rev)):
                            if id_rev[i] == id_ver:
                                del id_rev[i]
                                del review[i]   
                                break
                        id_rev.append(id_ver)
                        review.append(new_rev)
                        print("Review anda berhasil diedit")
                        break
                break
            elif cek == "2":
                break
            else:
                print("Input tidak valid. Isi dengan pilihan 1-2")
          
# Awal Mulai Program
print("-----Selamat Datang di Program Rental Mobil-----")
print("Anda harus Login terlebih dahulu untuk masuk ke program")
while True:
    # Cek Login/Daftar
    print("Tekan 1 untuk Login atau Tekan 2 untuk Daftar ")
    while True:
        cek = input()
        if cek == "1":
            break
        elif cek == "2":
            daftar_login()
        else:
            print("Input tidak valid. Pilih antara 1 atau 2")
    # Mulai Login
    print("\nSilahkan Login")
    id = input("ID: ")
    password = input("Password: ")
    if id == id_ver and password == password_ver:
        print("Berhasil Login!")
        time.sleep(2) # Ceritanya Efek Loading
        break
    else:
        print("ID atau Password salah, silahkan coba lagi atau mendaftar terlebih dahulu\n")
            
# Menu Utama
while(True):
    print('''
----------RENTAL MOBIL MURAH TAPI GA MURAHAN----------
Pilihan Menu:
1. Tampilkan Daftar Mobil
2. Tambah Mobil Dalam Daftar
3. Hapus Mobil Dalam Daftar
4. Update Daftar Mobil
5. Rental Mobil
6. Tulis Review Untuk Program Ini
7. Keluar Dari Program
    ''')
    cek = input("Masukkan Pilihan Menu: ")
    if cek == "1":
        read_menu()
    elif cek == "2":
        create_menu()
    elif cek == "3":
        delete_menu()
    elif cek == "4":
        update_menu()
    elif cek == "5":
        rental_menu()
    elif cek == "6":
        if counter >= 5 and done_rental == True:
            review_menu()
        else:
            print("Anda harus menggunakan menu lain di program ini (dengan tuntas) minimal sebanyak 5 kali dan sudah merental mobil untuk dapat memberikan review!")
    elif cek == "7":
        print("Terima Kasih, Sampai Jumpa!")
        break
    else:
        print("Pilihan tidak valid. Isi pilihan antara angka 1-7")
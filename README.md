# capstone1_jcds
Tugas Capstone 1 - Pemrograman Dasar Python - Program Rental Mobil

Program ini merupakan Capstone Project pertama dari JCDS (Job Connector Data Science) Purwadhika.
Saat dijalankan, alur dari program antara lain:
  1. Pilihan login, dimana user harus login terlebih dahulu sebelum masuk ke menu utama
  2. Apabila belum memiliki ID dan Password, dapat mendaftar terlebih dahulu
  3. Pendaftaran ID dan Password wajib minimal 6 karakter berupa angka atau huruf (diluar itu tidak dapat mendaftar)
  4. Setelah mendaftar, dapat dilanjutkan untuk melakukan login
  5. Setelah login, akan muncul menu utama yang terdiri dari 7 pilihan:
        a. Tampilkan Menu (read_menu) untuk menampilkan daftar mobil secara keseluruhan atau secara spesifik
        b. Menambah Mobil (create_menu) untuk menambahkan informasi mobil yang baru ke dalam daftar mobil
        c. Menghapus Mobil (delete_menu) untuk menghapus informasi suatu mobil pada daftar mobil
        d. Mengupdate Mobil (update_menu) untuk mengupdate data pada daftar mobil secara spesifik
        e. Merental Mobil (rental_menu) untuk merental mobil dan melakukan pembayaran
        f. Review Program (review_menu) untuk memberikan review mengenai program, dimana pilihan ini hanya dapat diakses apabila user sudah menggunakan pilihan menu lain secara tuntas minimal sebanyak 5 kali dan sudah berhasil merental mobil
        g. Keluar dari program untuk mengakhiri program

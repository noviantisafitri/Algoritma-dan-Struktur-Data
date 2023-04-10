# __Aplikasi Peminjaman Ruang Kelas__
--------------------------------------------------------------------------------------
## _Deskripsi Program_
> Program Aplikasi Peminjaman Ruang Kelas dibuat dengan tujuan untuk membantu memudahkan pengguna dalam melakukan peminjaman ruang kelas yang tersedia. Selain itu, program ini juga membantu admin untuk mengelola pendaftaran ruang kelas dan melakukan monitoring terhadap peminjaman ruang kelas yang telah dilakukan serta membantu dan memudahkan mahasiswa dalam melakukan peminjaman ruang kelas. Dengan begitu, program ini diharapkan dapat meningkatkan efektivitas dan efisiensi dalam penggunaan ruang kelas yang tersedia.

> Program ini dibuat dengan menggunakan Bahasa pemrograman Python dan mengimplementasikan struktur data Linked List. Aplikasi peminjaman ruang kelas ini juga menggunakan sebuah database, yaitu database MongoDB yang digunakan untuk menyimpan data akun mahasiswa dan staff serta data peminjaman ruang kelas.

## _Struktur Project_
> 1.	Folder Controller, berisi file-file controller yang akan mengatur alur program serta mengambil data dari model dan menampilkan ke view.
    -	File Controller Account, sebagai file controller yang berisi logika untuk manajemen akun mahasiswa dan staff, seperti registrasi, login, dan profil user.
    -	File Controller Linked List, sebagai file controller yang berisi logika untuk manajemen data ruang kelas dalam bentuk linked list, dimana data dalam linked list diambil dari database.
    -	File Controller User, sebagai file controller yang berisi logika untuk manajemen data mahasiswa dan staff seperti logika menambahkan peminjaman ruang.
> 2.	Folder Model, berisi file-file model yang berisi fungsi-fungsi untuk mengakses database dan memproses data.
    -	File Database, sebagai file yang berisi class untuk menghubungkan python dan database.
    -	File Ruang, sebagai file yang berisi definisi class Ruang yang digunakan untuk merepresentasikan sebuah node pada struktur data Linked List.
> 3.	Folder View, berisi file-file view yang berisi tampilan antarmuka aplikasi yang akan dilihat oleh pengguna.
    -	File App, sebagai halaman untuk menampilkan informasi dan melakukan peminjaman ruang kelas oleh pengguna yang belum terdaftar sebagai staff atau mahasiswa.
    -	File Mahasiswa, sebagai halaman untuk menampilkan informasi dan melakukan peminjaman ruang kelas oleh mahasiswa.
    -	File Staff, sebagai halaman untuk menampilkan informasi dan daftar peminjaman ruang kelas oleh staff.
> 4. File main, sebagai file utama yang berfungsi untuk menjalankan program.

## _Fitur_ 

- Login dan registrasi mahasiswa: Mahasiswa harus melakukan login terlebih dahulu sebelum dapat melakukan peminjaman ruang kelas. Jika pengguna belum terdaftar, maka ia dapat melakukan registrasi terlebih dahulu.
 
- Peminjaman ruang kelas: Mahasiswa dapat melakukan peminjaman ruang kelas yang tersedia dengan memilih ruang kelas yang diinginkan dan waktu peminjaman.

- CRUD: Admin dapat melakukan operasi Create, Read, Update, dan Delete (CRUD) pada peminjaman ruang kelas.

- Update peminjaman ruang kelas: Admin dapat melakukan update pada pengajuan peminjaman ruang kelas yang dilakukan oleh mahasiswa, yaitu dengan melakukan update pada bagian status peminjaman.

- Lihat daftar peminjaman: Admin dapat melihat semua daftar peminjaman ruang kelas yang telah dilakukan dengan detail ID Peminjaman, Kode Kelas, NIM, Nama, Program Studi, Mata Kuliah, Keperluan, Tanggal Pinjam, Tanggal Selesai, Status, dan Keterangan. Sedangkan mahasiswa hanya dapat melihat pengajuan peminjaman ruang kelas yang telah dilakukan dengan detail ID Peminjaman, Kode Kelas, NIM, Nama, Program Studi, Mata Kuliah, Keperluan, Tanggal Pinjam, Tanggal Selesai, dan Status.

- Search dan Sorting: Admin dapat melakukan search berdasarkan NIM dan Sorting berdasarkan ID, Kode Kelas, NIM dan Nama. Sedangkan Mahasiswa hanya dapat melakukan searching berdasarkan Kode kelas.

- Profil User: User dapat melihat data profilnya. Pada akun mahasiswa, mahasiswa dapat melihat NIM, Nama, Jenis Kelamin, dan Program Studi. Pada akun staff, staff dapat melihat data NIP, Nama, Jenis Kelamin, dan Jabatan. 



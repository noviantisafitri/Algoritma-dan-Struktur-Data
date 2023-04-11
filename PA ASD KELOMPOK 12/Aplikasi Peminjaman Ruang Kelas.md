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

- Pada program ini terdapat library yang digunakan, diantaranya adalah PrettyTable, datetime, dan PyMongo.
  1. PrettyTable merupakan library atau pustaka dalam python yang digunakan untuk membuat / mengeluarkan data dalam bentuk tabel.
  2. Datetime adalah sebuah library atau modul yang dipanggil jika anda membutuhkan segala operasi yang berhubungan demi waktu.
  3. PyMongo berisi alat untuk bekerja dengan MongoDB, dan merupakan cara yang disarankan untuk bekerja dengan MongoDB dari Python.

#__Jalannya Program__

- Login dan registrasi mahasiswa: Mahasiswa harus melakukan login terlebih dahulu sebelum dapat melakukan peminjaman ruang kelas. Jika pengguna belum terdaftar, maka ia dapat melakukan registrasi terlebih dahulu.

![Screenshot (67)](https://user-images.githubusercontent.com/116480927/231031926-85a1c2ed-fb3d-43c1-9421-4296762afc38.png)

![Screenshot (68)](https://user-images.githubusercontent.com/116480927/231031967-b5e4355b-420d-4516-8404-4449361810a8.png)

- Peminjaman ruang kelas: Mahasiswa dapat melakukan peminjaman ruang kelas yang tersedia dengan memilih ruang kelas yang diinginkan dan waktu peminjaman.

![Screenshot (69)](https://user-images.githubusercontent.com/116480927/231032085-6aef84fe-a34c-4e97-80ca-0308982f9bce.png)

- CRUD: Admin dapat melakukan operasi Create, Read, Update, dan Delete (CRUD) pada peminjaman ruang kelas.

![Screenshot (70)](https://user-images.githubusercontent.com/116480927/231032176-51799407-25f5-4fac-91e9-af32d08f233c.png)

- Update peminjaman ruang kelas: Admin dapat melakukan update pada pengajuan peminjaman ruang kelas yang dilakukan oleh mahasiswa, yaitu dengan melakukan update pada bagian status peminjaman.

![Screenshot (70)](https://user-images.githubusercontent.com/116480927/231032247-46d43d7a-fe6b-4bc5-920d-25bc931cdcd1.png)

- Lihat daftar peminjaman: Admin dapat melihat semua daftar peminjaman ruang kelas yang telah dilakukan dengan detail ID Peminjaman, Kode Kelas, NIM, Nama, Program Studi, Mata Kuliah, Keperluan, Tanggal Pinjam, Tanggal Selesai, Status, dan Keterangan. Sedangkan mahasiswa hanya dapat melihat pengajuan peminjaman ruang kelas yang telah dilakukan dengan detail ID Peminjaman, Kode Kelas, NIM, Nama, Program Studi, Mata Kuliah, Keperluan, Tanggal Pinjam, Tanggal Selesai, dan Status.

![Screenshot (72)](https://user-images.githubusercontent.com/116480927/231032319-9f441781-7b1b-4242-a842-b8feba0dea9e.png)

- Search dan Sorting: Admin dapat melakukan search berdasarkan NIM dan Sorting berdasarkan ID, Kode Kelas, NIM dan Nama. Sedangkan Mahasiswa hanya dapat melakukan searching berdasarkan Kode kelas.

![Screenshot (73)](https://user-images.githubusercontent.com/116480927/231032406-395ee92b-5169-4664-8ebf-60e683fc1133.png)

![Screenshot (74)](https://user-images.githubusercontent.com/116480927/231032527-6e781dcc-af7d-4704-ac38-4b2a77880aa4.png)

- Profil User: User dapat melihat data profilnya. Pada akun mahasiswa, mahasiswa dapat melihat NIM, Nama, Jenis Kelamin, dan Program Studi. Pada akun staff, staff dapat melihat data NIP, Nama, Jenis Kelamin, dan Jabatan. 

![Screenshot (75)](https://user-images.githubusercontent.com/116480927/231032560-f364d78f-6a94-43c8-9b68-9957699de18a.png)

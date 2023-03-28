from prettytable import PrettyTable
import os
import time
import random
from datetime import datetime
from pymongo import MongoClient
os.system('cls')

client = MongoClient("mongodb+srv://noviantis112:21november@cluster1.nsfjyfw.mongodb.net/?retryWrites=true&w=majority")

akun = client.akun #database akun 
akun_collection = akun.akun_collection

data = client.data #database peminjaman ruang
data_collection = data.data_collection

class Account : #akun mahasiswa
    def __init__(self):
        self.nama = []
        self.nim = []
        self.prodi = []
        self.jk = []
        self.password = []
        self.akun_nim = []

    def login_staff(self):
        nip = str(input("Masukan NIP : "))
        staff_find = akun_collection.find_one({"nip" : nip})
        if staff_find:
            pasw = str(input("Masukan Password : "))
            nip = staff_find.get("nip")
            nama = staff_find.get("nama")
            jb = staff_find.get("jabatan")
            jk = staff_find.get("jk")
            pas = staff_find.get("password")
            if pasw == pas:
                print("Halo", nama)
            else :
                print("Password anda salah")

        global profil_staff
        profil_staff = {"nip" : nip,"nama" : nama, "jabatan" : jb, "jk" : jk}

    def profil_staf(self):
        profil = PrettyTable(["NIP", "Nama", "Jabatan", "Jenis Kelamin"])
        profil.title = "Profil Mahasiswa"
        profil.add_row([profil_staff["nip"], profil_staff["nama"], profil_staff["jabatan"], profil_staff["jk"]])
        print(profil)

    def registrasi(self):
        nim = str(input("Masukan nim : "))
        nim_find = akun_collection.find_one({"nim" : nim})
        if nim_find:
            print("Akun telah terdaftar, silahkan login")
        else :
            nama = str(input("Masukan nama : "))
            prodi = str(input("Masukan Program Studi : "))
            jeniskelamin = int(input("""
            1. Perempuan
            2. Laki-laki
            Pilih jenis kelamin anda : """))
            if jeniskelamin == 1:
                jeniskelamin = "Perempuan"
            elif jeniskelamin == 2:
                jeniskelamin = "Laki-laki"

            pasw = str(input("Masukan Password : "))
            self.nim.append(nim)
            self.nama.append(nama)
            self.prodi.append(prodi)
            self.jk.append(jeniskelamin)
            self.password.append(pasw)
            for nim,nama,prodi,jeniskelamin, password in zip(self.nim, self.nama, self.prodi, self.jk, self.password):
                akun = {"nim" : nim,
                        "nama" : nama,
                        "prodi" : prodi,
                        "jk" : jeniskelamin,
                        "password" : password}
                self.akun_nim.append(akun)
            akun_collection.insert_many(self.akun_nim)
            print("Registrasi berhasil")

    def login(self):
        nim = str(input("Masukan nim : "))
        password = str(input("Masukan Password : "))

        nim_find = akun_collection.find_one({"nim" : nim})
        
        if nim_find:
            nim_findd = nim_find.get("nim")
            nama_find = nim_find.get("nama")
            prodi_find = nim_find.get("prodi")
            jk_find = nim_find.get("jk")
            password_find = nim_find.get("password")
            if password == password_find:
                print("login berhasil")
                print("Hallo", prof["nama"])
            else :
                print("""
                >> Password salah
                >> Silahkan coba lagi""")
                time.sleep(3)
        else :
            print("Nim tidak ditemukan") 

        global prof
        prof = {"nim" : nim_findd,
                "nama" : nama_find,
                "prodi" : prodi_find,
                "jk" : jk_find,
                "password" : password_find}

    def profil(self):
        profil = PrettyTable(["NIM", "Nama", "Program Studi", "Jenis Kelamin"])
        profil.title = "Profil Mahasiswa"
        profil.add_row([prof["nim"], prof["nama"], prof["prodi"], prof["jk"]])
        print(profil)

class Ruang: #Node untuk menyimpan data peminjaman ruang
    def __init__(self, data):
        self.ref = None
        self.data = {"kode" : data[0],
                    "nim"  : data[1],
                    "nama" : data[2],
                    "prodi" : data[3],
                    "mk" : data[4],
                    "keperluan" : data[5],
                    "tanggal p" : data[6],
                    "tanggal s" : data[7],
                    "status" : data[8],
                    "ket" : data[9]} 
        
class Admin :
        def __init__(self):
            self.head = None

        def add (self, data): #menambahkan data ke dalam node
            new_node = Ruang(data)
            if self.head is None:
                self.head = new_node
            else:
                n = self.head
                while n.ref is not None:
                    n = n.ref
                n.ref = new_node

        def add_database(self): #create peminjaman dari admin
            self.refresh()
            kode = str(input(" Kode : "))
            nim = str(input(" NIM : "))
            nama = str(input(" Nama : "))
            prodi = str(input(" Program Studi : "))
            mk = str(input(" Mata kuliah : "))
            keperluan = str(input(" Keperluan : "))
            tanggal_p = datetime(2023,3,28,17,30)
            tanggal_selesai = datetime(2023,3,28,19,20)
            status = str(input(" Status : "))
            ket = str(input("keterangan : "))
          
            data = {"kode" : kode,
                    "nim" : nim,
                    "nama" : nama,
                    "prodi" : prodi,
                    "mk" : mk,
                    "keperluan" : keperluan,
                    "tanggal p" : tanggal_p,
                    "tanggal s" : tanggal_selesai,
                    "status" : status,
                    "ket" : ket}
            data_collection.insert_one(data).inserted_id
            print("\nData berhasil ditambahkan")
            self.refresh()

        def add_data (self): #membaca data dari database dan menambahkan kedalam node
            tambah = data_collection.find()
            for i in tambah:
                kode = i["kode"]
                nim = i["nim"]
                nama = i["nama"]
                prodi = i["prodi"]
                mk = i["mk"]
                keperluan = i["keperluan"]
                tanggal_p = i["tanggal p"]
                tanggal_s = i["tanggal s"]
                status = i["status"] 
                ket = i["ket"]
                data = [kode, nim, nama, prodi, mk, keperluan, status, tanggal_p, tanggal_s, ket]
            
                self.add(data)
       
        def refresh(self): #mensinkronkan data dari database dan node
            while(self.head != None):
                n = self.head
                self.head = self.head.ref
                n = None
            self.add_data()
            self.update_data()
        
        def display(self): #menampilkan data dalam node
            tabel= PrettyTable(['No','Kode','NIM','Nama', 'Program Studi', 'Mata Kuliah','Keperluan', 'Status', 'Tanggal Pinjam', 'Tanggal Selesai', 'Keterangan'])
            no = 1
            if self.head is None :
                print("Data tidak ditemukan")
            else :
                n = self.head
                while n is not None:
                    tabel.add_row([no, n.data["kode"],n.data["nim"], n.data["nama"], n.data["prodi"], n.data["mk"],n.data["keperluan"], 
                                   n.data["status"], n.data["tanggal p"], n.data["tanggal s"], n.data["ket"]])
                    no += 1
                    n = n.ref
                            
                print(tabel) 
                print("\n")

        def update_data (self):
            t_now = datetime.now()
            lihat = data_collection.find()
            for i in lihat :
                tanggal_s = i["tanggal s"]
                if tanggal_s < t_now:

                    data_collection.update_one({"tanggal s" : tanggal_s}, {"$set" : {"nim" : "kosong"}})
                    data_collection.update_one({"tanggal s" : tanggal_s}, {"$set" : {"nama" : "kosong"}})
                    data_collection.update_one({"tanggal s" : tanggal_s}, {"$set" : {"prodi" : "kosong"}})
                    data_collection.update_one({"tanggal s" : tanggal_s}, {"$set" : {"mk" : "kosong"}})
                    data_collection.update_one({"tanggal s" : tanggal_s}, {"$set" : {"keperluan" : "kosong"}})
                    data_collection.update_one({"tanggal s" : tanggal_s}, {"$set" : {"tanggal p" : "kosong"}})
                    data_collection.update_one({"tanggal s" : tanggal_s}, {"$set" : {"tanggal s" : "kosong"}})
                    data_collection.update_one({"tanggal s" : tanggal_s}, {"$set" : {"ket" : "kosong"}})

        def update (self): #update data di database
            self.display()
            x = str(input("Masukan kode kelas yang ingin diubah : "))
            u = str(input("Masukan status : "))
            data_collection.update_one({"kode" : x }, {"$set" : {"status" : u }})
            self.refresh()

        def delete(self): #delete data di database
            self.display()
            d = str(input("Masukan kode kelas yang ingin dihapus : "))
            data_collection.delete_one({"kode" : d })
            self.refresh()

        def kelas_kosong (self):
            global data_kelas
            data_kelas = {"kode" : [], "ket" : []}
           

            tambah = data_collection.find({"ket" : "kosong"})
            for i in tambah:
                
                data_kelas["kode"].append(i["kode"])
                data_kelas["ket"].append(i["ket"])

            tabel= PrettyTable(['No','Kode','Keterangan'])
            no = 1
            for i in range(len(data_kelas["kode"])):

                tabel.add_row([no,data_kelas['kode'][i],data_kelas['ket'][i]]) 
                no += 1
            print(tabel) 

        def main(self): #menjalankan program admin
            while True:
                pilih = int(input("""

                                1. CREATE
                                2. READ
                                3. UPDATE
                                4. DELETE
                                5. DAFTAR KELAS
                                6. PROFIL
                                7. EXIT
                        
                        Masukan pilihan anda : """))

class Mahasiswa :
        
        def add_peminjaman (self): #create peminjaman dari user
            kode = "000"
            mk = str(input("Mata kuliah : "))
            keperluan = str(input("Keperluan : "))
            # print("Tanggal peminjaman")
            tanggal_p = datetime(2023,3,28,17,30)
            tanggal_selesai = datetime(2023,3,28,18,20)
            nim = prof["nim"]
            nama = prof["nama"]
            prodi = prof["prodi"]
            status = "Pending"

            data = {"kode" : kode,
                    "nim" : nim,
                    "nama" : nama,
                    "prodi" : prodi,
                    "mk" : mk,
                    "keperluan" : keperluan,
                    "tanggal p" : tanggal_p,
                    "tanggal s" : tanggal_selesai,
                    "status" : status,
                    "ket" : "digunakan"}
            a = data_collection.insert_one(data).inserted_id
            print("data berhasil ditambahkan")
            
            self.refresh()

        def read_user(self): #tampilan data peminjaman ruang untuk user
            data = {"kode" : [], "nim" : [], "nama" : [], "prodi" : [], "mk" : [],"keperluan" : [], 
                    "status" : [], "tanggal p" : [], "tanggal s" : []}

            tambah = data_collection.find({"nim" : prof["nim"]})
            for i in tambah:
                
                data["kode"].append(i["kode"])
                data["nim"].append(i["nim"])
                data["nama"].append(i["nama"])
                data["prodi"].append(i["prodi"])
                data["mk"].append(i["mk"])
                data["keperluan"].append(i["keperluan"])
                data["status"].append(i["status"])
                data["tanggal p"].append(i["tanggal p"])
                data["tanggal s"].append(i["tanggal s"])

            tabel= PrettyTable(['No','Kode','NIM','Nama', 'Program Studi', 'Mata Kuliah','Keperluan', 'Status', 'Tanggal Pinjam', 'Tanggal Selesai'])

            no = 1
            for i in range(len(data["kode"])):

                tabel.add_row([no,data['kode'][i], data["nim"][i],data['nama'][i], data['prodi'][i], data["mk"][i] ,data['keperluan'][i],data['status'][i], data["tanggal p"][i], data["tanggal s"][i]]) 
                no += 1

            print(tabel) 

        def read_kelas(self):
            global data_kelas
            data_kelas = {"kode" : [], "ket" : []}
           

            tambah = data_collection.find({"ket" : "kosong"})
            for i in tambah:
                
                data_kelas["kode"].append(i["kode"])
                data_kelas["ket"].append(i["ket"])

            tabel= PrettyTable(['No','Kode','Keterangan'])

            no = 1
            for i in range(len(data_kelas["kode"])):

                tabel.add_row([no,data_kelas['kode'][i],data_kelas['ket'][i]]) 
                no += 1

            print(tabel) 

        def main_user(self): #menjalankan program user
            while True:
                pilih = int(input("""

                                1. CREATE PEMINJAMAN
                                2. LIHAT PENGAJUAN PEMINJAMAN
                                3. DAFTAR KELAS
                                4. PROFIL
                                5. EXIT
                        
                        Masukan pilihan anda : """))
                
acc = Account()
adm = Admin()
mhs = Mahasiswa()

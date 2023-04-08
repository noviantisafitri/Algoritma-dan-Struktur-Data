from Model.Database import Database
from Model.Database import Database
from datetime import datetime
from random import randint
from prettytable import PrettyTable

class User(Database):

    def __init__(self):
        super().__init__()

    def find_nim (self, nim): #mencari nim didatabase sesuai dengan nim yang diinputkan
        nim_f = self.akun_collection.find_one({"nim" : nim})
        return nim_f
    
    def find_nip (self, nip): #mencari nip didatabase sesuai dengan nip yang diinputkan
        nip_f = self.akun_collection.find_one({"nip" : nip})
        return nip_f

    def id_peminjaman(self): #membuat id peminjaman
        no = randint(1000,9999)
        return no
    
    def find_data (self, cari): #mencari satu data kode kelas didatabase sesuai dengan inputan
        cek = self.data_collection.find_one({"kode" : cari})
        return cek
    
    def find_kelas (self, cari): #mencari seluruh data kode kelas didatabase sesuai dengan inputan
        cek = self.data_collection.find({"kode" : cari})
        return cek
    
    def update_data (self, no, status): #update data di database
        return self.data_collection.update_one(no, status)
    
    def delete_data (self, id): #delete data di database
        delete = self.data_collection.delete_one({"no" : id })
        return delete

    def data_bukti_peminjaman(self, id): #mencari data user yang status peminjamannya telah diacc oleh staff
        data = self.data_collection.find_one({"no" : id})
        return data

    def kodeKelas(self): #kode kelas yang tersedia
        kelas = ["D401", "D402", "D403", "D404","C401", "C404", "C402", "C403"]
        return kelas
    
    def readKelasMhs (self, nim): #menampilkan data peminjaman ruang pada mahasiswa
            
            data = {"no" : [],"kode" : [], "nim" : [], "nama" : [], "prodi" : [], "mk" : [],"keperluan" : [], 
                    "status" : [], "tanggalp" : [], "tanggals" : []}
            
            tambah = self.data_collection.find({"nim" : nim})#melakukan pencarian nim 

            for i in tambah: #melakukan perulangan dan mengambil data yang sesuai dengan nim
                data["no"].append(i["no"])
                data["kode"].append(i["kode"])
                data["nim"].append(i["nim"])
                data["nama"].append(i["nama"])
                data["prodi"].append(i["prodi"])
                data["mk"].append(i["mk"])
                data["keperluan"].append(i["keperluan"])
                data["status"].append(i["status"])
                data["tanggalp"].append(i["tanggalp"])
                data["tanggals"].append(i["tanggals"])

            tabel= PrettyTable(['No','Kode','NIM','Nama', 'Program Studi', 'Mata Kuliah','Keperluan', 'Status', 'Tanggal Pinjam', 'Tanggal Selesai'])
            for i in range(len(data["kode"])):
                tabel.add_row([data["no"][i],data["kode"][i], data["nim"][i],data["nama"][i], data["prodi"][i], 
                               data["mk"][i] ,data["keperluan"][i],data["status"][i], data["tanggalp"][i], data["tanggals"][i]]) 
            print(tabel) 

    def updatePeminjamanKelas(self): #jika kelas sudah selesai dilakukan peminjaman maka akan melakukan update secara otomatis
        date = datetime.now()
        cek = self.data_collection.find() #melakukan pengecekan pada semua data didatabase
        for i in cek :
            tanggal_s = i["tanggals"]
            cek =  tanggal_s < date #jika waktu selesai peminjaman kurang dari waktu sekarang
            if cek:
                self.data_collection.update_many({"tanggals" : tanggal_s}, {"$set" : {"ket" : "Selesai"}}) #mengupdate data peminjaman pada kolom status
            else :
                break
                    
    def readKodeKelas(self): #menampilkan semua kode kelas yang tersedia
        tabel= PrettyTable(['No','Kode Kelas'])
        no = 1
        for i in range(len(self.kodeKelas())):

            tabel.add_row([no,self.kodeKelas()[i]]) 
            no += 1
        print(tabel) 

    def addPengajuanPeminjaman(self, idPeminjaman, nim, kode, nama, prodi, mk, keperluan, tanggal_p, tanggal_s, status):
        #memasukan data kedalam database
        data = { "no" : idPeminjaman,  #memasukan data peminjaman oleh user dan staff ke database
        "kode" : kode,
        "nim" : nim,
        "nama" : nama,
        "prodi" : prodi,
        "mk" : mk,
        "keperluan" : keperluan,
        "tanggalp" : tanggal_p,
        "tanggals" : tanggal_s,
        "status" : status,
        "ket" : "Digunakan"}
        self.data_collection.insert_one(data)
        print("\nPeminjaman berhasil ditambahkan")
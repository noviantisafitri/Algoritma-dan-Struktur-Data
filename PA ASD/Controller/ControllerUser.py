from Model.Database import Database
from Model.Database import Database
from datetime import datetime
from prettytable import PrettyTable

class User(Database):
    def __init__(self):
        super().__init__()

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
        cek = self.find_all() #melakukan pengecekan pada semua data didatabase
        for i in cek :
            tanggal_s = i["tanggals"]
            cek =  tanggal_s < date #jika waktu selesai peminjaman kurang dari waktu sekarang
            if cek:
                self.update_data({"tanggals" : tanggal_s}, {"$set" : {"ket" : "Selesai"}}) #mengupdate data peminjaman pada kolom status
                    
    def readKodeKelas(self): #menampilkan semua kode kelas yang tersedia
        tabel= PrettyTable(['No','Kode Kelas'])
        no = 1
        for i in range(len(self.kodeKelas())):

            tabel.add_row([no,self.kodeKelas()[i]]) 
            no += 1
        print(tabel) 

    def addPengajuanPeminjaman(self, idPeminjaman, nim, kode, nama, prodi, mk, keperluan, tanggal_p, tanggal_s, status):
        #memasukan data kedalam database
        self.insert_to_database(idPeminjaman, nim, kode, nama, prodi, mk, keperluan, tanggal_p, tanggal_s, status)
        print("\nData berhasil ditambahkan")
    
    def cekRuangPeminjaman(self,kode, tanggal_p, tanggal_s):
        #jika tanggal peminjaman melebih tanggal selesai peminjaman user sebelumnya atau 
        # tanggal selesai peminjaman yang diinputkan kurang dari tanggal peminjaman user sebelumnya maka dapat dilakukan peminjaman
        if self.find_data(kode).get("ket") == "Digunakan" :
            if tanggal_p > self.find_data(kode).get("tanggals") or tanggal_s < self.find_data(kode).get("tanggalp"):
                pass
            else : 
                print("Mohon maaf kelas sedang digunakan")
                return False
        else :
            pass

    def data_bukti_peminjaman(self, id): #mencari data user yang status peminjamannya telah diacc oleh staff
        data = self.finduser_bp(id)
        return data

from Model.Database import Database
from Model.Database import Database
from datetime import datetime
from prettytable import PrettyTable

fileakun = "Menu.py"

with open(fileakun,"w") as write:
    bp = "buktipeminjaman2.txt"

class User(Database):
    def __init__(self):
        super().__init__()

    def kodeKelas(self):
        kelas = ["D401", "D402", "D403", "D404", "D405", "D406", "D407", "D408", "C401"]
        return kelas
    
    def readKelasMhs (self, nim):
            data = {"no" : [],"kode" : [], "nim" : [], "nama" : [], "prodi" : [], "mk" : [],"keperluan" : [], 
            "status" : [], "tanggal p" : [], "tanggal s" : []}
            tambah = self.data_collection.find({"nim" : nim})
            for i in tambah:
                data["no"].append(i["no"])
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
            for i in range(len(data["kode"])):
                tabel.add_row([data["no"][i],data["kode"][i], data["nim"][i],data["nama"][i], data["prodi"][i], 
                               data["mk"][i] ,data["keperluan"][i],data["status"][i], data["tanggal p"][i], data["tanggal s"][i]]) 
            print(tabel) 

    def updateKelasKosong (self): #jika kelas sudah selesai dilakukan peminjaman maka akan melakukan update secara otomatis
        date = datetime.now()
        cek = self.find_all()
        for i in cek :
            tanggal_s = i["tanggal s"]
            cek =  tanggal_s < date
            if cek:
                self.delete_data_tanggal(tanggal_s)
                # self.update_data({"tanggal s" : tanggal_s}, {"$set" : {"ket" : "kosong"}})
                # self.update_data({"tanggal s" : tanggal_s}, {"$set" : {"status" : "kosong"}})
                # self.update_data({"tanggal s" : tanggal_s}, {"$set" : {"nim" : "kosong"}})
                # self.update_data({"tanggal s" : tanggal_s}, {"$set" : {"nama" : "kosong"}})
                # self.update_data({"tanggal s" : tanggal_s}, {"$set" : {"prodi" : "kosong"}})
                # self.update_data({"tanggal s" : tanggal_s}, {"$set" : {"mk" : "kosong"}})
                # self.update_data({"tanggal s" : tanggal_s}, {"$set" : {"keperluan" : "kosong"}})
                # self.update_data({"tanggal s" : tanggal_s}, {"$set" : {"tanggal p" : "kosong"}})
                # self.update_data({"tanggal s" : tanggal_s}, {"$set" : {"tanggal s" : "kosong"}})
                    
    def readKelasKosong(self):
        tabel= PrettyTable(['No','Kode Kelas'])
        no = 1
        for i in range(len(self.kodeKelas())):

            tabel.add_row([no,self.kodeKelas()[i]]) 
            no += 1
        print(tabel) 

    def addPengajuanPeminjaman(self, kode, tanggal_p, tanggal_s):
        if kode in self.kodeKelas() : #jika kode kelas yang diinputkan berada dalam kode kelas yang tersedia
            tanggal_pinjam = input("Masukkan tanggal peminjaman (dd/mm/yyyy): ")
            time = input("Masukkan waktu (hh:mm:ss): ")
            tanggal_p = datetime.strptime(f"{tanggal_pinjam} {time}", "%d/%m/%Y %H:%M:%S") 

            if datetime.now() > tanggal_p : #mengecek tanggal dan waktu sekarang dengan tanggal dan waktu yang diinputkan
                print("Mohon masukan tanggal dengan benar") #jika waktu peminjaman yang telah diinputkan telah terlewati, maka tidak bisa dilakukan peminjaman
            
            else :
                tanggal_selesai = input("Masukkan tanggal selesai (dd/mm/yyyy): ")
                time2 = input("Masukkan waktu (hh:mm:ss): ")
                tanggal_s = datetime.strptime(f"{tanggal_selesai} {time2}", "%d/%m/%Y %H:%M:%S")
                #mencari kode kelas didatabase dan jika kode kelas ditemukan
                if self.find_data(kode) :
                    #jika tanggal peminjaman melebih tanggal selesai peminjaman user sebelumnya atau 
                    # tanggal selesai peminjaman yang diinputkan kurang dari tanggal peminjaman user sebelumnya maka dapat dilakukan peminjaman
                    if self.find_data(kode).get("status") != "kosong" :
                        if tanggal_p > self.find_data(kode).get("tanggal s") or tanggal_s < self.find_data(kode).get("tanggal p"):
                            pass
                        else :
                            print("Mohon maaf kelas sedang digunakan") 
                            
    def data_bukti_peminjaman(self):
        data =  self.finduser_bp()
        return data

        # with open (bp,"a")as edit:
        #                             print("===============================================",file=edit)
        #                             print("============ BUKTI PEMINJAMAN RUANGAN =========",file=edit)
        #                             print("===============================================",file=edit)
        #                             print(f"Kode              : {kode}",file=edit)
        #                             print("                                               ",file=edit)        
        #                             print(f"Program Studi     : {prodi}", file=edit)
        #                             print("                                               ",file=edit) 
        #                             print(f"Mata Kuliah       : {mk} ",file=edit)
        #                             print("                                               ",file=edit) 
        #                             print(f"Tanggal           : {tgl}",file=edit)
        #                             print("                                               ",file=edit) 
        #                             print(f"Keperluan Kelas   : {keperluan}",file=edit)
        #                             print("                                               ",file=edit)
        #                             print("===============================================",file=edit)   
        # return data
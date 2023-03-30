from pymongo import MongoClient

class Database:
    
    def __init__(self):
        client = MongoClient("mongodb+srv://noviantis112:21november@cluster1.nsfjyfw.mongodb.net/?retryWrites=true&w=majority")

        akun = client.akun #database akun 
        data = client.data #database peminjaman ruang
        self.akun_collection = akun.akun_collection
        self.data_collection = data.data_collection
    
    def find_nim (self, nim):
        nim_f = self.akun_collection.find_one({"nim" : nim})
        return nim_f
    
    def find_nip (self, nip):
        nip_f = self.akun_collection.find_one({"nip" : nip})
        return nip_f
    
    def insert_akun (self, data):
        self.akun_collection.insert_many(data)

    def id_peminjaman(self):
        nomor = self.data_collection.find()
        for i in nomor :
            no = i["no"]
        no += 1
        print(no)
        return no

    def insert_data(self, data):
        self.data_collection.insert_one(data).inserted_id
    
    def insert_to_database(self, no, nim, kode, nama, prodi, mk, keperluan, tanggal_p, tanggal_selesai, status):
        data = { "no" : no,
        "kode" : kode,
        "nim" : nim,
        "nama" : nama,
        "prodi" : prodi,
        "mk" : mk,
        "keperluan" : keperluan,
        "tanggal p" : tanggal_p,
        "tanggal s" : tanggal_selesai,
        "status" : status,
        "ket" : "Digunakan"}
        self.insert_data(data)

    def find_data (self, cari):
        cek = self.data_collection.find_one({"kode" : cari})
        return cek

    def find_data_by(self,cari):
        data = self.data_collection.find(cari)
        # for i in data:
        #     data = [i["kode"],i["nim"],i["nama"],i["prodi"],i["mk"],i["keperluan"],i["tanggal p"],i["tanggal s"],i["status"],i["ket"]]

    def update_data (self, no, status): #update data di database
        self.data_collection.update_one({"no" : no }, {"$set" : {"status" : status}})

    def delete_data (self, kode): #delete data di database
        self.data_collection.delete_one({"kode" : kode })
        
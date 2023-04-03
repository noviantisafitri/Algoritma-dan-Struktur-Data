from pymongo import MongoClient

class Database:
    
    def __init__(self):
        client = MongoClient("mongodb+srv://noviantis112:21november@cluster1.nsfjyfw.mongodb.net/?retryWrites=true&w=majority")

        akun = client.akun #database akun 
        data = client.data #database peminjaman ruang
        self.akun_collection = akun.akun_collection
        self.data_collection = data.data_collection
    
    def find_nim (self, nim): #mencari nim didatabase sesuai dengan nim yang diinputkan
        nim_f = self.akun_collection.find_one({"nim" : nim})
        return nim_f
    
    def find_nip (self, nip): #mencari nip didatabase sesuai dengan nip yang diinputkan
        nip_f = self.akun_collection.find_one({"nip" : nip})
        return nip_f
    
    def insert_akun (self, data): #menambahkan data registrasi akun mahasiswa ke database
        self.akun_collection.insert_many(data)

    def id_peminjaman(self): #membuat id peminjaman
        nomor = self.data_collection.find()
        no = 1100
        if nomor is not None:
            for i in nomor :
                no = i["no"]  
        no += 1
        return no

    def insert_data(self, data): #melakukan insert data ke database
        self.data_collection.insert_one(data).inserted_id
    
    def insert_to_database(self, no, nim, kode, nama, prodi, mk, keperluan, tanggal_p, tanggal_selesai, status):
        data = { "no" : no,  #memasukan data peminjaman oleh user dan staff ke database
        "kode" : kode,
        "nim" : nim,
        "nama" : nama,
        "prodi" : prodi,
        "mk" : mk,
        "keperluan" : keperluan,
        "tanggalp" : tanggal_p,
        "tanggals" : tanggal_selesai,
        "status" : status,
        "ket" : "Digunakan"}
        self.insert_data(data)

    def find_data (self, cari): #mencari satu data kode kelas didatabase sesuai dengan inputan
        cek = self.data_collection.find_one({"kode" : cari})
        return cek
    
    def find_kelas (self, cari): #mencari seluruh data kode kelas didatabase sesuai dengan inputan
        cek = self.data_collection.find({"kode" : cari})
        return cek
    
    def find_all (self): #mencari semua data didatabase
        all = self.data_collection.find()
        return all

    def update_data (self, no, status): #update data di database
        return self.data_collection.update_one(no, status)

    def delete_data (self, id): #delete data di database
        self.data_collection.delete_one({"no" : id })

    def finduser_bp(self, id): #mencari data didatabase berdasarkan no id
        return self.data_collection.find_one({"no" : id})
        

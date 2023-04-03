from Model.Database import Database
from prettytable import PrettyTable

class Account(Database): #akun 
    def __init__(self):
        self.nama = []
        self.nim = []
        self.prodi = []
        self.jk = []
        self.password = []
        self.akun_nim = []
        super().__init__()

    def cekNim(self, nim): #melakukan pengecekan nim di database
        if self.find_nim(nim):
            return True
        else :
            return False
        
    def registrasi(self, nim,nama, prodi, jeniskelamin, pasw):
        if nim != self.find_nim(nim) : #menambahkan data 
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
        self.insert_akun(self.akun_nim) #menambahkan data ke dalam database

    def login(self, cari, password): #melakukan pengecekan akun untuk login
        if cari:
            if password != cari.get("password"): #jika username dan password akun tidak sesuai
                print("Password salah")
                return False
            else :
                return True #jika username ditemukan dan password sesuai
        else:
            print("Akun tidak ditemukan") #jika username tidak ditemukan
            return False
                 
    def profil_mhs(self, nim): #menampilkan data profil mahasiswa
        profil = PrettyTable(["NIM", "Nama", "Program Studi", "Jenis Kelamin"])
        profil.title = "Profil Mahasiswa"
        profil.add_row([self.find_nim(nim).get("nim"), self.find_nim(nim).get("nama"), self.find_nim(nim).get("prodi"), self.find_nim(nim).get("jk")])
        print(profil)

    def profil_adm(self, nip): #menampilkan data profil staff
        profil = PrettyTable(["NIP", "Nama", "Jenis Kelamin", "Jabatan",])
        profil.title = "Profil Staff"
        profil.add_row([self.find_nip(nip).get("nip"), self.find_nip(nip).get("nama"),self.find_nip(nip).get("jk"), self.find_nip(nip).get("jabatan")])
        print(profil)

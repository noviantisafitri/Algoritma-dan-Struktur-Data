from Model.Database import Database
from prettytable import PrettyTable

class Account(Database): #akun mahasiswa
    def __init__(self):
        self.nama = []
        self.nim = []
        self.prodi = []
        self.jk = []
        self.password = []
        self.akun_nim = []
        super().__init__()
    
    def registrasi(self, nim,nama, prodi, jeniskelamin, pasw):
        if nim != self.find_nim(nim) :
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
        self.insert_akun(self.akun_nim)

    def login(self, cari, password):
        if cari:
            if password == cari.get("password"):
                print("Login berhasil")
            else :
                print("Password salah")
    
                
    def profil(self,nim):
        # prof = {"nim" : self.find_nim(nim).get("nim"),
        #         "nama" : self.find_nim(nim).get("nama"),
        #         "prodi" : self.find_nim(nim).get("prodi"),
        #         "jk" : self.find_nim(nim).get("jk")}
        
        # profil = PrettyTable(["NIM", "Nama", "Program Studi", "Jenis Kelamin"])
        # profil.title = "Profil Mahasiswa"
        # profil.add_row([prof["nim"], prof["nama"], prof["prodi"], prof["jk"]])
        # print(profil)

        profil = PrettyTable(["NIM", "Nama", "Program Studi", "Jenis Kelamin"])
        profil.title = "Profil Mahasiswa"
        profil.add_row([self.find_nim(nim).get("nim"), self.find_nim(nim).get("nama"),self.find_nim(nim).get("prodi"), self.find_nim(nim).get("jk")])
        print(profil)
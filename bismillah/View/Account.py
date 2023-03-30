from Controller.ControllerAccount import Account

class Main(Account):
    def __init__(self) :
        super().__init__()

    def registrasiMahasiswa(self):
        nim = str(input("Masukan nim : "))
        if nim == self.find_nim(nim).get("nim"):
            print("NIM telah terdaftar")
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
            self.registrasi(nim,nama,prodi,jeniskelamin,pasw)
            print("Registrasi berhasil")

    def loginMahasiswa(self):
        nim = str(input("Masukan nim : "))
        password = str(input("Masukan Password : "))
        self.login(self.find_nim(nim),password)
        # self.profil(nim)

    def loginStaff(self):
        nip = str(input("Masukan NIP : "))
        pasw = str(input("Masukan Password : "))
        self.login(self.find_nip(nip),pasw)


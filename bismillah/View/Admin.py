from Controller.ControllerAdmin import Admin
from Controller.ControllerLinkedList import LinkedList
from datetime import datetime
from prettytable import PrettyTable

ll = LinkedList()

class MenuAdmin(Admin):
    def __init__(self):
        super().__init__()
    
    def addData(self):
        kode_kelas = ["C401", "C402", "C403", "C404"]
        kode = str(input(" Kode : "))
        if kode in kode_kelas :
            tanggal_pinjam = int(input(" Tanggal Peminjaman : "))
            jam = int(input(" Jam   : "))
            tanggal_selesai = int(input(" Tanggal Selesai   : "))
            jam_s = int(input(" Jam : "))

            tanggal_p = datetime(2023,3,tanggal_pinjam,jam)
            tanggal_s = datetime(2023,3,tanggal_selesai,jam_s)

            if datetime.now() > tanggal_p :
                print("Mohon masukan tanggal dengan benar")
            else :
                if self.find_data(kode) :
                    
                    if tanggal_p > self.find_data(kode).get("tanggal s") or tanggal_s < self.find_data(kode).get("tanggal p"):
                        nim = str(input(" NIM : "))
                        if self.find_nim(nim):
                            nama = self.find_nim(nim).get("nama")
                            prodi = self.find_nim(nim).get("prodi")
                        else :
                            nama = str(input(" Nama : "))
                            prodi = str(input(" Program Studi : "))
                        mk = str(input(" Mata kuliah : "))
                        keperluan = str(input(" Keperluan : "))
                        status = "Done"
                        self.insert_to_database(self.id_peminjaman(), nim, kode, nama, prodi, mk, keperluan, tanggal_p, tanggal_s, status)
                        print("\nData berhasil ditambahkan")
                        ll.refresh()
                    else :
                        print("Mohon maaf kelas sudah sedang digunakan")
        else :
            print("Kode kelas tidak ditemukan")

    def updateData(self):
        id = str(input("Masukan ID yang ingin diubah : "))
        status = str(input("Masukan status : "))
        self.update_data(id, status)

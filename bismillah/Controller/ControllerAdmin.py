from Model.Database import Database
from datetime import datetime

class Admin(Database):
    def __init__(self):
        super().__init__()
    
    # def cari_kelas (self, kode, tp,ts):
    #     now = datetime.now()
    #     if now > tp :
    #         print("Mohon masukan tanggal dengan benar")
    #     else :
    #         cek = self.find_data({"kode" : kode})
    #         if cek :
    #             if tp > cek.get("tanggal s"):
    #                 print("kelas dapat dipinjam, setelah")

    #             elif ts < cek.get("tanggal p"):
    #                 print("kelas dapat dipinjam, sebelum")
    #             else :
    #                 print("Mohon maaf kelas sedang digunakan")
    #         else :
    #             pass
    

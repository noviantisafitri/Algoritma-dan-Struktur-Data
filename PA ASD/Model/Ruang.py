class Ruang: #Node untuk menyimpan data peminjaman ruang
    def __init__(self, data):
        self.data = {"no"   : data[0],
                    "kode" : data[1],
                    "nim"  : data[2],
                    "nama" : data[3],
                    "prodi" : data[4],
                    "mk" : data[5],
                    "keperluan" : data[6],
                    "tanggalp" : data[7],
                    "tanggals" : data[8],
                    "status" : data[9],
                    "ket" : data[10]} 
        # self.data = data
        self.next = None

from Model.Database import Database
from Model.Ruang import Ruang
from prettytable import PrettyTable

class LinkedList (Database):
    def __init__(self):
        self.head = None
        super().__init__()

    def refresh(self): #mensinkronkan data dari database dan node
        while(self.head != None):
            n = self.head
            self.head = self.head.next
            n = None
        self.add_data()
        self.displayData()

    def add_data(self): #encari data di databse
        data = self.data_collection.find()
        for i in data:
            data = [i["no"],i["kode"],i["nim"],i["nama"],i["prodi"],i["mk"],i["keperluan"],i["tanggal p"],i["tanggal s"],i["status"],i["ket"]]
            self.add(data) #menambahkan data dari database kedalam node

    def add (self, data): #menambahkan data ke dalam node
        new_node = Ruang(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node

    def displayData(self):
        tabel= PrettyTable(['No','Kode','NIM','Nama', 'Program Studi', 'Mata Kuliah','Keperluan', 'Tanggal Pinjam', 'Tanggal Selesai','Status',  'Keterangan'])
        if self.head is None :
            print("Data tidak ditemukan")
        else :
            n = self.head
            while n is not None:
                tabel.add_row([n.data["no"], n.data["kode"],n.data["nim"], n.data["nama"], n.data["prodi"], n.data["mk"],n.data["keperluan"],
                               n.data["tanggal p"], n.data["tanggal s"],  n.data["status"], n.data["ket"]])
                n = n.next      
            print(tabel) 

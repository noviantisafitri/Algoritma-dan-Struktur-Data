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
        self.refresh()
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
    
    def fibonacci_search(self, arr, x):
        arr = sorted(arr)
        fib2 = 0 
        fib1 = 1 
        fib = fib1 + fib2 

        while fib < len(arr):
            fib2 = fib1
            fib1 = fib
            fib = fib1 + fib2

        i = 0
        mid = 0
        n = len(arr)
        while fib > 0:
            mid = min(i+fib2, n-1)
            if isinstance(arr[mid], list):
                sub_arr = arr[mid]
                found = False
                for element in sub_arr:
                    if type(element) == type(x) and element == x:
                        found = True
                        break
                if found:
                    return mid, sub_arr.index(x)
                elif type(sub_arr[0]) == type(x) and sub_arr[0] < x:
                    fib = fib1
                    fib1 = fib2
                    fib2 = fib - fib1
                    i = mid
                else:
                    fib = fib2
                    fib1 = fib1 - fib2
                    fib2 = fib - fib1
            else:
                if type(arr[mid]) == type(x) and arr[mid] == x:
                    return mid, 0
                elif type(arr[mid]) == type(x) and arr[mid] < x:
                    fib = fib1
                    fib1 = fib2
                    fib2 = fib - fib1
                    i = mid
                else:
                    fib = fib2
                    fib1 = fib1 - fib2
                    fib2 = fib - fib1

        if isinstance(arr[i], list):
            sub_arr = arr[i]
            found = False
            for element in sub_arr:
                if type(element) == type(x) and element == x:
                    found = True
                    break
            if found:
                return i, sub_arr.index(x)
            else:
                return -1, -1
        else:
            if type(arr[i]) == type(x) and arr[i] == x:
                return i, 0
            else:
                return -1, -1

    def read(self, data = ""):
        #menampilkan data dalam node
        tabel= PrettyTable(['ID','Kode','NIM','Nama', 'Program Studi', 'Mata Kuliah','Keperluan', 'Tanggal Pinjam', 'Tanggal Selesai', 'Status', 'Keterangan'])
        # no = 1
        if(data == ""):
            if self.head is None :
                print("Data tidak ditemukan")
            else :
                n = self.head
                while n is not None:
                    temp = []
                    temp.extend(n.data)
                    tabel.add_row(temp)
                    # no += 1
                    n = n.next
        else:
            for i in range(len(data)):
                temp = []
                temp.extend(data[i])
                tabel.add_row(temp)
                # no += 1
        print(tabel)
        return tabel

    def sort_node(self):
        list_nodes = []
        node = self.head

        label = ['Kode','NIM','Nama', 'Program Studi', 'Mata Kuliah','Keperluan', 'Status', 'Tanggal Pinjam', 'Tanggal Selesai']

        for i in range(len(label)):
            print('{n}. {lbl}'.format(n = i, lbl = label[i]))
        key = int(input("Pilih salah satu key: "))
        while node is not None:
            list_nodes.append(node.data)
            node = node.next
        sorted_nodes = self.quick_sort(list_nodes, 0, len(list_nodes), key)
        return sorted_nodes

    def quick_sort(self, node_list, firsti, lasti, key:int):
        if lasti <= firsti:
            return node_list
                
        if firsti == lasti:
            return node_list

        part = self.partition(node_list, firsti, lasti, key)
        self.quick_sort(node_list, firsti, part - 1, key)
        self.quick_sort(node_list, part, lasti, key)

        return node_list

    def partition(self, node_list, firsti, lasti, key:int):
        pivot = node_list[firsti][key]
        batas = firsti + 1

        for i in range(firsti+1, lasti):
            if node_list[i][key] < pivot:
                node_list[batas], node_list[i] = node_list[i], node_list[batas]
                batas += 1

        node_list[batas-1], node_list[firsti] = node_list[firsti], node_list[batas-1]
        return batas
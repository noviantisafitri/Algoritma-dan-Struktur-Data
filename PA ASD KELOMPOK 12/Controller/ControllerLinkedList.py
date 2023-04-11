from Model.Database import Database
from Model.Ruang import Ruang
from Controller.ControllerUser import User
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
        User().updatePeminjamanKelas()
        self.add_data()
         
    def add_data(self): #mencari data di databse
        data = self.data_collection.find({"ket" : "Digunakan"})
        for i in data:
            data = [i["no"],i["kode"],i["nim"],i["nama"],i["prodi"],i["mk"],i["keperluan"],i["tanggalp"],i["tanggals"],i["status"],i["ket"]]
            self.add(data) #menambahkan data dari database kedalam node

    def add(self, data): #menambahkan data ke dalam node
        new_node = Ruang(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node 

    def displayData(self, data = ""):
        #menampilkan data dalam node
        self.refresh()
        tabel= PrettyTable(['ID','Kelas','NIM','Nama', 'Program Studi', 'Mata Kuliah','Keperluan', 'Tanggal Pinjam', 'Tanggal Selesai', 'Status', 'Keterangan'])

        if(data == ""):
            if self.head is None :
                print("Data tidak ditemukan")
            else :
                n = self.head
                while n is not None:
                    
                    tabel.add_row([n.data["no"], n.data["kode"],n.data["nim"], n.data["nama"], n.data["prodi"], n.data["mk"],n.data["keperluan"],
                                   n.data["tanggalp"], n.data["tanggals"],  n.data["status"], n.data["ket"]])
                  
                    n = n.next
        else:
            for i in range(len(data)):
                temp = []
                temp.extend(data[i])
                tabel.add_row(temp)
                
        print(tabel)

    def hasilSearchKodekelas(self, data):
        tabel= PrettyTable(['ID','Kelas','Tanggal Pinjam', 'Tanggal Selesai'])
        for i in range(len(data)):
            tabel.add_row([data[i][0], data[i][1], data[i][7], data[i][8]])
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

    def searchKelas(self, search):
        self.refresh()
        list_nodes = []
        temp_list = []
        cursor = self.convertData()
        for data in cursor:
            list_nodes.append(data["kode"])
            temp_list.append(data)
        searching = self.fibonacci_search(list_nodes, search)
        if searching[0] == -1:
            return False
        else:
            list_nodes = []
            for x in temp_list:
                if search == x["kode"]:
                    list_nodes.append(list(x.values())[0:])
            return list_nodes

    def searchNIM(self, search):
        self.refresh()
        list_nodes = []
        temp_list = []
        cursor = self.convertData()
        for data in cursor:
            list_nodes.append(data["nim"])
            temp_list.append(data)
        searching = self.fibonacci_search(list_nodes, search)
        if searching[0] == -1:
            return False
        else:
            list_nodes = []
            for x in temp_list:
                if search == x["nim"]:
                    list_nodes.append(list(x.values())[0:])
            return list_nodes
        
    def convertData(self):
        if self.head == None:
            return []
        else:
            current = self.head
            result = []
            while current != None:
                result.append(current.data)
                current = current.next
            return result


    def sort_node(self,key):
        list_nodes = []
        n = self.head
            
        while n is not None:
            convert_array = list(n.data.values()) #melakukan convert type data dictionary ke list
            list_nodes.append(convert_array)
            n = n.next
        sort = self.quick_sort(list_nodes, 0, len(list_nodes), key)
        return sort

    def quick_sort(self, node, first, last, key):
        
        if last <= first:
            return node
                
        if first == last:
            return node

        part = self.partition(node, first, last, key)
        self.quick_sort(node, first, part - 1, key)
        self.quick_sort(node, part, last, key)
        
        return node
        

    def partition(self, node, first, last, key):
        pivot = node[first][key]
        batas = first + 1

        for i in range(first+1, last):
            if node[i][key] < pivot:
                node[batas], node[i] = node[i], node[batas]
                batas += 1

        node[batas-1], node[first] = node[first], node[batas-1]
        return batas
    

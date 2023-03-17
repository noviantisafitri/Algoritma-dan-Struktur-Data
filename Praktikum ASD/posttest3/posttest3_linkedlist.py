import os
import time
from prettytable import PrettyTable
from datetime import date

class Node:
    def __init__(self,data): 
        self.next = None
        self.data = data
        self.prev = None

class History:
    def __init__(self):
        self.head = None

    def isEmpty(self): 
        if self.head is None:
            return True
        return False
 
    def display(self): #menampilkan data dalam node
        tabel= PrettyTable(['No','History'])
        tabel.title = date.today() 
        no = 1
        if self.head is None :
            print("History kosong")
        else :
            n = self.head
            while n is not None:

                tabel.add_row([no, n.data])
                no += 1
                n = n.next
                
            print(tabel) 
            print("\n")

    def add(self, value): #menambahkan data kedalam node
        new_node = Node(value)
        if self.isEmpty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        print("Sedang menambahkan history....")
        time.sleep(2)
        os.system('cls')
        print(">",value,"<","berhasil ditambahkan\n")
        self.display()

    def delete(self, position): #menghapus data dalam node sesuai letak/posisi
        n = self.head
        if self.head is None:
            print("History kosong")
        elif position == 1:
            self.head = self.head.next
            print("Sedang menghapus history....")
            time.sleep(2)
            os.system('cls')
            print(">",n.data,"<", "berhasil dihapus\n")
            self.display()
        else:
            n = self.head
            count = 1
            while n is not None and count != position:
                prev = n
                n = n.next
                count += 1
            if n is None:
                print("History tidak ditemukan.".format(position))
            else:
                prev.next = n.next
                print("Sedang menghapus history....")
                time.sleep(2)
                os.system('cls')
                print(">",n.data,"<", "berhasil dihapus\n")
                self.display()
                
        history_hapus.append(n.data)

    def delete_all(self): #menghapus semua data/node
        while(self.head != None):
            n = self.head
            history_hapus.append(n.data)
            self.head = self.head.next
            n = None
        print("Sedang menghapus semua history....")
        time.sleep(2)
        os.system('cls')
        print("Semua history telah berhasil dihapus")

    def back (self): 
        while True :
            b = input(">>> Tekan enter untuk kembali ke menu sebelumnya : ")
            if b == "":
                os.system('cls')
                break

    def history_add(self):
        tabel= PrettyTable(['No','History'])
        tabel.title = "History add" 
        no = 1
        for i in range(len(history_tambah)) :
            tabel.add_row([no, history_tambah[i]])
            no += 1
                
        print(tabel) 
        print("\n")

    def history_delete(self):
        tabel= PrettyTable(['No','History'])
        tabel.title = "History delete" 
        no = 1
        for i in range(len(history_hapus)) :
            tabel.add_row([no, history_hapus[i]])
            no += 1
                
        print(tabel) 
        print("\n")
        
history_tambah = [] #menampung semua data yang ditambah    
history_hapus = [] #menampung semua data yang dihapus

doubly = History()#object 
while True :
    os.system('cls')
    pilih = int(input("""
    -------------------------------------
        1. Add
        2. Read
        3. Delete
        4. History
        5. Exit
    -------------------------------------
        Masukan pilihan anda : """))
    
    if pilih == 1:
        add = "y"
        while add == "y":
            os.system('cls')
            x = str(input("\nMasukan data : "))
            os.system('cls')
            doubly.add(x)
            history_tambah.append(x)

            add = str(input("Apakah anda ingin menambahkan data lagi? (y/n) : "))

    elif pilih == 2:
        os.system('cls')
        print("Sedang menampilkan history....")
        time.sleep(2)
        os.system('cls')
        doubly.display()
        doubly.back()

    elif pilih == 3:
        os.system('cls')
        while True :
            hps = int(input("""
                        Pilih metode hapus history
                    -------------------------------------
                        1. Hapus berdasarkan nomor
                        2. Hapus semua history
                        3. Back
                    -------------------------------------
                        Masukan pilihan anda : """))
            if hps == 1:
                os.system('cls')
                doubly.display()
                x = int(input("Masukan history yg ingin dihapus : "))
                os.system('cls')
                doubly.delete(x)
                doubly.back()
            elif hps == 2:
                os.system('cls')
                doubly.delete_all()
                doubly.back()
            elif hps == 3:
                break

    elif pilih == 4:
        os.system('cls')
        while True :
            his = int(input("""
                                Lihat History
                    -------------------------------------
                        1. History Add
                        2. History Delete
                        3. Back
                    -------------------------------------
                        Masukan pilihan anda : """))
            if his == 1:
                os.system('cls')
                doubly.history_add()
                doubly.back()
            elif his == 2:
                os.system('cls')
                doubly.history_delete()
                doubly.back()
            elif his == 3:
                break
            
    elif pilih == 5:
        os.system('cls')
        print("Program telah selesai")
        break       

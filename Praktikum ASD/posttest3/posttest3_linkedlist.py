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

    def delete_all(self): #menghapus semua data/node
        while(self.head != None):
            n = self.head
            self.head = self.head.next
            n = None
        print("Sedang menghapus semua history....")
        time.sleep(2)
        os.system('cls')
        print("Semua history telah berhasil dihapus")

    def back (self): 
        while True :
            b = input(">>> Tekan enter untuk kembali ke menu awal : ")
            if b == "":
                os.system('cls')
                break

doubly = History()#object 
while True:
    try :
        os.system('cls')
        pilih = int(input("""
        -------------------------------------
            1. Add
            2. Read
            3. Delete
            4. Exit
        -------------------------------------
            Masukan pilihan anda : """))
        
        if pilih == 1:
            add = "y"
            while add == "y":
                os.system('cls')
                x = str(input("\nMasukan data : "))
                os.system('cls')
                doubly.add(x)

                add = str(input("Apakah anda ingin menambahkan data lagi? (y/n) : "))

        elif pilih == 2:
            os.system('cls')
            print("Sedang menampilkan history....")
            time.sleep(2)
            os.system('cls')
            doubly.display()
            doubly.back()

        elif pilih == 3:
            while True :
                os.system('cls')
                hps = int(input("""
                            Pilih metode hapus history
                        ------------------------------------
                            1. Hapus berdasarkan nomor
                            2. Hapus semua history
                        ------------------------------------
                            Masukan pilihan anda : """))
                if hps == 1:
                    remove = "y"
                    while remove == "y":
                        os.system('cls')
                        doubly.display()
                        x = int(input("Masukan no history yg ingin dihapus : "))
                        os.system('cls')
                        doubly.delete(x)
                        remove = str(input("Apakah anda ingin menghapus history lagi? (y/n) : "))
                    break
                elif hps == 2:
                    os.system('cls')
                    doubly.delete_all()
                    doubly.back()
                    break
                    
        elif pilih == 4:
            os.system('cls')
            print("Program telah selesai")
            break
    except:
        print("Perhatikan Inputan")
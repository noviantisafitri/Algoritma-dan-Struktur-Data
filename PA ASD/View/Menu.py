from Controller.ControllerAccount import Account
from Controller.ControllerUser import User
from Controller.ControllerLinkedList import LinkedList
import os
import time
from datetime import datetime

ll = LinkedList()
acc = Account()
user = User()


fileakun = "Menu.py"

with open(fileakun,"w") as write:
    bp = "buktipeminjaman2.txt"

                                                                #ACCOUNT

def registrasiMahasiswa(): #fungsi untuk membuat akun mahasiswa
    nim = str(input("Masukan nim : "))
    if acc.cekNim(nim): #melakukan pencarian nim yang telah diinput ke database
        print("NIM telah terdaftar")
        return False
    else : #jika nim tidak ada dalam database maka bisa melakukan registrasi
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
        acc.registrasi(nim,nama,prodi,jeniskelamin,pasw) #melakukan proses penambahan data regis ke database
        print("Registrasi berhasil")
        return True

def loginMahasiswa(): 
    global nim_mhs
    nim_mhs = str(input("Masukan nim : "))
    password = str(input("Masukan Password : "))
    if acc.login(acc.find_nim(nim_mhs),password): #melakukan pencarian nim dan password didatabase
        print("Login berhasil")
        return True #jika user ditemukan
    else :
        return False #jika user tidak ditemukan/password salah

def loginStaff():
    nip = str(input("Masukan NIP : "))
    pasw = str(input("Masukan Password : "))
    if acc.login(acc.find_nip(nip),pasw): #melakukan pencocokan username dan password staff
        print("Login berhasil")
        return True #jika akun ditemukan
    else :
        return False #jika akun tidak ditemukan

def profilMhs(): #menampilkan profil mahasiswa
    acc.profil_mhs(nim_mhs) #mengambil data mahasiswa dari database

                                                                #ADMIN
                                                                  
def addData(): #menambahkan data oleh admin
    # try :
        kode = str(input("Kode : "))

        if kode in user.kodeKelas() : #jika kode kelas yang diinputkan berada dalam kode kelas yang tersedia
            tanggal_pinjam = input("Masukkan tanggal peminjaman (dd/mm/yyyy): ")
            time = input("Masukkan waktu (hh:mm:ss): ")
            tanggal_p = datetime.strptime(f"{tanggal_pinjam} {time}", "%d/%m/%Y %H:%M:%S") 

            if datetime.now() > tanggal_p : #mengecek tanggal dan waktu sekarang dengan tanggal dan waktu yang diinputkan
                print("Mohon masukan tanggal dengan benar") #jika waktu peminjaman yang telah diinputkan telah terlewati, maka tidak bisa dilakukan peminjaman
            
            else :
                tanggal_selesai = input("Masukkan tanggal selesai (dd/mm/yyyy): ")
                time2 = input("Masukkan waktu (hh:mm:ss): ")
                tanggal_s = datetime.strptime(f"{tanggal_selesai} {time2}", "%d/%m/%Y %H:%M:%S")
                #mencari kode kelas didatabase dan jika kode kelas ditemukan
                if user.find_data(kode) :
                    #jika tanggal peminjaman melebih tanggal selesai peminjaman user sebelumnya atau 
                    # tanggal selesai peminjaman yang diinputkan kurang dari tanggal peminjaman user sebelumnya maka dapat dilakukan peminjaman
                    if user.find_data(kode).get("status") != "kosong" :
                        if tanggal_p > user.find_data(kode).get("tanggal s") or tanggal_s < user.find_data(kode).get("tanggal p"):
                            pass
                        else :
                            print("Mohon maaf kelas sedang digunakan") 

                nim = str(input("NIM : "))
                if user.find_nim(nim): #jika nim mahasiswa ditemukan/telah terdaftar maka akan mencari dan mengambil data nama dan prodi 
                    nama = user.find_nim(nim).get("nama")
                    prodi = user.find_nim(nim).get("prodi")

                else : #jika nim belum terdaftar maka akan diminta untuk menginputkan nama dan prodi
                    nama = str(input("Nama : "))
                    prodi = str(input("Program Studi : "))

                mk = str(input("Mata kuliah : "))
                keperluan = str(input("Keperluan : "))
                status = "Done" 
                #memasukan data kedalam database
                user.insert_to_database(user.id_peminjaman(), nim, kode, nama, prodi, mk, keperluan, tanggal_p, tanggal_s, status)
                print("\nData berhasil ditambahkan")
                ll.displayData()#menampilkan data  
        else :
            print("Kode kelas tidak ditemukan")
    # except :
    #     print("Mohon perhatikan inputan")

def updateData(): #melakukan update data didatabase
    global id
    ll.displayData()
    id = int(input("Masukan ID yang ingin diubah : "))
    status = str(input("Masukan status : "))
    user.update_data({"no" : id }, {"$set" : {"status" : status}}) #melakukan update data pada bagian status berdasarkan ID
    # ll.displayData()
    data = user.data_bukti_peminjaman()
    kode = data.get("kode")
    prodi = data.get("prodi")
    mk = data.get("mk")
    tgl = data.get("tanggal s")
    keperluan = data.get("keperluan")

    with open (bp,"a")as edit:
                            print("===============================================",file=edit)
                            print("============ BUKTI PEMINJAMAN RUANGAN =========",file=edit)
                            print("===============================================",file=edit)
                            print(f"Kode              : {kode}",file=edit)
                            print("                                               ",file=edit)        
                            print(f"Program Studi     : {prodi}", file=edit)
                            print("                                               ",file=edit) 
                            print(f"Mata Kuliah       : {mk} ",file=edit)
                            print("                                               ",file=edit) 
                            print(f"Tanggal           : {tgl}",file=edit)
                            print("                                               ",file=edit) 
                            print(f"Keperluan Kelas   : {keperluan}",file=edit)
                            print("                                               ",file=edit)
                            print("===============================================",file=edit)   
    return data

#def bukti_peminjaman():
                    
                    

def deleteData(): #mengahpus data didatabase
    ll.displayData()
    del_id = int(input("Masukan ID yang ingin dihapus : "))
    user.delete_data(del_id) #menghapus data berdasarkan ID
    ll.displayData()

                                                                #USER

def addPeminjaman():
    kode = str(input("Kode : "))

    if kode in user.kodeKelas() : #jika kode kelas yang diinputkan berada dalam kode kelas yang tersedia
        tanggal_pinjam = input("Masukkan tanggal peminjaman (dd/mm/yyyy): ")
        time = input("Masukkan waktu (hh:mm:ss): ")
        tanggal_p = datetime.strptime(f"{tanggal_pinjam} {time}", "%d/%m/%Y %H:%M:%S") 

        if datetime.now() > tanggal_p : #mengecek tanggal dan waktu sekarang dengan tanggal dan waktu yang diinputkan
            print("Mohon masukan tanggal dengan benar") #jika waktu peminjaman yang telah diinputkan telah terlewati, maka tidak bisa dilakukan peminjaman
        
        else :
            tanggal_selesai = input("Masukkan tanggal selesai (dd/mm/yyyy): ")
            time2 = input("Masukkan waktu (hh:mm:ss): ")
            tanggal_s = datetime.strptime(f"{tanggal_selesai} {time2}", "%d/%m/%Y %H:%M:%S")
            #mencari kode kelas didatabase dan jika kode kelas ditemukan
            if user.find_data(kode) :
                #jika tanggal peminjaman melebih tanggal selesai peminjaman user sebelumnya atau 
                # tanggal selesai peminjaman yang diinputkan kurang dari tanggal peminjaman user sebelumnya maka dapat dilakukan peminjaman
                if user.find_data(kode).get("status") != "kosong" :
                    if tanggal_p > user.find_data(kode).get("tanggal s") or tanggal_s < user.find_data(kode).get("tanggal p"):
                        pass
                    else :
                        print("Mohon maaf kelas sedang digunakan") 

            #mencari data user didatabase dan mengambil data nim, nama dan prodi
            nim = user.find_nim(nim_mhs).get("nim")
            nama = user.find_nim(nim_mhs).get("nama")
            prodi = user.find_nim(nim_mhs).get("prodi")

            mk = str(input(" Mata kuliah : "))
            keperluan = str(input(" Keperluan : "))
            status = "Pending"

            #memasukan data kedalam database
            user.insert_to_database(user.id_peminjaman(), nim, kode, nama, prodi, mk, keperluan, tanggal_p, tanggal_s, status)
            print("\nData berhasil ditambahkan")
            ll.displayData()
    else :
        print("Kode kelas tidak ditemukan")

def readPeminjaman(): #melihat data peminjaman yang telah dilakukan
    user.readKelasMhs(nim_mhs)

def readDaftarKelas(): #melihat daftar kelas yang sedang tidak digunakan atau statusnya kosong
    ll.refresh()
    user.updateKelasKosong()
    user.readKelasKosong()

#SORT

def sortData():
    ll.refresh()
    ll.displayData()
    choice = input("Sort data [Y/N]: ")
    if choice.lower() == 'y':
        os.system('cls')
        ll.read(ll.sort_node())
    ll.refresh()

#SEARCH
def searchKelas():
    list_nodes = []
    temp_list = []
    cursor = ll.find_all()
    for data in cursor:
        list_nodes.append(data["kode"])
        temp_list.append(data)
    search = input("Masukkan Kode Kelas yang ingin dicari: ")
    searching = ll.fibonacci_search(list_nodes, search)
    if searching[0] == -1:
        return False
    else:
        list_nodes = []
        for x in temp_list:
            if search == x["kode"]:
                list_nodes.append(list(x.values())[1:])
        return list_nodes
    
def searchKodeKelas() :
    temp_data = searchKelas()
    if temp_data is False:
        print("Kode kelas tidak ditemukan!")
    else:
        ll.read(temp_data)

def searching_node_nim():
    list_nodes = []
    temp_list = []
    cursor = ll.find_all()
    for data in cursor:
        list_nodes.append(data["nim"])
        temp_list.append(data)
    search = input("Masukkan NIM yang ingin dicari: ")
    searching = ll.fibonacci_search(list_nodes, search)
    if searching[0] == -1:
        return False
    else:
        list_nodes = []
        for x in temp_list:
            if search == x["nim"]:
                list_nodes.append(list(x.values())[1:])
        return list_nodes
    
def searchNim():
    ll.displayData()
    temp_data = searching_node_nim()
    if temp_data is False:
        print("NIM tidak ditemukan!")
    else:
        ll.read(temp_data)

def back(): #fungsi untuk kembali kemenu sebelumnya
    while True :
        b = input(">>> Tekan enter untuk kembali ke menu sebelumnya : ")
        if b == "":
            os.system('cls')
            break

def mainProgram():
    os.system('cls')
    while True:
        # try:
            role = int(input("""
                            1. Mahasiswa
                            2. Staff
                            3. EXIT
                            Masukan pilihan anda : """))
            if role == 1:
                while True:
                    os.system('cls')
                    pil = int(input("""
                                1. Login
                                2. Registrasi
                                3. EXIT
                                Pilih : """))
                    if pil == 1 :
                        os.system('cls')
                        if loginMahasiswa():
                            while True:
                                os.system('cls')
                                pilih = int(input("""

                                                1. CREATE PEMINJAMAN
                                                2. LIHAT PENGAJUAN PEMINJAMAN
                                                3. DAFTAR KELAS
                                                4. SEARCH KELAS
                                                5. PROFIL
                                                6. EXIT
                                        
                                        Masukan pilihan anda : """))
                                if pilih == 1:
                                    os.system('cls')
                                    addPeminjaman()
                                    back()
                                elif pilih == 2:
                                    os.system('cls')
                                    readPeminjaman()
                                    back()
                                elif pilih == 3:
                                    os.system('cls')
                                    readDaftarKelas()
                                    back()
                                elif pilih == 4:
                                    os.system('cls')
                                    searchKodeKelas()
                                    back()
                                elif pilih == 5:
                                    os.system('cls')
                                    profilMhs()
                                    back()
                                elif pilih == 6:
                                    break
                        else :
                            time.sleep(3)
                            continue

                    elif pil == 2 :
                        os.system('cls')
                        if registrasiMahasiswa():
                            pass
                        else :
                            time.sleep(3)
                            continue
                    elif pil == 3:
                        os.system('cls')
                        break

            elif role == 2 :
                os.system('cls')
                if loginStaff():
                    while True:
                        os.system('cls')
                        pilih = int(input("""

                                        1. CREATE
                                        2. READ
                                        3. UPDATE
                                        4. DELETE
                                        5. SORT
                                        6. SEARCH
                                        7. DAFTAR KELAS
                                        8. PROFIL
                                        9. EXIT
                                
                                Masukan pilihan anda : """))
                        
                        os.system('cls')
                        if pilih == 1:
                            os.system('cls')
                            addData()
                            back()
                        elif pilih == 2:
                            os.system('cls')
                            ll.displayData()
                            back()
                        elif pilih == 3:
                            os.system('cls')
                            updateData()
                            back()
                        elif pilih == 4:
                            os.system('cls')
                            deleteData()
                            back()
                        elif pilih == 5:
                            os.system('cls')
                            sortData()
                            back()
                        elif pilih == 6:
                            os.system('cls')
                            searchNim()
                            back()
                        elif pilih == 7:
                            os.system('cls')
                            readDaftarKelas()
                            back()
                        elif pilih == 8:
                            pass
                        elif pilih == 9:
                            break
                else :
                    continue
        # except ValueError:
        #     print("Mohon perhatikan inputan")
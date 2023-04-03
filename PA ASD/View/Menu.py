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
        nama = str(input("Masukan nama : ")).capitalize()
        prodi = str(input("Masukan Program Studi : ")).capitalize()
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
        os.system('cls')
        print("Login berhasil")
        print("Halo",acc.find_nim(nim_mhs).get("nama"))
        time.sleep(3)
        return True #jika user ditemukan
    else :
        return False #jika user tidak ditemukan/password salah

def loginStaff():
    global nip
    nip = str(input("Masukan NIP : "))
    pasw = str(input("Masukan Password : "))
    if acc.login(acc.find_nip(nip),pasw): #melakukan pencocokan username dan password staff
        os.system('cls')
        print("Login berhasil")
        print("Halo",acc.find_nip(nip).get("nama"))
        time.sleep(3)
        return True #jika akun ditemukan
    else :
        return False #jika akun tidak ditemukan

def profilMhs(): #menampilkan profil mahasiswa
    acc.profil_mhs(nim_mhs) #mengambil data mahasiswa dari database

def profilStaff(): #menampilkan profil staff
    acc.profil_adm(acc.find_nip(nip).get("nip"))

                                                                #ADMIN
                                                                  
def addData(): #menambahkan data oleh admin
    # try :
        kode = str(input("Kode : ")).capitalize()
        if kode in user.kodeKelas() : #jika kode kelas yang diinputkan berada dalam daftar kode kelas yang tersedia
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
                if user.find_data(kode):
                    for i in user.find_kelas(kode): #melakukan pencarian data pada kode kelas yang sama
                            
                        if i["ket"] == "Digunakan" : #jika ket pada setiap kode kelas "Digunakan" maka akan melakukan pencocokan pada tanggal peminjaman 
                            if tanggal_p > i["tanggals"] or tanggal_s < i["tanggalp"]: #melakukan pengecekan pada tanggal peminjaman dan selesai
                                formDataPeminjaman(kode, tanggal_p, tanggal_s) #fungsi untuk melakukan isi data peminjaman
                            else :
                                print("Mohon maaf kelas sedang digunakan") #jika waktu peminjaman yang diinputkan bertabrakan dengan peminjaman yang telah ada didatabase           
                else :
                    formDataPeminjaman(kode, tanggal_p, tanggal_s)
        else :
            print("Kode kelas tidak ditemukan") #jika kode kelas yang diinputkan tidak ada didalam daftar kode kelas yang tersedia
    # except :
    #     print("Mohon perhatikan inputan")

def formDataPeminjaman(kode, tanggal_p, tanggal_s): #form data peminjaman
    nim = str(input("NIM : "))
    if user.find_nim(nim): #jika nim mahasiswa ditemukan/telah terdaftar maka akan mencari dan mengambil data nama dan prodi 
        nama = user.find_nim(nim).get("nama")
        prodi = user.find_nim(nim).get("prodi")

    else : #jika nim belum terdaftar maka akan diminta untuk menginputkan nama dan prodi
        nama = str(input("Nama : ")).capitalize()
        prodi = str(input("Program Studi : ")).capitalize()

    mk = str(input("Mata kuliah : ")).capitalize()
    keperluan = str(input("Keperluan : ")).capitalize()
    status = "Done" 
    idP = user.id_peminjaman()
    user.addPengajuanPeminjaman(idP, nim, kode, nama, prodi, mk, keperluan, tanggal_p, tanggal_s, status)
    ll.displayData()#menampilkan data  
    buktiPeminjaman(idP)

def updateData(): #melakukan update data didatabase
    ll.displayData()
    id = int(input("Masukan ID yang ingin diubah : "))
    status = str(input("Masukan status : ")).capitalize()
    user.update_data({"no" : id }, {"$set" : {"status" : status}}) #melakukan update data pada bagian status berdasarkan ID
   
    if status == "Done" :
        buktiPeminjaman(id)

    ll.displayData()

def buktiPeminjaman(id): #
    kode = user.data_bukti_peminjaman(id).get("kode")
    prodi = user.data_bukti_peminjaman(id).get("prodi")
    mk = user.data_bukti_peminjaman(id).get("mk")
    tgl = user.data_bukti_peminjaman(id).get("tanggals")
    keperluan = user.data_bukti_peminjaman(id).get("keperluan")

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
                   

def deleteData(): #mengahpus data didatabase
    ll.displayData()
    del_id = int(input("Masukan ID yang ingin dihapus : "))
    user.delete_data(del_id) #menghapus data berdasarkan ID
    ll.displayData()

                                                                #USER

def addPeminjaman():
    kode = str(input("Kode : ")).capitalize()

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
            nim = user.find_nim(nim_mhs).get("nim")
            nama = user.find_nim(nim_mhs).get("nama")
            prodi = user.find_nim(nim_mhs).get("prodi")
            #mencari kode kelas didatabase dan jika kode kelas ditemukan
            if user.find_data(kode):
                for i in user.find_kelas(kode):
                        #jika tanggal peminjaman melebih tanggal selesai peminjaman user sebelumnya atau 
                        # tanggal selesai peminjaman yang diinputkan kurang dari tanggal peminjaman user sebelumnya maka dapat dilakukan peminjaman
                    if i["ket"] == "Digunakan" :
                        if tanggal_p > i["tanggals"] or tanggal_s < i["tanggalp"]:
                            mk = str(input("Mata kuliah : ")).capitalize()
                            keperluan = str(input("Keperluan : ")).capitalize()
                            status = "Pending"
                            user.addPengajuanPeminjaman(user.id_peminjaman(), nim, kode, nama, prodi, mk, keperluan, tanggal_p, tanggal_s, status)

                        else :
                            print("Mohon maaf kelas sedang digunakan")
                            break
            else :
                mk = str(input("Mata kuliah : ")).capitalize()
                keperluan = str(input("Keperluan : ")).capitalize()
                status = "Pending"

                #memasukan data kedalam database
                user.addPengajuanPeminjaman(user.id_peminjaman(), nim, kode, nama, prodi, mk, keperluan, tanggal_p, tanggal_s, status)

    else :
        print("Kode kelas tidak ditemukan")

def readPeminjaman(): #melihat data peminjaman yang telah dilakukan
    user.readKelasMhs(nim_mhs)

def readDaftarKelas(): #melihat daftar kelas yang sedang tidak digunakan atau statusnya kosong
    ll.refresh()
    user.readKodeKelas()

#SORT

def sortData():
    ll.refresh()
    sort = ll.sort_node()
    os.system('cls')
    ll.displayData(sort)

#SEARCH
def searchKelas():
    list_nodes = []
    temp_list = []
    cursor = ll.find_all()
    for data in cursor:
        list_nodes.append(data["kode"])
        temp_list.append(data)
    search = input("Masukkan Kode Kelas yang ingin dicari: ").capitalize()
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
        ll.displayData(temp_data)

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
            else :
                print("Nim tidak ditemukan")
        return list_nodes
    
def searchNim():
    temp_data = searching_node_nim()
    if temp_data == False:
        print("NIM tidak ditemukan!")
    else:
        ll.displayData(temp_data)

def back(): #fungsi untuk kembali kemenu sebelumnya
    while True :
        b = input(">>> Tekan enter untuk kembali ke menu sebelumnya : ")
        if b == "":
            os.system('cls')
            break


                                                    #MENU - MENU
def welcome():
    print(""" 
                ░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗
                ░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝
                ░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░
                ░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░
                ░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
                ░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝
                """)
    
def roleUser():
    print("""
    PILIH ROLE

    1. MAHASISWA
    2. STAFF
    3. EXIT\n""")

def pilihLogin():
    print("""  
    PILIH LOGIN

    1. LOGIN
    2. REGISTRASI
    3. EXIT\n""")

def menuUser():
    print("""
            MENU USER

    1. CREATE PEMINJAMAN
    2. LIHAT PENGAJUAN PEMINJAMAN
    3. DAFTAR KELAS
    4. SEARCH KELAS
    5. PROFIL
    6. EXIT\n""")

def menuAdmin():
    print("""    
    MENU ADMIN

    1. CREATE
    2. READ
    3. UPDATE
    4. DELETE
    5. SORT
    6. SEARCH
    7. DAFTAR KELAS
    8. PROFIL
    9. EXIT\n""")

def mainProgram():
    os.system('cls')
    welcome()
    time.sleep(3)
    while True:
        try:
            os.system('cls')
            roleUser()
            role = int(input("Masukan pilihan anda : "))
            if role == 1:
                while True:
                    os.system('cls')
                    pilihLogin()
                    pil = int(input("Masukan Pilihan anda : "))
                    if pil == 1 :
                        os.system('cls')
                        if loginMahasiswa():
                            while True:
                                os.system('cls')
                                menuUser()
                                pilih = int(input("Masukan pilihan anda : "))
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
                        menuAdmin()
                        pilih = int(input("Masukan pilihan anda : "))
                        if pilih == 1:
                            os.system('cls')
                            addData()
                            back()
                        elif pilih == 2:
                            os.system('cls')
                            user.updatePeminjamanKelas()
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
                            os.system('cls')
                            profilStaff()
                            back()
                        elif pilih == 9:
                            break
                else :
                    continue
        except ValueError:
            print("Mohon perhatikan inputan")

from Controller.ControllerAccount import Account
from Controller.ControllerUser import User
from Controller.ControllerLinkedList import LinkedList
from View import Mahasiswa
import os
import time
from datetime import datetime, timedelta

ll = LinkedList()
acc = Account()
user = User()

def loginStaff():
    global nip
    try :
        nip = str(input(">>> Masukan NIP : "))
        pasw = str(input(">>> Masukan Password : "))
        if acc.login(user.find_nip(nip),pasw): #melakukan pencocokan username dan password staff
            os.system('cls')
            print("Login berhasil")
            print("Halo",user.find_nip(nip).get("nama"))
            time.sleep(3)
            return True #jika akun ditemukan
        else :
            return False #jika akun tidak ditemukan
    except :
        print("\n- Mohon perhatikan inputan")

def profilStaff(): #menampilkan profil staff
    acc.profil_adm(user.find_nip(nip).get("nip"))

                                                                #ADMIN
                                                                  
def addPeminjaman(nip = ""): #menambahkan data oleh admin
    try :
        kode = str(input(">>> Kode : ")).capitalize()
        if kode in user.kodeKelas() : #jika kode kelas yang diinputkan berada dalam daftar kode kelas yang tersedia
            tanggal_pinjam = input(">>> Masukkan tanggal peminjaman (dd/mm/yyyy): ")
            time = input("  > Masukkan waktu (hh:mm:ss): ")
            tanggal_p = datetime.strptime(f"{tanggal_pinjam} {time}", "%d/%m/%Y %H:%M:%S") 

            if datetime.now() > tanggal_p : #mengecek tanggal dan waktu sekarang dengan tanggal dan waktu yang diinputkan
                print("\n- Mohon masukan tanggal dengan benar") #jika waktu peminjaman yang telah diinputkan telah terlewati, 
                                                            #maka tidak bisa dilakukan peminjaman
            
            else :
                tanggal_selesai = input(">>> Masukkan tanggal selesai (dd/mm/yyyy): ")
                time2 = input("  > Masukkan waktu (hh:mm:ss): ")
                tanggal_s = datetime.strptime(f"{tanggal_selesai} {time2}", "%d/%m/%Y %H:%M:%S")
                waktu_p = timedelta(hours=1)
                jam_p = tanggal_s - tanggal_p

                if tanggal_s < tanggal_p :
                    print("\n- Peminjaman tidak dapat diproses karena tanggal tidak sesuai")
                #mencari kode kelas didatabase dan jika kode kelas ditemukan
                else :
                    if jam_p >= waktu_p :
                        if user.find_data(kode):
                            for i in user.find_kelas(kode): #melakukan pencarian data pada kode kelas yang sama
                                    
                                if i["ket"] == "Digunakan" : #jika ket pada setiap kode kelas "Digunakan" maka akan melakukan pencocokan pada tanggal peminjaman 
                
                                    if tanggal_p > i["tanggals"] or tanggal_s < i["tanggalp"]: #melakukan pengecekan pada tanggal peminjaman dan selesai
                                        if nip == "": #user.find_nip(nip):
                                            formDataPeminjaman(kode, tanggal_p, tanggal_s) #fungsi untuk melakukan isi data peminjaman
                                            break
                                        else:
                                            Mahasiswa.formPeminjamanMhs(kode, tanggal_p, tanggal_s)
                                            break
                                    else :
                                        print("\n- Mohon maaf kelas sedang digunakan") #jika waktu peminjaman yang diinputkan bertabrakan dengan peminjaman yang telah ada didatabase     
                                else : 
                                
                                    if nip == "":
                                        formDataPeminjaman(kode, tanggal_p, tanggal_s)             
                                        break
                                    else :
                                        Mahasiswa.formPeminjamanMhs(kode, tanggal_p, tanggal_s)
                                        break    
                        else :
                            if nip == "":
                                formDataPeminjaman(kode, tanggal_p, tanggal_s)             
                                            #formDataPeminjaman(kode, tanggal_p, tanggal_s) #fungsi untuk melakukan isi data peminjaman
                            else :
                                Mahasiswa.formPeminjamanMhs(kode, tanggal_p, tanggal_s)
                            # formDataPeminjaman(kode, tanggal_p, tanggal_s) 
                    else : 
                        print("\n- Waktu minimal peminjaman ruang adalah 1 jam")                  
        else :
            print("\n- Kode kelas tidak ditemukan") #jika kode kelas yang diinputkan tidak ada didalam daftar kode kelas yang tersedia
    
    except :
        print("\n- Mohon masukan inputan dengan benar")

def formDataPeminjaman(kode, tanggal_p, tanggal_s): #form data peminjaman
    try :
        nim = str(input(">>> NIM : "))
        if user.find_nim(nim): #jika nim mahasiswa ditemukan/telah terdaftar maka akan mencari dan mengambil data nama dan prodi 
            nama = user.find_nim(nim).get("nama")
            prodi = user.find_nim(nim).get("prodi")

        else : #jika nim belum terdaftar maka akan diminta untuk menginputkan nama dan prodi
            while True:
                nama = str(input(">>> Nama : ")).capitalize()
                prodi = str(input(">>> Program Studi : ")).capitalize()
                if 2 < len(nama) < 30 and 2 < len(prodi) < 30:
                    break
                else:
                    print("\n- Panjang karakter nama dan prodi harus diantara 2-30")

        if nim.isnumeric() and len(nim) == 10:
            if (nama.isnumeric() or prodi.isnumeric()):
                print("\n- Input tidak boleh angka")
            elif (nama =="" or prodi == ""):
                print("\n- Input tidak boleh kosong")
            else :
                mk = str(input(">>> Mata kuliah : ")).capitalize()
                keperluan = str(input(">>> Keperluan : ")).capitalize()

                if (mk.isnumeric() or keperluan.isnumeric()):
                    print("\n- Input tidak boleh angka")
                elif (mk == "" or keperluan == ""):
                    print("\n- Input tidak boleh kosong")
                else:
                    status = "Done" 
                    idP = user.id_peminjaman()
                    user.addPengajuanPeminjaman(idP, nim, kode, nama, prodi, mk, keperluan, tanggal_p, tanggal_s, status) 
                    buktiPeminjaman(idP)
        else :
            print("\n- Harap masukan NIM dengan benar")
            
    except :
        print("\n- Mohon perhatikan inputan")

def updateData(): #melakukan update data didatabase
    try :
        ll.displayData()
        id = int(input(">>> Masukan ID yang ingin diubah : "))
        if id not in user.cari_id(id).get("no"):
            print("\n- ID tidak ditemukan")
        else :
            status = str(input(">>> Masukan status : ")).capitalize()
            user.update_data({"no" : id }, {"$set" : {"status" : status}}) #melakukan update data pada bagian status berdasarkan ID
        
            if status == "Done" :
                buktiPeminjaman(id)

            ll.displayData()
    except :
        print("\n- Mohon perhatikan inputan")

def buktiPeminjaman(id): #
    kode = user.cari_id(id).get("kode")
    prodi = user.cari_id(id).get("prodi")
    mk = user.cari_id(id).get("mk")
    tgl = user.cari_id(id).get("tanggals")
    keperluan = user.cari_id(id).get("keperluan")

    with open ("buktipeminjaman2.txt","a") as edit:
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
    try :
        ll.displayData()
        del_id = int(input(">>> Masukan ID yang ingin dihapus : "))
        del_id not in user.delete_data(del_id) #menghapus data berdasarkan ID
    except:
        print("\n- ID tidak ditemukan")

def readDaftarKelas(): #melihat daftar kelas yang sedang tidak digunakan atau statusnya kosong
    ll.refresh()
    user.readKodeKelas()

#SORT

def sortData():
    try:
        ll.refresh()

        label = ['ID','Kode Kelas','NIM','Nama']

        for i in range(len(label)):
            print('{n}. {lbl}'.format(n = i, lbl = label[i]))
            
        key = int(input("Pilih salah satu key : "))
        if key <= 3:
            sort = ll.sort_node(key)
            os.system('cls')
            ll.displayData(sort)
        else :
            print("\n- Key tidak tersedia")
    except:
        print("\n- Mohon perhatikan inputan")
    
def searchNimMhs():
    try:
        search = input("Masukkan NIM yang ingin dicari : ")
        temp_data = ll.searchNIM(search)
        if temp_data == False:
            print("\n- NIM tidak ditemukan!")
        else:
            ll.displayData(temp_data)
    except:
        print("\n- Mohon perhatikan inputan")

def back(): #fungsi untuk kembali kemenu sebelumnya
    while True :
        b = input("\n>>> Tekan enter untuk kembali ke menu sebelumnya <<<")
        if b == "":
            os.system('cls')
            break

def menuStaff():
    print("""    
        MENU STAFF
✿   ✿   ✿   ✿   ✿   ✿
    1. CREATE
    2. READ
    3. UPDATE
    4. DELETE
    5. SORT
    6. SEARCH
    7. DAFTAR KELAS
    8. PROFIL
    9. EXIT
✿   ✿   ✿   ✿   ✿   ✿\n""")

def MenuStaff():
        os.system('cls')
        if loginStaff():     
            while True:
                os.system('cls')
                try:
                    menuStaff()
                    pilih = int(input("✎ Masukan pilihan anda : "))
                    if pilih == 1:
                        os.system('cls')
                        addPeminjaman()
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
                        searchNimMhs()
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
                except:
                    print("\n- Mohon perhatikan inputan")
        else :
            time.sleep(3)
            os.system('cls')

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
            print("Halo",user.find_nip(nip).get("nama")) #mengambil nama staff dari database
            time.sleep(3)
            return True #jika akun ditemukan
        
        else :
            return False #jika akun tidak ditemukan
    except :
        print("\n- Mohon perhatikan inputan")

def profilStaff(): #menampilkan profil staff
    acc.profil_adm(user.find_nip(nip).get("nip"))

                                                                #ADMIN
                                                                  
def addPeminjaman(nip = ""): #menambahkan data peminjaman ruang
    try :
        kode = str(input(">>> Kode : ")).capitalize()
        if kode in user.kodeKelas() : #jika kode kelas yang diinputkan berada dalam daftar kode kelas yang tersedia
            tanggal_pinjam = input(">>> Masukkan tanggal peminjaman (dd/mm/yyyy): ")
            time = input("    > Masukkan waktu (hh:mm:ss): ")
            tanggal_p = datetime.strptime(f"{tanggal_pinjam} {time}", "%d/%m/%Y %H:%M:%S") 

            if datetime.now() > tanggal_p : #mengecek tanggal dan waktu sekarang dengan tanggal dan waktu yang diinputkan
                print("\n- Mohon masukan tanggal dengan benar") #jika waktu peminjaman yang telah diinputkan telah terlewati, 
                                                                #maka tidak bisa dilakukan peminjaman
            
            else : #jika tanggal peminjaman telah sesuai
                hari = timedelta(days=30) #waktu maks pengajuan peminjaman
                hari_p = tanggal_p - datetime.now()

                if hari_p > hari: #jika waktu peminjaman untuk lebih dari 30 hari kedepan
                    print("\n- Peminjaman hanya untuk maksimal 30 hari kedepan")

                else : #jika waktu pengajuan peminjaman kurang dari 30 hari kedepan
                    tanggal_selesai = input(">>> Masukkan tanggal selesai (dd/mm/yyyy): ")
                    time2 = input("    > Masukkan waktu (hh:mm:ss): ")
                    tanggal_s = datetime.strptime(f"{tanggal_selesai} {time2}", "%d/%m/%Y %H:%M:%S")

                    waktu_p = timedelta(hours=1) #waktu minimum peminjaman
                    jam_p = tanggal_s - tanggal_p #melakukan perhitungan jam peminjaman

                    if tanggal_s < tanggal_p : #jika tanggal selesai tidak sesuai atau kurang dari tanggal peminjaman
                        print("\n- Peminjaman tidak dapat diproses karena tanggal tidak sesuai")
                
                    else :

                        if jam_p >= waktu_p : #jika jam peminjaman lebih dari 1 jam

                            if user.find_data(kode): #jika kode kelas ditemukan dalam database

                                for i in user.find_kelas(kode): #melakukan pencarian data pada kode kelas yang sama
                                        
                                    if i["ket"] == "Digunakan" : #jika ket pada setiap kode kelas "Digunakan" maka akan melakukan pencocokan pada tanggal peminjaman 
                    
                                        if tanggal_p > i["tanggals"] or tanggal_s < i["tanggalp"]: #melakukan pengecekan pada tanggal peminjaman dan selesai
                                            if nip == "": 
                                                formDataPeminjaman(kode, tanggal_p, tanggal_s) #fungsi untuk melakukan isi data peminjaman oleh admin
                                                break
                                            else:
                                                Mahasiswa.formPeminjamanMhs(kode, tanggal_p, tanggal_s) #fungsi untuk melakukan isi data peminjaman oleh mahasiswa
                                                break
                                        else :
                                            print("\n- Mohon maaf kelas sedang digunakan") #jika waktu peminjaman yang diinputkan bertabrakan dengan 
                                                                                        #peminjaman yang telah ada didatabase     
                                    
                                    else : #jika status kelas didatabase adalah "Selesai"
                                    
                                        if nip == "":
                                            formDataPeminjaman(kode, tanggal_p, tanggal_s)             
                                            break
                                        else :
                                            Mahasiswa.formPeminjamanMhs(kode, tanggal_p, tanggal_s)
                                            break  

                            else : #jika kode kelas tidak ada didatabase/belum ada peminjaman
                                if nip == "":
                                    formDataPeminjaman(kode, tanggal_p, tanggal_s)             
                                                
                                else :
                                    Mahasiswa.formPeminjamanMhs(kode, tanggal_p, tanggal_s)
                                
                        else : #jika jam peminjaman < 1 jam
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

        if nim.isnumeric() and len(nim) == 10: #jika nim berupa angka dan terdiri dari 10 angka

            if (nama.isnumeric() or prodi.isnumeric()): #jika nama dan prodi berupa angka
                print("\n- Input tidak boleh angka")

            elif (nama =="" or prodi == ""): #jika nama dan prodi diinput kosong
                print("\n- Input tidak boleh kosong")

            else : #jika nama dan prodi berupa alphabet

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
        
        else : #jika nim bukan angka atau tidak terdiri dari 10 angka
            print("\n- Harap masukan NIM dengan benar")
            
    except :
        print("\n- Mohon perhatikan inputan")

def updateData(): #melakukan update data didatabase
    try :
        ll.displayData() #menampilkan data di node

        id = int(input(">>> Masukan ID yang ingin diubah : ")) #memilih id yang akan diubah

        if id != user.cari_id(id).get("no"): #jika id yang diinput tidak ada di database
            print("\n- ID tidak ditemukan")

        else : #jika id ditemukan didatabase
            status = str(input(">>> Masukan status : ")).capitalize()
            user.update_data({"no" : id }, {"$set" : {"status" : status}}) #melakukan update data pada bagian status berdasarkan ID
            print("\n---Data berhasil diupdate---")
        
            if status == "Done" :
                buktiPeminjaman(id)

    except :
        print("\n- Mohon perhatikan inputan")

def buktiPeminjaman(id): 
    #mengambil data dari database
    kode = user.cari_id(id).get("kode")
    prodi = user.cari_id(id).get("prodi")
    mk = user.cari_id(id).get("mk")
    tgl = user.cari_id(id).get("tanggals")
    keperluan = user.cari_id(id).get("keperluan")

    with open ("buktipeminjaman2.txt","a") as edit: #membuka file txt untuk menampilkan bukti peminjaman
                            
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
                   

def deleteData(): #mengahapus data didatabase
    try :
        ll.displayData() #menampilkan data didatabase
        del_id = int(input(">>> Masukan ID yang ingin dihapus : "))
        user.delete_data(del_id) #menghapus data berdasarkan ID
        print("\n---Data berhasil dihapus---")
    except:
        print("\n- ID tidak ditemukan")

def readDaftarKelas(): #melihat daftar kelas yang sedang tidak digunakan atau statusnya kosong
    ll.refresh()
    user.readKodeKelas()

#SORT

def sortData():
    try:
        ll.refresh() #merefresh data di node

        label = ['ID','Kode Kelas','NIM','Nama']

        for i in range(len(label)): #menampilkan label/key yang tersedia
            print('{n}. {lbl}'.format(n = i, lbl = label[i]))
            
        key = int(input("Pilih salah satu key : ")) #memilih untuk melakukan sort berdasarkan key yang diinginkan
        if key <= 3: #jika key yang diinput <= 3
            sort = ll.sort_node(key) #melakukan sort
            os.system('cls')
            ll.displayData(sort) #menampilkan hasil sort

        else : #jika key tidak ditemukan
            print("\n- Key tidak tersedia")

    except:
        print("\n- Mohon perhatikan inputan")
    
def searchNimMhs():
    try:
        #melakukan pencarian data berdasarkan nim
        search = str(input("Masukkan NIM yang ingin dicari : "))
        temp_data = ll.searchNIM(search) #melakukan pencarian nim

        if temp_data == False: #jika pencariannya adalah false/tidak ditemukan
            print("\n- NIM tidak ditemukan!")

        else: #jika nim ditemukan
            ll.displayData(temp_data) #menampilkan data hasil pencarian
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

def MenuStaff(): #menjalankan menu-menu staff
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

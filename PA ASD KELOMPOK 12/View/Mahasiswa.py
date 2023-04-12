from Controller.ControllerAccount import Account
from Controller.ControllerUser import User
from Controller.ControllerLinkedList import LinkedList
from View import Staff
import os
import time

acc = Account()
user = User()
ll = LinkedList()

def registrasiMahasiswa(): #fungsi untuk membuat akun mahasiswa
    nim = str(input(">>> Masukan NIM : "))

    if len(nim) == 10:

        if acc.cekNim(nim): #melakukan pencarian nim yang telah diinput ke database
            print("NIM telah terdaftar")
            return False
        
        else : #jika nim tidak ada dalam database maka bisa melakukan registrasi
            nama = str(input(">>> Masukan Nama : ")).capitalize()
            prodi = str(input(">>> Masukan Program Studi : ")).capitalize()

            if 2 < len(nama) < 30 and 2 < len(prodi) < 30:
                jeniskelamin = int(input("""
                1. Perempuan
                2. Laki-laki
                Pilih jenis kelamin anda : """))
                if jeniskelamin == 1:
                    jeniskelamin = "Perempuan"
                elif jeniskelamin == 2:

                    jeniskelamin = "Laki-laki"
                pasw = str(input("\n>>> Masukan Password : "))

                acc.registrasi(nim,nama,prodi,jeniskelamin,pasw) #melakukan proses penambahan data regis ke database
                print("Registrasi berhasil")
                return True
            else :
                print("\n- Panjang karakter nama dan prodi harus diantara 2-30")
    else :
        print("\n- NIM harus terdiri dari 10 angka")

def loginMahasiswa(): 
    global nim_mhs
    nim_mhs = str(input(">>> Masukan NIM : "))
    password = str(input(">>> Masukan Password : "))

    if acc.login(user.find_nim(nim_mhs),password): #melakukan pencarian nim dan password didatabase
        os.system('cls')
        print("Login berhasil")
        print("Halo",user.find_nim(nim_mhs).get("nama")) #mencari nama user berdasarkan nim
        time.sleep(3)
        return True #jika user ditemukan
    
    else :
        return False #jika user tidak ditemukan/password salah
   
def profilMhs(): #menampilkan profil mahasiswa
    acc.profil_mhs(nim_mhs) #mengambil data mahasiswa dari database

def formPeminjamanMhs(kode, tanggal_p, tanggal_s):
    try :
        #mengambil data nim,nama, dan prodi mahasiswa dari database
        nim = user.find_nim(nim_mhs).get("nim")
        nama = user.find_nim(nim_mhs).get("nama")
        prodi = user.find_nim(nim_mhs).get("prodi")

        while True :
            mk = str(input(">>> Mata kuliah : ")).capitalize()
            keperluan = str(input(">>> Keperluan : ")).capitalize()

            if 2 < len(mk) < 30 and 2 < len(keperluan) < 30:
                break
            else:
                print("\n- Panjang karakter mata kuliah dan keperluan harus diantara 2-30")
        
        if mk.isnumeric() or keperluan.isnumeric(): #jika tipenya berupa angka
            print("\n- Input tidak boleh angka")

        elif mk == "" or keperluan == "": #jika inputan kosong
            print("\n- Input tidak boleh kosong")
        else :
            status = "Pending"

            #memasukan data kedalam database
            user.addPengajuanPeminjaman(user.id_peminjaman(), nim, kode, nama, prodi, mk, keperluan, tanggal_p, tanggal_s, status)
    except:
        print("\n- Mohon perhatikan inputan")

def readPeminjaman(): #melihat data peminjaman yang telah dilakukan
    user.readKelasMhs(nim_mhs)

def searchKodeKelas() :
    try :
        search = input("Masukkan Kode Kelas yang ingin dicari : ").capitalize()
        temp_data = ll.searchKelas(search) #proses pencarian data

        if temp_data == False: #jika pencarian false
            print("\n- Kode kelas tidak ditemukan!")

        else:
            ll.hasilSearchKodekelas(temp_data) #jika ditemukan maka akan menampilkan hasil pencariannya
    except:
        print("\n- Mohon perhatikan inputan")

                                                    #MENU - MENU

def menuMahasiswa():
    print("""
            MENU MAHASISWA
✿   ✿   ✿   ✿   ✿   ✿   ✿   ✿   ✿
    1. CREATE PEMINJAMAN
    2. LIHAT PENGAJUAN PEMINJAMAN
    3. DAFTAR KELAS
    4. SEARCH KELAS
    5. PROFIL   
    6. EXIT
✿   ✿   ✿   ✿   ✿   ✿   ✿   ✿   ✿\n""")

def pilihLogin():
    print("""  
      PILIH LOGIN
✿   ✿   ✿   ✿   ✿   ✿
    1. LOGIN
    2. REGISTRASI
    3. EXIT
✿   ✿   ✿   ✿   ✿   ✿\n""")

def MenuMahasiswa(): #menjalankan menu-menu mahasiswa
    os.system('cls')
    while True:
        try :
            pilihLogin()
            pil = int(input("✎ Masukan Pilihan anda : "))
            if pil == 1 :
                os.system('cls')
                if loginMahasiswa(): 
                    while True:
                        try :
                            os.system('cls')
                            menuMahasiswa()
                            pilih = int(input("✎ Masukan pilihan anda : "))
                            if pilih == 1:
                                os.system('cls')
                                Staff.addPeminjaman(nim_mhs)
                                Staff.back()
                            elif pilih == 2:
                                os.system('cls')
                                readPeminjaman()
                                Staff.back()
                            elif pilih == 3:
                                os.system('cls')
                                Staff.readDaftarKelas()
                                Staff.back()
                            elif pilih == 4:
                                os.system('cls')
                                searchKodeKelas()
                                Staff.back()
                            elif pilih == 5:
                                os.system('cls')
                                profilMhs()
                                Staff.back()
                            elif pilih == 6:
                                os.system('cls')
                                break
                            else :
                                print("\n- Pilihan tidak tersedia")
                        except :
                            print("\n- Mohon perhatikan inputan")
                else:
                    time.sleep(3)
                    os.system('cls')
                    continue
            
            elif pil == 2:
                os.system('cls')
                if registrasiMahasiswa():
                    time.sleep(3)
                    os.system('cls')
                    pass
                else :
                    time.sleep(3)
                    continue

            elif pil == 3:
                os.system('cls')
                break

        except:
            print("\n- Mohon perhatikan inputan")

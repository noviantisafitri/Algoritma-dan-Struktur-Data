from Controller.ControllerAccount import Account
from Controller.ControllerUser import User
from View import Staff
import os
import time

acc = Account()
user = User()


def registrasiMahasiswa(): #fungsi untuk membuat akun mahasiswa
    try : 
        nim = str(input("Masukan NIM : "))
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
    except :
        print("Mohon perhatikan inputan")

def loginMahasiswa(): 
    global nim_mhs
    # try :
    nim_mhs = str(input("Masukan NIM : "))
    password = str(input("Masukan Password : "))
    if acc.login(user.find_nim(nim_mhs),password): #melakukan pencarian nim dan password didatabase
        os.system('cls')
        print("Login berhasil")
        print("Halo",user.find_nim(nim_mhs).get("nama"))
        time.sleep(3)
        return True #jika user ditemukan
    else :
        return False #jika user tidak ditemukan/password salah
    # except :
    #     print("Mohon perhatikan inputan")
    
def profilMhs(): #menampilkan profil mahasiswa
    acc.profil_mhs(nim_mhs) #mengambil data mahasiswa dari database

def formPeminjamanMhs(kode, tanggal_p, tanggal_s):
    try :
        nim = user.find_nim(nim_mhs).get("nim")
        nama = user.find_nim(nim_mhs).get("nama")
        prodi = user.find_nim(nim_mhs).get("prodi")
        mk = str(input("Mata kuliah : ")).capitalize()
        keperluan = str(input("Keperluan : ")).capitalize()
        status = "Pending"
    except:
        print("Mohon perhatikan inputan")

    #memasukan data kedalam database
    user.addPengajuanPeminjaman(user.id_peminjaman(), nim, kode, nama, prodi, mk, keperluan, tanggal_p, tanggal_s, status)

def readPeminjaman(): #melihat data peminjaman yang telah dilakukan
    user.readKelasMhs(nim_mhs)

                                                    #MENU - MENU

def menuMahasiswa():
    print("""
         MENU MAHASISWA

    1. CREATE PEMINJAMAN
    2. LIHAT PENGAJUAN PEMINJAMAN
    3. DAFTAR KELAS
    4. SEARCH KELAS
    5. PROFIL
    6. EXIT\n""")

def pilihLogin():
    print("""  
    PILIH LOGIN

    1. LOGIN
    2. REGISTRASI
    3. EXIT\n""")

def MenuMahasiswa():
    os.system('cls')
    while True:
        # try :
            pilihLogin()
            pil = int(input("Masukan Pilihan anda : "))
            if pil == 1 :
                os.system('cls')
                if loginMahasiswa(): 
                    while True:
                        # try :
                            os.system('cls')
                            menuMahasiswa()
                            pilih = int(input("Masukan pilihan anda : "))
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
                                Staff.searchKodeKelas()
                                Staff.back()
                            elif pilih == 5:
                                os.system('cls')
                                profilMhs()
                                Staff.back()
                            elif pilih == 6:
                                break
                            else :
                                print("Pilihan tidak tersedia")
                        # except :
                            print("Mohon perhatikan inputan")
                else:
                    time.sleep(3)
                    continue
            
            elif pil == 2:
                os.system('cls')
                if registrasiMahasiswa():
                    pass
                else :
                    time.sleep(3)
                    continue

            elif pil == 3:
                os.system('cls')
                break

        # except:
        #     print("Mohon perhatikan inputan")
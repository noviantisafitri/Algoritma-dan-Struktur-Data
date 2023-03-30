from View.Account import Main
from View.Admin import MenuAdmin
import os

main = Main()
m = MenuAdmin()
role = int(input("""
                1. Mahasiswa
                2. Staff
                3. EXIT
                Masukan pilihan anda : """))
if role == 1:
    pil = int(input("""
                1. Login
                2. Registrasi
                Pilih : """))
    if pil == 1 :
        os.system('cls')
        main.loginMahasiswa()
    elif pil == 2 :
        os.system('cls')
        main.registrasiMahasiswa()

elif role == 2 :
    os.system('cls')
    # main.loginStaff()
    m.addData()
    


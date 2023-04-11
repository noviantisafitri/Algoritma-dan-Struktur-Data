from View import Staff
from View import Mahasiswa
import os
import time


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
✿   ✿   ✿   ✿   ✿   ✿
    1. MAHASISWA
    2. STAFF
    3. EXIT
✿   ✿   ✿   ✿   ✿   ✿\n""")

def mainProgram():
    os.system('cls')
    welcome()
    time.sleep(3)
    while True:
        try:
            os.system('cls')
            roleUser()
            role = int(input("✎ Masukan pilihan anda : "))
            if role == 1:
                Mahasiswa.MenuMahasiswa()
            elif role == 2 :
                Staff.MenuStaff()
            elif role == 3 :
                 os.system('cls')
                 print("Sedang memproses keluar dari program...")
                 time.sleep(3)
                 os.system('cls')
                 print("--- THANK YOU ---")
                 break
                 
        except:
            print("\n- Mohon perhatikan inputan")

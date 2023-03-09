import os
os.system('cls')

def fibonacciSearch(arr, x): 
    n = len(arr) #panjang array
    fib2 = 0  
    fib1 = 1  
    fib = fib2 + fib1  
  
    # Cari nilai dari fibonacci(n) yang terbesar yang lebih kecil atau sama dengan n
    while fib < n: #nilai fib lebih kecil dari n
        fib2 = fib1  
        fib1 = fib
        fib = fib2 + fib1
  
    # Indeks awal untuk pencarian
    offset = -1
  
    # Melakukan pencarian
    while fib > 1:
        i = min(offset+fib2, n-1)
  
        # Jika x lebih besar daripada nilai elemen pada indeks i, lakukan pencarian pada subarray kanan
        if x > arr[i]:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
  
        # Jika x lebih kecil daripada nilai elemen pada indeks i, lakukan pencarian pada subarray kiri
        elif x < arr[i]:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
  
        # Jika x ditemukan, kembalikan indeks i
        else:
            return i
  
    # Jika elemen tidak ditemukan, kembalikan -1
    if fib1 and arr[offset+1] == x:
        return offset+1
    
    return -1

def jumpSearch(data, x):
    a = len(data) #panjang data
    step = int(a ** 0.5) #jarak lompatan

    #melakukan pencarian
    prev = 0
    while data[min(step, a) - 1] < x: 
        prev = step
        step += int(a ** 0.5)
        if prev >= a :
            return -1
    
    #melakukan pencarian linear untuk mencari x
    while data[prev] < x: 
        prev += 1

        if prev == min(step, a): #jika telah mencapai blok/akhir blok, elemen tidak ada
            return -1

    if data[prev] == x: #jika elemen/data ditemukan
        return prev
    return -1

def binarySearch(data,x):
    start = 0
    end = len(data)-1
    while start <= end:
        mid = (start + end)//2
        if x == data[mid]:
            return mid
        elif x < data[mid]:
            end = mid - 1
        else:
            start = mid + 1

def back (): 
    while True :
        b = input(">>> Tekan enter untuk melakukan searching : ")
        if b == "":
            os.system('cls')
            break
        
while True :
    var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]
    print('\n', var)

    x = str(input("\nMasukan nama yang ingin dicari : ")).capitalize()
    for i in range(len(var)):
        cari = fibonacciSearch(var[i], x)
        #cari = jumpSearch(var[i], x)
        #cari = binarySearch(var[i], x)
        if isinstance (var[i], list): 
            for angka in range(len(var[i])):
                if var[i][angka] == x:
                    print("-"*50)
                    print("\n>>Hasil Search<<\n")
                    print(x,"berada di array index ke -",i,"kolom",cari)
                    print("-"*50)
                    back()     
        else:
            if var[i] == x:
                print("-"*50)
                print("\n>>Hasil Search<<\n")
                print(x,"berada di array index ke -",i)
                print("-"*50)
                back()

import os
from random import randint
os.system('cls')


def quicksort(data):
    if len(data) <= 1: #jika panjang data <=1 maka tidak perlu disort
        return data
    elif len(data) > 1:

        pivot = data[0] #pivot menggunakan index 0
        left = [x for x in data[1:] if x <= pivot] #list left akan menampung data yg lebih kecil
        right = [x for x in data[1:] if x >= pivot] #list right akan menampung data yg lebih besar

        return quicksort(left) + [pivot] + quicksort(right) #memanggil function yang telah dibuat untuk melakukan sort

data =  [randint(0,77) for angka in range(12)] #menggunakan randint untuk mendapatkan angka secara acak
print("Quick Sort")
print("Sebelum disort", data)
hasil = quicksort(data)
print("Setelah disort", hasil)
print("="*100)

def mergesort(data):
    if len(data) > 1:
        mid = len(data) // 2 #membagi data menjadi 2 bagian
        left = data[:mid] #data dari awal hingga ke tengah
        right = data[mid:] #data dari tengah hingga ke akhir

        mergesort(left) #melakukan sort
        mergesort(right)
        
        i=j=k= 0 #inisiasi, index dimulai dari 0

        while i < len(left) and j < len(right): 
            if left[i] < right[j]: #jika data kiri lebih kecil dari kanan
                data[k] = left[i] #data ditampung dikiri
                i += 1
            else :
                data[k] = right[j] #data ditampung dikanan
                j +=1
            k +=1

        while i < len(left):
            data[k] = left[i]
            i += 1
            k +=1
 
        while j < len(right):
            data[k] = right[j]
            j +=1
            k +=1

data =  [randint(0,84) for angka in range(12)]
print("Merge Sort")
print("Sebelum disort", data)
hasil = mergesort(data)
print("Setelah disort", data)
print("="*100)

def shellsort(data):
    n = len (data)
    gap = n // 2 #untuk membandingkan data
    
    #melakukan pengurutan data
    while gap > 0:
        for i in range (gap, n):
            temp = data[i] #data dalam list
            j=i
            while j >= gap and data [j-gap] > temp:
                data[j] = data[j-gap]
                j -= gap 
            data [j] = temp
        gap //= 2 #gap diperkecil lagi

    return data

data = [randint(0,184) for angka in range(12)]
print("Shell Sort")
print("Sebelum disort", data)
hasil = shellsort(data)
print("Setelah disort", data)
print("="*100)
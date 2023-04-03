import os
os.system('cls')

def mergesort(angka):
    if len(angka) > 1 :
        mid = len(angka)//2
        atas = angka[:mid]
        bawah = angka [mid:]

        mergesort(atas)
        mergesort(bawah)
        i = j = k = 0
        while i < len(atas) and j < len(bawah):
            if atas[i] < bawah [j]:
                angka[k] = atas[i]
                i = i + 1
            else :
                angka[k] = bawah[j]
                j =j + 1
            k = k+1

        while i < len(atas):
            angka[k] = atas[i]
            i = i+1
            k = k+1

        while j < len(bawah):
            angka[k] = bawah[j]
            j = j+1
            k = k+1
    return angka
    
def pisah(listku): 
    pisahkan = [] 
    for i in listku: 
        if isinstance(i, list):
            pisahkan.extend(pisah(i))
        else: 
            pisahkan.append(int(i)) 
    return pisahkan

variable = [12, 1, [22, 3, [8, 14]], 2, 6, [11], 90]

print("Merge Sort")
print("Sebelum = ",variable) 
pisahkan = pisah(variable) 
print("Setelah dipisah = ",pisahkan) 
sort = mergesort(pisahkan)
print("Setelah disorting =", sort)
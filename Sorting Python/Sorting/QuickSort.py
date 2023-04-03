import os
os.system('cls')

def QuickSort(data):
    if len(data) <= 1:
        return data
  
    pivot = data[0]
    left = [x for x in data if x < pivot]
    right = [x for x in data if x > pivot]
  
    return QuickSort(left) + [pivot] + QuickSort(right)
  
def pisah(listku):
    list2 = []
    for pivot in listku:
        if isinstance(pivot, list):
            for i in pivot:
                if type(i) == int:
                    list2.append(i)
                if isinstance(i, list) :
                    for angka in i:
                        if type(angka) == list:
                            list2.append(angka)
                        else:
                            list2.append(angka)
        else:
            list2.append(pivot)
    return list2

variable = [12, 1, [22, 3, [8, 14]], 2, 6, [11], 90] 

print("Quick Sort")
print("Sebelum Sort :",variable)
pisahkan = pisah(variable)
hasil = QuickSort(pisahkan)
print("Setelah Sort :",hasil)

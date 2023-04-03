import os
os.system('cls')

def jumpSearch(listt, x):
    a = len(listt)
    step = int(a ** 0.5)

    prev = 0
    while listt[min(step, a) - 1] < x:
        prev = step
        step += int(a ** 0.5)
        if prev >= a :
            return -1
    
    while listt[prev] < x:
        prev += 1

        if prev == min(step, a):
            return -1

    if listt[prev] == x:
        return prev
    return -1

Dataset = ['daiva', 'zaki', ['wahyu', 'zaki'], 'shafa', ['zaki', 'aji', 'wahyu'], 'zaki']
x = 'zaki'

for i in range(len(Dataset)):
    if type(Dataset[i]) == list:
        cari = jumpSearch(Dataset[i],x)
        cari += 1 #kolom dimulai dari 1
        if cari != -1:
            print(x,"berada di array index ke -",i,"kolom",cari)
    else:
        if Dataset[i] == x:
            print(x,"berada di array index ke -",i)


# OUTPUT
# zaki berada di array index ke - 1        
# zaki berada di array index ke - 2 kolom 2
# zaki berada di array index ke - 4 kolom 1
# zaki berada di array index ke - 5  
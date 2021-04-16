from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def mans_minejums():
    minejums = ""
    while minejums not in ["1","2","3"]:
        minejums = input("Izvēlies skaitli - 1, 2, 3: ")
    return int(minejums)

def parbaudi_minejumu(lists,minejums):
    if lists[minejums-1] == "o":
        print("Pareizi🎉") 
    else:
        print ("Nepareizi😒")
        print(lists)

#pa soļiem izsauc visas funkcijas
#norāda sarakstu
mylist = [" ", "o", " "]

#sajauc sarakstu
sajaukts_saraksts = shuffle_list(mylist)

#spēlētāja minējums
speletaja_minejums = mans_minejums()

#pārbauda spēlētāja minējumu
parbaudi_minejumu(sajaukts_saraksts, speletaja_minejums)
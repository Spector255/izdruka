#vienkārši piepildīt list ar elementiem
saraksts = list(range(0, 11, 2))  #izdrūka massīvu kurā ir ielikti pāra skaitļi no 0 līdz 11
print(saraksts)
print("========================")

#enumerate - parāda indeksus tuple formā
vards = "banans"
for i in enumerate(vards):
    print(i)
print("========================")

#atpakajot tuples
vards = "banans"
for indekss, burts in enumerate(vards):
    print(indekss, burts)
    print()
    '''
    print (indekss)
    print(burts)
    print("\n")
    '''
print("========================")

#izmanto zip - sapako vairākus list kopā kā tuple
mylist1 = [1, 2, 3]
mylist2 = ["a", "b", "c"]
for i in zip(mylist1, mylist2):
    print(i)

mylist3 = [100,200,300,400]  #ignorē 4. elementu
for i in zip(mylist1, mylist2, mylist3):
    print(i)
print("========================")

#izmanto in, lai noskaidrotu vai objektā atrodams meklētais elements
print("x" in [1,2,3])
print("x" in [1,2,3,"x"])
print(2 in [1,2,3])
print("a" in "banans")
print("mykey" in {"mykey":345})
d = {"mykey":345}
print(345 in d.keys())
print(345 in d.values())
print("========================")

#min un max
mylist = [10,20,30,40,50,60,70,80,90,100]
print(min(mylist))
print(max(mylist))
print(min(mylist2))
print(max(mylist2))
print("========================")

#bibliotēku importēšana
#random - nejaušs, gadījuma skaitlis
from random import shuffle
mylist = [1,2,3,4,5,6,7,8,9,10]
print(mylist)
shuffle(mylist)
print(mylist)
mylist2 = ["a", "b", "c"]
print(mylist2)
shuffle(mylist2)
print(mylist2)
print("========================")

from random import randint
skaitlis = randint(0,100)
print(skaitlis)
skaitlis = randint(-100,0)
print(skaitlis)
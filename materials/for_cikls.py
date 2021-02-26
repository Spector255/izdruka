#iterācija - kādas darbības atkārtota izpildīšana
mainigais = [1, 2, 3]
for elements in mainigais:
    print(elements)  #darbības, kas jāveic

#drukā list elemntus
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # ,"a","b","c","d"
for sk in myList:
    print(sk)

for sk in myList:
    print(f"{sk} Sveiki!")  #var nerakstīt cikla mainīga nosaukumu

#izdrukā tikai pāra skaitļus
for sk in myList:
    if sk % 2 == 0:
        print(sk)
    else:
        print(f"Nepāra skaitlis: {sk}")

#summas aprēķināšana
summa = 0

for sk in myList:
    summa = summa + sk
    print(f"Pēc {sk} sakitļu saskaitīšanas summa ir {summa}")

print(summa)

#Drukā tekstu
abcd = "Hello world!"
for abc in abcd:
    print(abc)

for burts in "programma":
    print(burts, end="  ")

print()

#drukā tuple
tup = (1,2,3,4)
for elements in tup:
    print(elements)

mylist = [(1,2),(3,4),(5,6),(7,8)] #packed tuple
print(len(mylist))

print("=====")

for elements in mylist:
    print(elements)

print("=====")

for (a,b) in mylist:    #atpako tuple
    print(a)
    print(b)
    print(a,b)

print("=====")

for a,b in mylist:  #var nelikt iekavas
    print(a)
    print(b)

print("=====")

new = [(1,2,3),(4,5,6),(7,8,9)]

for (a,b,c) in new:    #atpako tuple
    print(b)

print("=====")

#vārdnīcas
d = {"k1":11, "k2":12, "k3": 13}
for elem in d:
    print(elem) #izdrukā tikai atslēgas

print("=====")

for elem in d.items():
    print(elem) #drukā pārus

print("=====")

for (elem,bcd) in d.items():
    print(elem)
    print(bcd)

#ar skaitļiem izmanto funkciju ()

cipars = int(input("Ievadiet skaitli: "))

for i in range (cipars): #izdrukā visus skaitļus no intervāla [0;cipars)
    print (i)

for i in range (cipars +1): #izdrukā visus skaitļus no intervāla [0;cipars]
    print (i)

for i in range (5,cipars): #izdrukā visus skaitļus no intervāla [5;cipars)
    print (i)

for i in range (5,cipars+1): #izdrukā visus skaitļus no intervāla [5;cipars]
    print (i)

for i in range (5,cipars+1, 2): #izdrukā katro otrū skaitļu no intervāla [5;cipars]
    print (i)
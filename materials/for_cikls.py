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
    print (burts, end = "  ")
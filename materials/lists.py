#lists jeb saraksti
#a = ['Sveika', 100, 'tu', '3.59', 'skaista!', [1,26]]
myList = [1, 2, 3, 'tu', '3.59', 'skaista!', [1, 26]]
print(myList[6][0])
print(myList)
print(len(myList))  #saraksta garums

my_list = ["viens", "divi", "trīs", 'četri']
print(my_list)
print(len(my_list))  #saraksta garums
print(my_list[0])  #izdrukā pirmo elementu (ar 0 indeksu)
print(my_list[1:]
      )  #izdrukā no noradīta elementa līdz beigam == print(my_list[1:4])
print(my_list[2:3])

#sarakstu apvienošana jeb konkatinācija
#print(myList + my_list)
cits_list = ["pieci", "seši"]
print(my_list + cits_list)  #izdrukā sarakstu ar abu mainīgo
jauns_list = my_list + cits_list
print(jauns_list)

#sarakstu mainīšana
jauns_list[0] = 1
print(jauns_list)

jauns_list.append("astoņi")  #pievieno pēdejo elementu
print(jauns_list)

jauns_list.insert(
    -1, "septiņi"
)  #pievieno elementu pirms noradītam indeksam == jauns_list.insert (6, "septiņi")
print(jauns_list)

jauns_list.pop()  #noņem nost elementu noradīto indeksu (š.s. pēdejo)
print(jauns_list)

pop_elem = jauns_list.pop(
    2)  #Izņem elementu, bet tas valuable piešķir variable (mainīgai)
print(pop_elem)

#elementu kārtošana
new_list = ['b', 'a', 'd', 'z', 'e']
num_list = [4, 1, 8, 3, 0]

print(new_list)  #nesakartots saraksts
new_list.sort()  #sakartojam sarakstu
print(new_list)  #nesakartojam sarakstu

print(num_list)
num_list.reverse()  #apgriež pretēja virziena
print(num_list)
num_list.sort()
print(num_list)

num_list.reverse()  #sakarto otrādi
print(num_list)

myList = [
    1,
    2,
    3,
    100,
    3.59,
]
myList.sort()
print(myList)

#saraksts sarakstā (nested)
nestedList = [1, 5, [7, 2]]
print(nestedList[1])
print(len(nestedList))
print(nestedList[2][1])

augli = ["ābols", "banāns", "gurķis"]
print(augli[2])
#aizstāt elementu - gurķis -> apelsīns
augli[2] = "apēlsins"
print(augli)

augli.append("bumbieris")  #pievieno pēdejo elementu
print(augli)

augli.insert(2, "citrons")
print(augli)

augli.pop(1)
print(augli)

print(f"Sarakstā mums ir {len(augli)} dažādi augļi.")
augli.sort()
print(augli)
#Izveido programmu, kas aprēķina un izdrukā dotā saraksta myList = [5, 7, 6, 8, 25, -4, 3] summu. Ņem vērā, ka programmai jādarbojas korekti arī tad, ja sarakstu papildina vai maina. 
myList = [5, 7, 6, 8, 25, -4, 3]
rez = 0
for i in range (len(myList)):
    rez += myList[i]
print(rez)
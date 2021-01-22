#[sākums:beigas:solis]
myString = "Sveiki, pasaule"
print(myString)
print(myString[0])  #Izdrukā 1. simbolu
print(myString[6])  #Izdrukā 7. simbolu
print(myString[6:0:-1])

#[sākums:beigas:solis]
myString = "Sveiki, pasaule!"
print(myString)
print(myString[0])  #Izdrukā 1. simbolu
print(myString[6])  #Izdrukā 7. simbolu
print(myString[-1])  #Izdrukā pēdejo simbolu
print(myString[13])  #Izdrukā 14. simbolu
print(myString[-3])  #Izdrukā 14. simbolu
print(myString[6:0:-1])

myString = "abcdefghijklmnoprstuvz"
print(myString)
print(len(myString))
print(myString[2])  #Izdrukā C
print(myString[2:])  #izdrukā visu, sākot no c
print(myString[:3])  #izdrukā visu, līdz 3. indeksam neieskaitot
print(myString[3:6]) #izdrukā no 3 līdz 6. indeksam neieskaitot
print(myString[::]) #izdrukā visu
print(myString[::3]) #izdrukā katru trešo elementu
print(myString [2:7:2]) #izdrukā katru otro elementu no 2. līdz 7. elementam (neieskaitot)
print(myString [::-1]) #izdrukā visu no otra gala
print(myString [::-2]) #izdrukā visu no otra gala, katru otro elementu
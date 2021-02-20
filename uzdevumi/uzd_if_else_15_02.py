a = 15
b = 2.5
c = 4.78
######################################
if a > b and a > c:
    print("a ir vislielākais skaitlis")
    if b > c:
        print("c ir vismazākais")
    else:
        print("b ir vismazākais")
elif b > a and b > c:
    print("b ir vislielākais skaitlis")
    if a > c:
        print("c ir vismazākais")
    else:
        print("a ir vismazākais")
else:
    print("c ir vislielākais skaitlis")
    if a > b:
        print("b ir vismazākais")
    else:
        print("a ir vismazākais")
######################################
x = [a, b, c]
print("Maksimālais skaitlis: ", max(x))
print("Minimālais skaitlis: ", min(x))
######################################
temp = float(input("Ievadiet ķermeņa temperatūra: "))
if temp < 35.0:
    print("Vai nav par aukstu?")
elif temp >= 35.0 and temp <= 37.0:
    print("Viss kārtībā!")
else:
    print("Iespējams drudzis!")
######################################
#Bonus :) 
a = int(input("Ievadiet pirmo skaitli: "))
b = int(input("Ievadiet otro skaitli: "))
c = int(input("Ievadiet trešo skaitli: "))
if a >= b and a >= c:
    if b >= c:
        print(c, b, a)
    else:
        print(b, c, a)
elif b >= a and b >= c:
    if a >= c:
        print(c, a, b)
    else:
        print(a, c, b)
elif c >= a and c >= b:
    if b >= a:
        print(a, b, c)
    else:
        print(b, a, c)
######################################
#Firma darbiniekiem apsolījusi Ziemassvētku piemaksu 15% apjomā no mēneša algas par KATRU nostrādāto gadu virs 2 gadiem.#
#Uzdevums. Izveido programmu, kas lietotājam pajautā mēneša algas apjomu un nostrādāto gadu skaitu, bet pēc tam aprēķina un izvada piemaksas lielumu. 
#Piemērs: Ja ir 5 gadu stāžs un 1000 eiro alga, tad piemaksa būs 450 eiro. 
alga = float(input("Ievadiet savu algu: "))
gads = int(input("Ievadiet stāžu: "))
if gads <= 2:
    print("Jūms nav piemaksas")
else:
    stazs = gads - 2
    piemaksa = ((alga/100)*15)*stazs
    print(f"Jūsu piemaksa ir {piemaksa} eiro")
######################################

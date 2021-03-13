#Uzraksti programmu, kura prasīs lietotājam ievadīt veselus nenegatīvus skaitļus (kāmēr nav 0), pievienos tos sarakstam un izvādis skaitļu skaitu, kas ir lielāki par savu nākamo kaimiņu.
skaits = 0
a = 0
mylist = []
while True:
    n = int(input("Ievadi veselu nenegatīvu skaitli: "))
    if a > n:
        skaits += 1
    a = n
    mylist.append(n)
    if n == 0:
        break
print(
    f"Skaitļu virknē {mylist} ir {skaits} skaitļi, kas ir lielāki par savu nākamo kaimiņu."
)
#############################
skaits = 0
a = 0
mylist = []
while n>=0:
    n = int(input("Ievadi veselu nenegatīvu skaitli: "))
    if a > n:
        skaits += 1
    a = n
    mylist.append(n)
    if n == 0:
        break
print(
    f"Skaitļu virknē {mylist} ir {skaits} skaitļi, kas ir lielāki par savu nākamo kaimiņu."
)

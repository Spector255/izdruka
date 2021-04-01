def saskaiti_skaitlus(pirmais, otrais):
   summa = pirmais + otrais
   return (summa)

rez1 = saskaiti_skaitlus(2,3)
rez2 = saskaiti_skaitlus(25.2,3.658)
rez3 = saskaiti_skaitlus(3.2,13)
print(rez1 * rez2 + rez3)

#pārbauda vai ir pāra saskaiti_skaitlus
def parbaude(skaitlis):
    return skaitlis % 2 == 0

if (parbaude(5)) == True:
    print("Tas ir pāra skitlis")
else:
    print("Tas nav pāra skaitlis")

if (parbaude(48)) == True:
    print("Tas ir pāra skitlis")
else:
    print("Tas nav pāra skaitlis")

#atgriezīs true, ja sarakstā atrodāms kaut viens pāra skaitlis
def parbaude2(saraksts):
    for skaitlis in saraksts:
        if skaitlis % 2 == 0:
            return True

print(parbaude2([1,2,3,4,5,6,7,8,9]))
print(parbaude2([1,3,5,7,9]))
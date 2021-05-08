#Lietotājs ievada divus vārdus, funkcija pārbauda kurā vārdā ir vairāk burtu, un par cik burtu ir vairāk.
def salidz(pirmais, otrais):
    if (len(pirmais)) > (len(otrais)):
        print(f"Pirmais vārds ({pirmais}) ir garāk nēka otrais({otrais}) uz {len(pirmais)-len(otrais)} burtu/burtiem")
    elif (len(otrais)) > (len(pirmais)):
        print(f"Otrais vārds ({otrais}) ir garāk nēka pirmais({pirmais}) uz {len(otrais)-len(pirmais)} burtu/burtiem")
    else:
          print(f"Vārds {pirmais} ir tik garš, kā {otrais}")

pirmais = input("Ievadiet 1. vārdu: ")
otrais = input("Ievadiet 2. vārdu: ")

salidz(pirmais,otrais)

print("###################")
def saraksta_izdruka(mlist):
    if mlist[0]>mlist[-1]:
        print(mlist[::-1])
    elif mlist[-1]>mlist[0]:
        print(mlist)
    else:
        print("Pirmais un pēdējais cipari ir vienādi")

saraksta_izdruka([1,2,3,4,5,6,7,8,9])
saraksta_izdruka([1,2,3,4,5,6,7,8,9,0])

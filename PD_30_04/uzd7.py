#Uzraksti funkcija, kuru aprēķina x sekojošās vienādībās: ax+b=0 vai arī ax-b=0. Lietotājs ievada a, b un zīmi
def vienadojums(a,b,zime):
    if zime == "+":
        neg=0-b
        rez=neg/a
        return rez
    elif zime == "-":
        if b<0:
            rez = b/a
            return rez
        rez = abs(b)/a
        return rez
    else:
        return("Error, invalid symbol")

print(vienadojums (2,3,"+")) #-1.5
print(vienadojums (2,3,"-")) #1.5
print(vienadojums (2,3,"p")) #error
print(vienadojums (4,5,"+")) #-1.25
print("=====")
print(vienadojums (1,3,"+")) #-3
print(vienadojums (-1,3,"+")) #3
print(vienadojums (1,-3,"+")) #3
print(vienadojums (-1,-3,"+")) #-3
print(vienadojums (1,3,"-")) #3
print(vienadojums (-1,3,"-")) #-3
print(vienadojums (1,-3,"-")) #-3
print(vienadojums (-1,-3,"-")) #3
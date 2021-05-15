#pip install --upgrade pip
#pip install PyYAML

from turtle import*
from random_word import RandomWords
r = RandomWords()

#right(90) #Pagrieziens pa labi uz 90 grādiem
#forward(20) #Parvietošana pa taisni uz 20 soliem
#write('S') #raksta burtu "S"
#pu() #paceļam pildspalvu, pēc tiem robots vairs nezīmes, kāmer netiks uzrakstits pd()
#right(90)
#forward (30)
#print(position())
#print(xcor())
#print(ycor())

def karatavas_zimejums(garums):
    #hideturtle()
    pu()
    setposition(-150,20)
    left(90)
    pd()
    forward(100)
    right(90)
    forward(100)
    right(90) 
    forward(20) #(-50; 100)
    pu()
    svitras_lielums = 300/(garums*2)
    setposition(-150,-50)
    left (90)
    svitr = 0
    while svitr != garums:
        pd()
        forward(svitras_lielums)
        pu()
        forward(svitras_lielums)
        svitr += 1
    right (90)    

def pareizi_viens(vards, burts):
    garums = len(vards)
    svitras_lielums = 300/(garums*2)
    indekss = vards.index(burts) +1
    pu()
    setx((svitras_lielums*2)*indekss)
    pd()
    write(burts)
    return("Pareizi")

def pareizi_daudz(vards, burts):
    garums = len(vards)
    svitras_lielums = 300/(garums*2)
    final=""
    c = 0
    i = 0
    while c != burtu_skaits: 
            while vards[i] != burts:
                i += 1
            indekss = vards.index(burts) +1
            pu()
            setposition(-150,-40)
            setx((svitras_lielums*2)*indekss)
            pd()
            write(burts)
            vards =  vards[:i] + vards[i+1:]
            i += 1
            c += 1
    

def nepareizi(kludas):
    if kludas == 1:
        pu()
        setposition(-60,90)
        pd()
        circle(10)
        pu()
        print("Nepareizi")
        return True
    elif kludas == 2:
        pu()
        setposition(-50,80)
        pd()
        forward(25) #(-50,55)
        pu()
        print("Nepareizi")
        return True
    elif kludas == 3:
        pu()
        setposition(-50,55)
        pd()
        right(45)
        forward(15)
        pu()
        left(45)
        print("Nepareizi")
        return True
    elif kludas == 4:
        pu()
        setposition(-50,55)
        pd()
        left(45)
        forward(15)
        pu()
        right(45)
        print("Nepareizi")
        return True
    elif kludas == 5:
        pu()
        setposition(-50,55+12.5)
        pd()
        right (30)
        forward(15)
        pu()
        left(30)
        print("Nepareizi")
        return True
    elif kludas == 6:
        pu()
        setposition(-50,55+12.5)
        pd()
        left (30)
        forward(15)
        pu()
        right(30)
        print("Game Over")
        return False

vards = r.get_random_word().upper()
print(vards)
kludas = 0
pareizas = 0
garums = len(vards)
print(garums)
karatavas_zimejums(garums)

while pareizas < garums:
    burts = input(("Ievadiet burtu: ")).upper()
    if burts in vards:
        burtu_skaits = vards.count(burts)
        if burtu_skaits > 1:
            pareizi_daudz(vards, burts)
            pareizas += burtu_skaits
        else:
            pareizi_viens(vards, burts)
            pareizas += 1
    else:
        kludas += 1
        if nepareizi(kludas) == False:
            break
    
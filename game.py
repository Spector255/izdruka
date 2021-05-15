#pip install --upgrade pip
#pip install PyYAML

from turtle import *
from random_word import RandomWords

r = RandomWords()


def karatavas_zimejums(garums):
    hideturtle()
    pu()
    setposition(-150, 20)
    left(90)
    pd()
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(20)  #(-50; 100)
    pu()
    svitras_lielums = 300 / (garums * 2)
    setposition(-150, -50)
    left(90)
    svitr = 0
    while svitr != garums:
        pd()
        forward(svitras_lielums)
        pu()
        forward(svitras_lielums)
        svitr += 1
    right(90)


def pareizi_viens(vards, burts):
    garums = len(vards)
    svitras_lielums = 300 / (garums * 2)
    loc = 0
    indekss = vards.index(burts)
    pu()
    setposition(-150, -45)
    left(90)
    while loc != indekss:
        forward(svitras_lielums * 2)
        loc += 1
    right(90)
    pd()
    write(burts)


def pareizi_daudz(vards, burts, skaits):
    garums = len(vards)
    svitras_lielums = 300 / (garums * 2)
    final = ""
    c = 0
    for i in range(garums):
        if vards[i] == burts:
            pu()
            setposition(-150, -45)
            left(90)
            loc = 0
            while loc != i:
                forward(svitras_lielums * 2)
                loc += 1
            right(90)
            pd()
            write(burts)


def nepareizi(kludas):
    if kludas == 1:
        pu()
        setposition(-60, 90)
        pd()
        circle(10)
        pu()
        return True
    elif kludas == 2:
        pu()
        setposition(-50, 80)
        pd()
        forward(25)  #(-50,55)
        pu()
        return True
    elif kludas == 3:
        pu()
        setposition(-50, 55)
        pd()
        right(45)
        forward(15)
        pu()
        left(45)
        return True
    elif kludas == 4:
        pu()
        setposition(-50, 55)
        pd()
        left(45)
        forward(15)
        pu()
        right(45)
        return True
    elif kludas == 5:
        pu()
        setposition(-50, 55 + 12.5)
        pd()
        right(30)
        forward(15)
        pu()
        left(30)
        return True
    elif kludas == 6:
        pu()
        setposition(-50, 55 + 12.5)
        pd()
        left(30)
        forward(15)
        pu()
        right(30)
        print("Game Over")
        print(f"Pareizs vārds bija - {vards}")
        return False


vards = r.get_random_word().upper()
kludas = 0
pareizas = 0
garums = len(vards)
karatavas_zimejums(garums)
answers = []

while pareizas < garums:
    burts = input(("Ievadiet burtu: ")).upper()
    if burts in answers:
        print("Šis burts jau bija")
    else:
        if burts == "ADMIN":
            print(vards)
            print(garums)
            print(answers)
        elif burts in vards:
            answers.append(burts)
            burtu_skaits = vards.count(burts)
            if burtu_skaits > 1:
                pareizi_daudz(vards, burts, burtu_skaits)
                ("Pareizi!")
                pareizas += burtu_skaits
            else:
                pareizi_viens(vards, burts)
                ("Pareizi!")
                pareizas += 1
            if pareizas == garums:
                print("Apsveicam!")
        else:
            answers.append(burts)
            kludas += 1
            print("Nepareizi!")
            if nepareizi(kludas) == False:
                break

#pip install PyYAML
#pip install random-word

from turtle import*
from random_word import RandomWords
r = RandomWords()

#right(90) #Pagrieziens pa labi uz 90 grādiem
#forward(20) #Parvietošana pa taisni uz 20 soliem
#write('S') #raksta burtu "S"
#pu() #paceļam pildspalvu, pēc tiem robots vairs nezīmes, kāmer netiks uzrakstits pd()
#right(90)
#forward (30)
#print(xcor())
#print(ycor())

def karatavas_zimejums():
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

karatavas_zimejums()
vards = r.get_random_word()
vards = vards.upper()
print(vards)
kludas = 0
pareizas = 0
garums = (len(vards))

while pareizas != garums or kludas != garums:
    burts = input(("Ievadiet burtu: ")).upper()
    
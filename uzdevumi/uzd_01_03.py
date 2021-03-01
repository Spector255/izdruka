sakums = int(input("Ievadiet intervālu sākumu: "))
beigums = int(input("Ievadiet intervālu gālu: "))
while beigums<sakums:
    if beigums<sakums:
        print ("Nekorēkti dati")
        sakums = int(input("Ievadiet intervālu sākumu: "))
        beigums = int(input("Ievadiet intervālu gālu: ")) 
for i in range (sakums, beigums+1): 
    print (i)
print("##################################")
##########################################
skaitlis = int(input("Ievadiet skaitli: "))
faktorials = 1

for i in range (skaitlis):
    faktorials = faktorials*(skaitlis-i)
print(faktorials)
print("##################################")
##########################################
sakums = int(input("Ievadiet intervālu sākumu: "))
beigums = int(input("Ievadiet intervālu gālu: "))
dalskaitlis = int(input("Ievadiet skaitli, ar kuru jādals cipariem Jūsu intervāla parbaudīt: "))
while beigums<sakums:
    if beigums<sakums:
        print ("Nekorēkti dati")
        sakums = int(input("Ievadiet intervālu sākumu: "))
        beigums = int(input("Ievadiet intervālu gālu: ")) 
for i in range (sakums, beigums+1): 
    if i % dalskaitlis == 0:
        print (i)
print("##################################")
##########################################
rindas = int(input("Ievadiet rindas skaitu: "))
while rindas>9:
    if rindas>9:
        print ("Nekorēkti dati")
        rindas = int(input("Ievadiet rindas skaitu: "))
startr=1
stri=""
for startr in range (startr,rindas+1):
   stri = stri + str(startr)
   print (stri)
print("##################################")
##########################################
abc = [0,1]
while (abc[-1]+abc[-2]<=100):
    b1 = abc[-1]
    b2 = abc[-2]
    if b1+b2 <= 100:
         abc.append(b1+b2)
print (abc)

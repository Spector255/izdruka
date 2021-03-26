mylist = [x for x in range(0, 11)]
print(mylist)

mylist = [x**2 for x in range(0, 11)]
print(mylist)

print("=======================================================")

mylist2=[]

for i in range (11):
    mylist2.append(i)
print(mylist2)

for i in range(len(mylist2)):
    mylist2[i]
    mylist2[i] = mylist2[i]**2
print(mylist2)

print("=======================================================")

mylist3=[]

skaitlis=int(input("Ievadiet līdz kurām skaitļim jākapina: "))
pakape=int(input("Ievadiet pakape: "))

for i in range (skaitlis):
    mylist3.append(i)
print(mylist3)

for i in range(len(mylist3)):
    mylist3[i]
    mylist3[i] = mylist3[i]**pakape
print(mylist3)

print("=======================================================")

#5. grupa
#nested lists
#
#mylist=[]
#for x in [2,4,6]:
#    for y in [1,10,1000]:
#        mylist.append(x*y)
#print(mylist)
#
#mylist2 = [x*y for x in [2,4,6] for y in [1,10,1000]]
#print(mylist2)
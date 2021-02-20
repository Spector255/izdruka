print("Hello world!") 

i=1
while i<=5:
    print("Sveiki!") 
    i += 1 #i=i+1
print ("i tagad ir", i)

j = 0

while j<5:
    print("Nr.",j)
    j += 1

while i>0:
    print("skaitām atpakaļ",i)
    i -= 1

# ar soli 2
i = 20
while True:
    if i > 26:
        break
    print("i ir", i)
    i += 2
########################
augstums = int(input("Eglītes augstumu: "))
z=augstums-1
x=1
for i in range(0,augstums):
    for i in range(0,z):
        print(' ',end='')
    for i in range(0,x):
        print('*',end='')
    for i in range(0,z):
        print(' ',end='')
    x=x+2
    z=z-1
    print()
########################
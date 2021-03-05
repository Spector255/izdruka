#############1. uzd####################
neparaskaitlis = int(input("Ievadiet skaitli: "))
sakums = 1
while sakums != neparaskaitlis + 1:
    if sakums % 2 != 0:
        print(sakums, end=" ")
        sakums += 1
    else:
        sakums += 1
print()
print("##################################")
#############2. uzd####################
Askaitlis = int(input("Ievadiet A skaitli: "))
Bskaitlis = int(input("Ievadiet B skaitli: "))
if Askaitlis < Bskaitlis:
    while Askaitlis != Bskaitlis + 1:
        print(Askaitlis)
        Askaitlis += 1
else:
    while Askaitlis != Bskaitlis - 1:
        print(Askaitlis)
        Askaitlis -= 1
print("##################################")
#############3. uzd####################
paraskaitlis = int(input("Ievadiet skaitli: "))
while paraskaitlis != -1:
    if paraskaitlis % 2 == 0:
        print(paraskaitlis, end=" ")
        paraskaitlis -= 1
    else:
        paraskaitlis -= 1
print()
print("##################################")
#############4. uzd####################
ievade = 0.0
Mylist = []
for i in range(10):
    ievade = float(input(f"Ievadiet {i+1}. skaitli: "))
    Mylist.append(ievade)
print(Mylist)
print("##################################")
#############5. uzd####################
skaitlis = int(input("Ievadiet skaitli: "))
while skaitlis < 0:
    print("Nekorēkti dati")  #
    skaitlis = int(input("Ievadiet skaitli, kurš ir vienāds ar 2 vai lielāk:"))
cipars = 1
pakape = 1
rezultats = 0
while rezultats <= skaitlis:
    rezultats = pakape * pakape
    if rezultats > skaitlis:
        break
    print(rezultats, end=" ")
    pakape += 1
print()
print("##################################")
#############6. uzd####################
skaitlis = int(input("Ievadiet skaitli, kurš ir vienāds ar 2 vai lielāk: "))
while skaitlis < 2:
    print("Nekorēkti dati, es taču pateicu LIELĀK!!!")  #:)
    skaitlis = int(input("Ievadiet skaitli, kurš ir vienāds ar 2 vai lielāk:"))
atlikums = 1
dalitajs = 2
while atlikums != 0:
    if skaitlis % dalitajs != 0:
        dalitajs += 1
    else:
        atlikums = 0
print(f"{skaitlis} dalās ar {dalitajs} bez atlikuma")
print("##################################")
#############7. uzd####################
rindas = int(input("Ievadiet rindas skaitu: "))
while rindas > 9:
    print("Nekorēkti dati")
    rindas = int(input("Ievadiet rindas skaitu: "))
startr = 1
stri = ""
for startr in range(startr, rindas + 1):
    stri = stri + str(startr)
    print(stri)
print("##################################")
#############8. uzd####################
abc = [0, 1]
while (abc[-1] + abc[-2] <= 100):
    b1 = abc[-1]
    b2 = abc[-2]
    if b1 + b2 <= 100:
        abc.append(b1 + b2)
print(abc)

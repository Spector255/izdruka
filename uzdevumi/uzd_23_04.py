def otraislielais(virkne):
    mylist=list(virkne)
    rez = ""
    for i in range (len(mylist)):
        if i%2!=0:
            rez += str(mylist[i]).upper()
        else:
            rez += str(mylist[i]).lower()
    return rez

print(otraislielais("Ieraksts"))
print("#########################################")
def visivvardi(virkne):
    mylist = virkne.split(' ', maxsplit=-1)
    for i in range (len(mylist)):
        konv = str(mylist[i])
        if konv[0] == 'v' or konv[0] == 'V' :
            print (konv)

visivvardi("Izdrukā visus vārdus, kas sākas ar v burtu")
print("#########################################")

def salidzinasana(virkne):
    mylist = virkne.split(' ', maxsplit=1)
    for i in range (len(mylist)):
        konv = str(mylist[i]).lower()
        konv2 = str(mylist[i+1]).lower()
        if konv[0] == konv2[0]:
            return True
        else:
            return False

print(salidzinasana("Balts balodis"))
print(salidzinasana("Zila vista"))
print("#########################################")

def maina(vards):
    mylist=list(vards)
    pirm=mylist[0]
    beig=mylist[-1]
    mylist[0]=beig
    mylist[-1]=pirm
    rez=""
    for i in range (len(mylist)):
        rez=rez + str(mylist[i])
    return rez

print(maina("code"))
print(maina("a"))
print(maina("ab"))
#args (arguments) - atgriež tuple no funkcijam 
def myfunc(a,b,c,d=0,e=0,):
    #atgriež 5% no a un b summas
    return (sum((a,b,c)))*0.05

print(myfunc(60,40,100,5))

def myfunc2(*args):
    return sum(args)*0.05#ļauj padot tik argumentus, cik nepieciešams

print(myfunc2(60,40,100,5,1245,69))

#kwargs (key word arguments) - atgriež vārdnīcu

def  myfuncKW(**kwargs):
    if "auglis" in kwargs:
        print(f"Mana izvēle ir {kwargs['auglis']} un {kwargs['darzenis']}.")
    else:
        print("Nevienu augli neatrodu.")

myfuncKW(auglis="ābols", darzenis="burkāns")
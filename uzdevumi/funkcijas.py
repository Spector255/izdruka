#funkcija atgriež 10% no a un 20% no skaitļa b
def procenti(a,b):
    skaitlis_a = (a/100)*10  #a*0,1
    skaitlis_b = (b/100)*20 
    return skaitlis_a,skaitlis_b

"""
def procenti(a,b):
    return a*0.1,b*0.2
"""

print(procenti(58,103))
#####1_uzd#####
def var_pagulet(diena):
    if diena == "Brīvdiena" or diena == "Svētdiena" or diena == "Sestdiena":
        return True
    else:
        return False

print(var_pagulet("Brīvdiena"))
print(var_pagulet("Darbdiena"))
print(var_pagulet("Sestdiena"))
print(var_pagulet("Svētdiena"))
print("##########2_uzd##############")
#####2_uzd#####
def ir_problema(a_smile,b_smile):
    if a_smile == "+" and b_smile == "+":
        return True
    elif a_smile == "-" and b_smile == "-":
        return True
    else:
        return False
print(ir_problema("+","+"))
print(ir_problema("-","-"))
print(ir_problema("+","-"))
print(ir_problema("-","+"))
print("############3_uzd############")
#####3_uzd#####
def summa(a_sk,b_sk):
    if a_sk == b_sk:
        return((a_sk+b_sk)*2)
    else:
        return(a_sk+b_sk)
print(summa(5,10))
print(summa(5,5))
print("#############4_uzd###########")
#####4_uzd#####
def starpiba(sk):
    if  sk <=21:
        st=21-sk
    else:
        st=sk-21
    if st > 21:
        return st*2
    return st
print(starpiba(3))
print(starpiba(121))
print("#############5_uzd###########")
#####5_uzd#####
"""
We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble. Funkcija papagaila_problema
"""

def papagaila_problema(stunda, runa):
    if stunda >= 25:
        return "Error"
    if (stunda > 20 or stunda < 7)and runa == True:
        print("Kaimiņi izsauca pašvaldības policiju")
        return True
    return False

print (papagaila_problema(4))
print (papagaila_problema(13))
print (papagaila_problema(21))
print (papagaila_problema(28))
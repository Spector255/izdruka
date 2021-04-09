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
def modulis(skaitlis):
    if abs(skaitlis) > 21:
        return abs(skaitlis)  * 2
    else:
        return abs(skaitlis)
print(modulis(-48))
print(modulis(48))
print(modulis(-5))
print(modulis(5))
print("##############################")
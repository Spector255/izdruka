#if, else, elif
if 2 > 99:
    print()
elif 5 > 6:
    print("abc")
elif 6 < 2:
    print("abvjbje")
elif 8 > 2:
    print("123456798")
else:
    print("bcd")

x = int(input("Ievadiet skaitli: "))
if x > 5:
    print(f"{x} Lielāks par 5")
elif x > 0:
    print(f"{x} Lielāks par 0")
else:
    print(f"{x} Tas nav pozitīvs skaitlis")
'''
a = int(input("Ievadiet pirmo skaitli: "))
b = int(input("Ievadiet otro skaitli: "))
c = int(input("Ievadiet trešo skaitli: "))
if a > b and a > c:
    if b > c:
        print(a, b, c)
    else:
        print(a, c, b)
elif b > a and b > c:
    if a > c:
        print(b, a, c)
    else:
        print(b, c, a)
elif c > a and c > b:
    if b > a:
        print(c, b, a)
    else:
        print(c, a, b)
'''

if True:
    print("patiesi")

suns_grib_est = False

if suns_grib_est:
    print("Pabaro suni!")
else:
    print("Suns ir paēdis!")

#tuples - līdzīgi list, bet nav maināmi, izmanto (iekavas), sakārtots
my_tup = (1,2,3)
abc = [1,2,3]
print(type (my_tup))
print(type (abc))
print(len (my_tup))
print(len (abc))

#var saturet dažādus datu tipus
my_tup = ("es", 6, 6,2.58,6)
print(my_tup)

#var indeksēt
print(my_tup[0])
print(my_tup[-1])

#metodes
print(my_tup.count(6)) #saskaita cik reizes atkārtojās konkrētais objekts
print(my_tup.index(6)) #parāda indeksu, kur pirmoreiz parādās objekts iekāvās

abc[0] = "viens"
print(abc)
#my_tup[0] = "viens" #nav maināms

#sets - nesakārtotu, unikālu objektu kopa.
my_set = set()
print(my_set)
my_set.add(1)
print(my_set)
my_set.add(2)
print(my_set)
my_set.add(1.26)
print(my_set)
my_set.add(2)
print(my_set)
my_list = [1,1,1,1,1,1,1,2222,2,2,22,2,2,2,2,2,2,2,2,3,3,3,3,3,333,33,3,3,3,3,]
print(my_list)
print(set(my_list))

#piemērs
s = "Salaspils"
my_set = set(s)
print(my_set)

#booleans - True vai False - izmanto loģiskos operatoros
print(True) #ar lielo burtu
print(type(True))

#piemērs
print(1>2)
print(1==1)
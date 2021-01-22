#Man  -> Gan
man = "Māja"
print(man)
slic = man[1:]
man = "G" + slic
print(man)
man = "K" + slic
print(man)
'''
Vai arī
print("G"+slic)
'''

#string konkatinācija
x = "Sveika, Pasaule!"
x = x + " Tu esi skaista!"
print(x)

print(2 + 3)
print("2" + "3")
print(2 + 2.5)

print(x.upper()) #izdrukā tikai ar lielajiem burtiem
print(x.lower()) #izdrukā tikai ar maziem burtiem
print(x.split()) #atdala katru vārdu ar ' ' zīmem, pēc katras atstarpes!
print(x.split("a")) #atdala katru vārdu ar ' ' zīmem, pēc katras a!   
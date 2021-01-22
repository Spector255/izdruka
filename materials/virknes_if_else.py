print("Kā tevi sauc?")
vards = input("Mani sauc ")
print(f"Labdien, {vards}")
vecums = int (input("Cik tev gādu? "))
if vecums > 99:
    print(f"Ta nevar būt, kā tev ir {vecums}")
else: 
    print(f"Tev ir {vecums} gadi.")
    print(f"Tavs dzimšanas gads ir {2021-vecums}.")

#---------------------
#String (rakstzīmju virknes)
print("sveiki")
print('Sveiki')
print("I'm going on a run")
print('Arī šis ir "risinājums"')
print("Sveika, \npasaule!") #drukā 2 rindas
print("Sveika, \tpasaule!") #drukā ar tabulācijas atkāpi

#String garums - len ()
print(len("sveiki"))
print(len("Ko tu domā?"))
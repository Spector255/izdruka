#izveido suluspiedi, kas izspiež sulu no āboliem un apelsīniem.
#izveido funkciju, kas "sagriež" augli 4 gabalos.
def griezejs(augli):
    return augli*4

#izveido funkcijum kas paziņo no cik gabaliem izspiesta sula
def suluspiede(abolu_gab, apelsinu_gab):
    print(f"Sula ir izpiesta no {abolu_gab} abolu gabaliem un no {apelsinu_gab} apelsinu gabaliem")

abolu_gab = (griezejs(15))
apelsinu_gab = (griezejs(6))
print(abolu_gab,apelsinu_gab)

suluspiede(abolu_gab,apelsinu_gab)

#otrais variants - funkcija funkcijā
def griezejs2(augli):
    return augli*4

def suluspiede2(aboli, apelsini):
    abolu_gab = (griezejs2(aboli))
    apelsinu_gab = (griezejs2(apelsini))
    print(f"Sula ir izpiesta no {abolu_gab} abolu gabaliem un no {apelsinu_gab} apelsinu gabaliem")

suluspiede2(45,16)
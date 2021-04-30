#Izveido programmu, kas salīdzina divus lietotāja ievadītos skaitļus un izdod paziņojumu kurš no skaitļiem ir lielāks. Ņem vērā, ka skaitļi var būt arī decimāldaļas un abi skaitļi var būt arī vienādi. Izdrukai jābūt pilnā teikumā, kurā ir iekļauti arī paši skaitļi. Piemēram: ja lietotājs ievada 3,5 un 8, programma izvada “Skaitlis 8 ir lielāks par skaitli 3,5” 
a = float(input("Ievadiet 1. skaitli: "))
b = float(input("Ievadiet 2. skaitli: "))
if a > b:
    print(f"Skaitlis {a} ir lielāks par skaitli {b}")
elif b > a:
    print(f"Skaitlis {b} ir lielāks par skaitli {a}")
else:
    print(f"Skaitlis {a} ir vienāds ar skaitli {b}")
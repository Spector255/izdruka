#go to restaurant
"""
#we can give our functions parameters and those parameters take arguments
def order_food(dish):
    print(f"I am ordering {dish}")
    print(f"{dish.capitalize()} should be pretty tasty")

def eat():
    #everything after indent will be run by this function
    print("Hello!")
    #print("Let's order some food!")
    order_food("potatoes")
    order_food("ice cream")
    print("Lets eat")
    print("Let's leave and be happy")

#call the function 2 times
eat()
#eat()
"""
def funkcijas_nosaukums(vards, uzvards):
    """
    Funkcijas apraksts
    """
    print(f"Sveiki, {vards} {uzvards}!") #visas darbības, ko veic funkcija

funkcijas_nosaukums("Daniils","Zemīts")
funkcijas_nosaukums("Artemijs","Vaščenko")
funkcijas_nosaukums("Ieva","Hermane")
funkcijas_nosaukums("Alīna","Šehlova")

def pilseta(nosaukums, valsts):
    print(f"{nosaukums.capitalize()} ir pilsēta {valsts.capitalize()}.")

pilseta("Salaspils", "Latvijā")
pilseta("Parīze", "Francijā")
pilseta("Berlīne","Vācijā")
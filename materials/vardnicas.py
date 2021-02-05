#Vārdnīcas jab dictionaries
auto = {
    'marka': 'Rolls Roice',
    'modelis': 'Phantom',
    'gads': 2021,
    'cena': 508400
}
d = {
    "k1":[1,2,3]
}
print(d['k1'][1])
tel = {
    "direktors": "67947253",
    "vietnieks": "65674720",
    "sekretāre": "65826974"
}
print(tel["sekretāre"]) #norādot atslēgu, izdrukā vērtību
print(tel["direktors"])

cena = {
    "piens": 1.12,
    "āboli": 0.95,
    "apelsīni": 1.89
}
print(cena["piens"])
print(cena["apelsīni"])

d = {
    "k1":123,
    "k2":[10,11,12],
    "k3":{"atsl1":100, "atsl2":200}
    } #vārdnīcās var uzglābāt dažādus datu tipus
print(d["k3"])
print(d["k3"]["atsl2"]) #izdrukā iekššjās vārdnīcas vērtību
print(d["k2"][2]) #izdrukā saraksta elementu

myDict = {
    "key1":["a","b","c"] 
}
myDict["key1"][1]="f"
print(myDict)
my_list = myDict["key1"]
print(my_list)
burts = my_list[2]
print(burts)
print(burts.upper())

print(myDict["key1"][2].upper()) #aizvieto programmu no 37 līdz 43 rindai

#jaunu objektu pievienošana
new_dict = {
    "k1":100,
    "k2":200,
} 
print(new_dict)
new_dict["k3"]=300
print(new_dict)
new_dict["k1"]="simts"
print(new_dict)

#vārnīcu metodes
print(new_dict.keys()) #izdrukā visas atslēgas
print(new_dict.values()) #izdrukā vērtības
print(new_dict.items()) #izdrukā pārus
vertibu_list = list(new_dict.values())
print(vertibu_list)

print(new_dict.get("k1")) #saņem vērtību pēc atslēgas
print(new_dict)
new_dict.pop("k1") #saņem vērtību pēc atslēgas, izņem to arā no vārdnīcas
print(new_dict)
new_dict.update({"k1": "simts"}) #pievieno elementu vardnicas galā, jā tādas atslēgas nebija, vai atjauno to
print(new_dict)
"""new_dict.popitem()
print(new_dict)
new_dict.del() #izdzēs konkrēto elementu
print(new_dict)
new_dict.clear() #izdsēs pilnibā vārdnīcu"""
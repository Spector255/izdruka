#Vārdnīcas jab dictionaries
auto = {
    'marka': 'Rolls Roice',
    'modelis': 'Phantom',
    'gads': 2021,
    'cena': 508400
}

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
    }
print(d["k3"])
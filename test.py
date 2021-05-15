burts = "a"
vards = "abca"
if burts in vards:
    print("Yes")
else:
    print("No")
indeks = vards.index(burts)
print(f"Indeks #1{indeks}")
vards[indeks] = ""
indeks = vards.index(burts)
print(f"Indeks #2{indeks}")
print(vards.count(burts))
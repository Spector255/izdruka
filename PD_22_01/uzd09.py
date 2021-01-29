vards = input("Ievadiet, lūdzu, vārdu: ")
izvvards = vards[::-1]
pdbrt = izvvards[-1].lower()
prmbrt = izvvards[0].upper()
izvvards = izvvards[1:-1:1]
print(f"{prmbrt+izvvards+pdbrt}. Pamatīgs juceklis, vai ne, {vards[0]}?")

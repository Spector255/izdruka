#Klients pieejot pie kases norāda, vai ir pieejama klienta karte.
#Klients pērk N preces. Klientu karte, katrai precei dod 11% atlaidi.
#Ja pērk vismaz 3 gabalus vai 3 kg ir 5% atlaide, taču, ja ir arī klientu karte tad 15% atlaide.
#Klients ievada preces nosaukumu, cenu (bez atlaides) un daudzumu.
#Programma izvada pilnā teikumā preces nosaukumu, apjomu, cenu un cenu par konkrēto daudzumu. Ja ir pieejama klientu karte izvada cenu ar atlaidi.
#Beigās norāda cik jāmaksā par visu pirkumu kopā, kā arī, kāds ir kopējais ietaupījums.

karte = input(
    'Labdien! Ja Jums ir klienta karte, tad ievadiet "+", ja nav, tad ievadiet "-" : '
)
produktusk = int(input('Lūdzu ievadiet produktu skaitu grozā: '))
summapp = 0.0
for i in range(produktusk):
    produkts_nos = input('Ievadiet preces nosaukumu: ')
    produkts_cen = float(input('Ievadiet preces cenu: '))
    sver = input(
        'Ievadiet "Jā", ja tas produksts ir svērams, vai ievadiet "Nē", ja tas nav svērama produkcija: '
    )
    while sver != "Jā" and sver != "Nē":
        print("Nekorēkti dati")
        sver = input(
            'Ievadiet "Jā", ja tas produksts ir svērams, vai ievadiet "Nē", ja tas nav svērama produkcija: '
        )
    if sver == "Jā":
        produkts_dau = float(input('Ievadiet preces daudzumu: '))
    else:
        produkts_dau = int(input('Ievadiet preces daudzumu: '))
    if produkts_dau >= 3.0 and karte == "+":
        produkts_kopsumma = ((produkts_dau * produkts_cen) / 100) * 85
        produkts_kopsumma = round(produkts_kopsumma, 2)
    elif produkts_dau >= 3.0 and karte == "-":
        produkts_kopsumma = ((produkts_dau * produkts_cen) / 100) * 95
        produkts_kopsumma = round(produkts_kopsumma, 2)
    elif produkts_dau <= 3.0 and karte == "+":
        produkts_kopsumma = ((produkts_dau * produkts_cen) / 100) * 89
        produkts_kopsumma = round(produkts_kopsumma, 2)
    else:
        produkts_kopsumma = produkts_dau * produkts_cen
        produkts_kopsumma = round(produkts_kopsumma, 2)
    summapp = summapp + produkts_kopsumma
    print(
        f"Jūs izvēlejaties {produkts_nos}, {produkts_dau},par {produkts_cen}€, kopā par šo produkstu Jūms jāsamaksā {produkts_kopsumma}€"
    )
summapp=round(summapp,2)
print()
print(f"Kopā Jums par pirkumu jāsamksa {summapp} €")

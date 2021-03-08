#Veikala preču cenu pārbaude.
#Precēm ir pašizmaksa (par kādu cenu veikals iepirka preci), cena (par kādu cenu pārdod klientiem), atlaide (veselos eiro (1€)).
#Lietotājs ievada šīs trīs iepriekšminētās vērtības, kopā ar preces nosaukumu (izmantojot mainīgos, kurus cikls katrā iterācijā pārraksta).
#Programma veic salīdzināšanu, kas nosaka vai:
#1) cena ir lielāka par pašizmaksu un cena pēc atlaides ir lielāka par pašizmaksu -> izdrukā peļņu
#2) cena ir mazāka par pašizmaksu vai cena pēc atlaides ir mazāka par pašizmaksu -> izdrukā  zaudējumus
#3) neizpildas iepriekšejie nosacījumi -> vienkārši neizdevīgi pārdot
#Gadījumā, ja pārdodot preci ir peļņa, jāizvada ne tikai dati par preci, bet arī peļņa procentos.
#Tai pat laikā ir jāveic arī zaudējumu un peļņas summēšana, lai uzzinātu vai gala rezultātā par visām precēm kopā ir peļņa vai zaudējumi.
#Viss iepriekš minētais ir jāveic ciklā, kur katras iterācijas beigās tiek veikta pārbaude vai lietotājs vēlas ievadīt vēl vienu preci (ievadāmo simbolu var izvēlēties patstāvīgi). Visās vietās, kur būtu noderīgi izvadīt informāciju,#izvadām to ar print f.

sakums="+"
while sakums == "+":
    produkts_nos = input('Ievadiet preces nosaukumu: ')
    produkts_pas = float(input('Ievadiet preces pašizmaksu: '))
    produkts_cen = float(input('Ievadiet preces cenu: '))
    while produkts_cen < 0.00 or produkts_pas < 0.00:
        print("Nekorēkti dati")
        produkts_pas = float(input('Ievadiet preces pašizmaksu: '))
        produkts_cen = float(input('Ievadiet preces cenu: '))
    prod_atl = produkts_cen - 1
    if produkts_cen > produkts_pas and produkts_pas < prod_atl:
        print(f'Pārdodot prēci "{produkts_nos}" Jūs pelnesiet {round(produkts_cen-produkts_pas,2)}€({round(((produkts_cen-produkts_pas)/produkts_pas)*100)}%), savukārt pārdod to preci ar atlaidi Jūs pelnesiet {round(prod_atl - produkts_pas,2)}€({round(((prod_atl-produkts_pas)/produkts_pas)*100)}%)')
    elif produkts_cen < produkts_pas or produkts_pas > prod_atl:
        if produkts_cen > produkts_pas:
            print(f'Pārdodot prēci "{produkts_nos}" Jūs pelnesiet {round(produkts_cen-produkts_pas,2)}€({round(((produkts_cen-produkts_pas)/produkts_pas)*100)}%)€, savukārt pārdod to preci ar atlaidi Jūs zaudesiet {abs(round(prod_atl - produkts_pas,2))}€')
        else:
            print(f'Pārdodot prēci "{produkts_nos}" Jūs zaudesiet {produkts_cen-produkts_pas}€, savukārt pārdod to preci ar atlaidi Jūs zaudesiet {prod_atl - produkts_pas}€')
    else:
        print(f'Prēci "{produkts_nos}" neizdevīgi pārdot')
    sakums = input('Ja Jus gribiet turpināt ievadiet "+": ')
print("Paldies!")
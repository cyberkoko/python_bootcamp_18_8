produkty = {
    'ziemniaki': 1.99,
    'bataty': 6.99,
    'pomidory': 2.5,
    'piwo': 7
}

koszyk = {}

for p in produkty:
    print(f"- {p} - {produkty[p]} PLN ")

while True:
    jaki_produkt = input("Jaki produkt chcesz kupić (wpisz k by zakończyć)? ")
    if jaki_produkt == 'k':
        print(koszyk)
        break
    ile = float(input(f"Ile chcesz kupić: {jaki_produkt}? "))
    koszyk[jaki_produkt] = ile * produkty[jaki_produkt]

for wklad in koszyk:
    print(f" - Koszt - {wklad} - {koszyk[wklad]}")
print()

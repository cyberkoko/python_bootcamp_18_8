miastoA = input('Miasto A: ')
miastoB = input('Miasto B: ')
dystans = float(input(f'Dystans {miastoA}-{miastoB}: '))
cena = float(input('Cena paliwa: '))
spalanie = float(input('Spalanie na 100 km: '))

wynik = dystans * cena * spalanie / 100
# wynik = int(wynik)
print(f'Koszt przejazdu {miastoA}-{miastoB} to {wynik:.2f} PLN')

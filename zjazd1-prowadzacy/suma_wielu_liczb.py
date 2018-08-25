# Program ma pytać użytkownika o kolejne liczby całkowite.
# Może ich być dowolnie wiele, a żeby zakończyć podawanie liczb,
# użytkownik wpisuje tekst 'koniec'.
# Na samym końcu program wypisuje sumę wszystkich podanych liczb.
# Dalsze rozwinięcie: program wypisuje także liczbę liczb i ich średnią.

suma = 0
licznik = 0

while True:
    txt = input('Podaj kolejną liczbę: ')
    if txt == 'koniec':
        break
    suma += int(txt)
    licznik += 1

print(f'Podano {licznik} liczb')
print(f'Suma wynosi {suma}')

if licznik > 0:
    srednia = suma / licznik
    print(f'Średnia wynosi {srednia}')

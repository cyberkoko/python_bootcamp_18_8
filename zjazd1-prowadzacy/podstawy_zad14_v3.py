# ta wersja niepoprawnie obsługuje przypadek braku liczb (od razu koniec)
pierwszy_raz = True
while True:
    txt = input('Podaj kolejną liczbę: ')
    if txt == 'koniec':
        break
    liczba = int(txt)
    if pierwszy_raz:  # pierwsza liczba
        min = max = liczba
        pierwszy_raz = False
    else:
        if liczba > max:
            max = liczba
        if liczba < min:
            min = liczba

print(f'Maksimum: {max}')
print(f'Minimum: {min}')


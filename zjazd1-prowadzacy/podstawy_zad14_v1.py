# ta wersja niepoprawnie obsługuje przypadek braku liczb (od razu koniec)

i = 0
while True:
    i += 1
    txt = input('Podaj kolejną liczbę: ')
    if txt == 'koniec':
        break
    liczba = int(txt)
    if i == 1:  # pierwsza liczba
        min = max = liczba
    else:
        if liczba > max:
            max = liczba
        if liczba < min:
            min = liczba

print(f'Maksimum: {max}')
print(f'Minimum: {min}')

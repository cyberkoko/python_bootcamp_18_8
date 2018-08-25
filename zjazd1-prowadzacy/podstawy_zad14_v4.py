min = max = None

while True:
    txt = input('Podaj kolejną liczbę: ')
    if txt == 'koniec':
        break
    liczba = int(txt)
    if max is None or liczba > max:
        max = liczba
    if min is None or liczba < min:
        min = liczba

print(f'Maksimum: {max}')
print(f'Minimum: {min}')

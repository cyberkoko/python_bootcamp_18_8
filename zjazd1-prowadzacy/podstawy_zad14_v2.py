txt = input('Podaj pierwszą liczbę: ')
if txt == 'koniec':
    print('No to pa')
    exit(0)
liczba = int(txt)
min = max = liczba

while True:
    txt = input('Podaj kolejną liczbę: ')
    if txt == 'koniec':
        break
    liczba = int(txt)
    if liczba > max:
        max = liczba
    if liczba < min:
        min = liczba

print(f'Maksimum: {max}')
print(f'Minimum: {min}')

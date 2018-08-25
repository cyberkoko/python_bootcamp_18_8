liczba1 = int(input('Podaj pierwszą liczbę: '))
liczba2 = int(input('Podaj drugą liczbę: '))
operacja = input('Podaj rodzaj operacji: ')

if operacja == '+':
    print(f'Wynik: {liczba1 + liczba2}')
if operacja == '-':
    print(f'Wynik: {liczba1 - liczba2}')
if operacja == '*':
    print(f'Wynik: {liczba1 * liczba2}')
if operacja == '/':
    print(f'Wynik: {liczba1 / liczba2}')
else:
    print('Nieznana operacja')

print('Koniec')

def oblicz(operacja, arg1, arg2):
    if operacja == '+':
        return arg1 + arg2
    elif operacja == '-':
        return arg1 - arg2
    elif operacja == '*':
        return arg1 * arg2
    elif operacja == '/':
        return arg1 / arg2
    else:
        raise ValueError(f'Nieznana operacja {operacja}')

try:
    liczba1 = int(input('Podaj pierwszą liczbę: '))
    liczba2 = int(input('Podaj drugą liczbę: '))
    operacja = input('Podaj rodzaj operacji: ')

    wynik = oblicz(operacja, liczba1, liczba2)
    print(f'Wynik: {wynik}')
except Exception as e:
    print(f'Nastąpił błąd: {e}')

print('Koniec')

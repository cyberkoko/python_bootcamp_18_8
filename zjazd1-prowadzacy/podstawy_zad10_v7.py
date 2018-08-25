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
        return None


liczba1 = int(input('Podaj pierwszą liczbę: '))
liczba2 = int(input('Podaj drugą liczbę: '))
operacja = input('Podaj rodzaj operacji: ')

wynik = oblicz(operacja, liczba1, liczba2)

if wynik is not None:
	print(f'Wynik: {wynik}')
	print(f'A pomnożnony przez 100 {100 * wynik}')
else:
	print('Nieznana operacja')

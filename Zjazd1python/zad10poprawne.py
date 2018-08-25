liczba1 = int(input('Podaj pierwszą liczbę:'))
liczba2 = int(input('Podaj drugą liczbę: '))
rodzaj = input('Podaj rodzaj operacji: ')
if rodzaj == '+' : 
    wynik = liczba1+liczba2
elif rodzaj == '-' :
    wynik = liczba1-liczba2	
elif rodzaj == '*' :
    wynik = liczba1*liczba2
elif rodzaj == '/':
    wynik = liczba1/liczba2
else:
    wynik = None
if wynik is not None:
    print(f'Wynik:{wynik}')
else:
	print('Nieznana operacja') 
 	
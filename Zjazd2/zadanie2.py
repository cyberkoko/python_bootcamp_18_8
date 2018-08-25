suma = []

while len(suma) < 10:
    nowa_liczba = input('Podaj nowa liczbe')
    if nowa_liczba == 'k':
        break
    else:
        nowa_liczba = int(nowa_liczba)
        nowa_liczba = suma.append('')
srednia = sum(suma) / len(suma)

print(f'Srednia z liczb (suma) to (srednia)')

#licznik = 0
#txt = input('Podaj kolejną liczbę ')
#liczba = suma.append('')
#if licznik == 10:
#    print('Koniec')
#    licznik += 1

# print(f'Średnia wynosi {}')

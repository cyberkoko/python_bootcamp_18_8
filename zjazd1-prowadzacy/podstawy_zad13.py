ILE_DNI = 7
suma = 0
i = 1
while i <= ILE_DNI:
    temp = float(input(f'Podaj temperaturę w dniu nr {i}: '))
    suma += temp
    print(f'Bieżąca srednia: {suma / i}')
    i += 1

srednia = suma / ILE_DNI
print(f'Średnia temperatura wynosi {srednia}')

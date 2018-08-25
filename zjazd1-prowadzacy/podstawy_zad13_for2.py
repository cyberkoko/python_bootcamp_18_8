suma = 0

for i in range(1, 8):
    temp = float(input(f'Podaj temperaturę w dniu nr {i}: '))
    suma += temp

srednia = suma / 7
print(f'Średnia temperatura wynosi {srednia}')

suma = 0

# range generuje liczby od 0 do 6
# tych liczb jest dokładnie 7 - tyle razy wykona się pętla
for i in range(7):
    temp = float(input(f'Podaj temperaturę w dniu nr {i+1}: '))
    suma += temp

srednia = suma / 7
print(f'Średnia temperatura wynosi {srednia}')

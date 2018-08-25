from random import randint
zakres = 10

x = randint(0,zakres)
y = randint(0,zakres)
gr1 = randint(0,zakres)
gr2 = randint(0,zakres)

while True:
    odleglosc_x = abs(gr1-x)
    odleglosc_y = abs(gr2-y)
    
    print(f'Jesteś na pozycji X = {gr1} Y = {gr2} ')
    kierunek = input('Podaj kierunek ruchy (wsad) lub (q) ')
    if kierunek == 'w': 
        gr1 += 1
    elif kierunek == 's':
        gr1 -= 1
    elif kierunek == 'a':
        gr2 += 1
    elif kierunek == 'd':
        gr2 -= 1
    elif kierunek == 'q':
        print ('Poddajesz się ? Szkoda')
        break
    else:
        print('Nie ma takiego kierunku')
        continue
    if gr1 < 0 or gr1 >= zakres or gr2 < 0 or gr2 >= zakres:
        print('Porażka, spadłeś z planszy')
        break
    if gr1 == x and gr2 == y:
        print('Znalazleś skarb')
        break
    nowa_odleglosc_x = abs(gr1-x)
    nowa_odleglosc_y = abs(gr2-y)
    if nowa_odleglosc_x < odleglosc_x or nowa_odleglosc_y < odleglosc_y:
        print('Cieplo')
    else:
        print('Zimno')
print('Koniec')            









    
        
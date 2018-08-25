from random import randrange

PLANSZA = 10

skarb_x = randrange(0, PLANSZA)
skarb_y = randrange(0, PLANSZA)
gracz_x = randrange(0, PLANSZA)
gracz_y = randrange(0, PLANSZA)

while True:
    odleglosc_x = abs(gracz_x - skarb_x)
    odleglosc_y = abs(gracz_y - skarb_y)

    print(f'Bieżąca pozycja:  {gracz_x}x{gracz_y}')
    znak = input('Podaj kierunek ruchu [wsad] lub [q] aby zakończyć: ')
    if znak == 'w':
        gracz_y -= 1
    elif znak == 's':
        gracz_y += 1
    elif znak == 'a':
        gracz_x -= 1
    elif znak == 'd':
        gracz_x += 1
    elif znak == 'q':
        print('Poddajesz się? No dobra...')
        break
    else:
        print('Nie ma takiej komendy')
        continue
    
    if gracz_x < 0 or gracz_x >= PLANSZA or gracz_y < 0 or gracz_y >= PLANSZA:
        print('Spadasz z planszy, porażka!')
        break
    if gracz_x == skarb_x and gracz_y == skarb_y:
        print('Znalazłeś skarb, sukces!')
        break
    nowa_odleglosc_x = abs(gracz_x - skarb_x)
    nowa_odleglosc_y = abs(gracz_y - skarb_y)
    if nowa_odleglosc_x < odleglosc_x or nowa_odleglosc_y < odleglosc_y:
        print('Ciepło')
    else:
        print('Zimno')
    
print('Koniec')

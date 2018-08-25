x = int(input('Podaj pozycję gracza X: '))
y = int(input('Podaj pozycję gracza Y: '))

if 10 <= x <= 90 and 10 <= y <= 90:
    print('Środek planszy')
elif 0 <= x < 10 and 10 <= y <= 90:
    print('Lewa krawędź')
elif 90 < x <= 100 and 10 <= y <= 90:
    print('Prawa krawędź')
elif 10 <= x <= 90 and 0 <= y < 10:
    print('Górna krawędź')
elif 0 <= x < 10 and 0 <= y < 10:
    print('Lewy górny róg')
elif 90 < x <= 100 and 0 <= y < 10:
    print('Prawy górny róg')
elif 10 <= x <= 90 and 90 < y <= 100:
    print('Dolna krawędź')
elif 0 <= x < 10 and 90 < y <= 100:
    print('Lewy dolny róg')
elif 90 < x <= 100 and 90 < y <= 100:
    print('Prawy dolny róg')
else:
    print('Poza planszą')

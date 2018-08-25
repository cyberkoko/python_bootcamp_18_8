x = int(input('Podaj pozycję gracza X: '))
y = int(input('Podaj pozycję gracza Y: '))

if x < 0 or x > 100 or y < 0 or y > 100:
    print('Poza planszą')
elif x < 10:
    if y < 10:
        print('Lewy górny róg')
    elif y > 90:
        print('Lewy dolny róg')
    else:
        print('Lewa krawędź')
elif x > 90:
    if y < 10:
        print('Prawy górny róg')
    elif y > 90:
        print('Prawy dolny róg')
    else:
        print('Prawy krawędź')
else:
    if y < 10:
        print('Górna krawędź')
    elif y > 90:
        print('Dolna krawędź')
    else:
        print('Środek planszy')

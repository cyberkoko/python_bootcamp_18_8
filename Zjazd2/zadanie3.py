lista = [0, 100, 52, -5, -6, -45]

liczby_dodatnie = 0
liczby_ujemne = 0
for liczba in lista:
    if liczba > 0:
        liczby_dodatnie += 1
    elif liczba < 0:
        liczby_ujemne += 1
print('Ujemnych',(liczby_ujemne), 'dodatnie',(liczby_dodatnie))

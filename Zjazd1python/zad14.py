max = 0 


while True:
    txt = input('Podaj liczbę ')
    if txt == 'koniec':
        break
    liczba = int(txt)
    if liczba > max:
        max = liczba 
print(f'Maksimum wynosi {max}')
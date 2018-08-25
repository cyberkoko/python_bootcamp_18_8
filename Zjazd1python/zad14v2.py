min = max = None
while True:
    txt = input('Podaj liczbę ')
    if txt == 'koniec':
        break
        
    liczba = int(txt)
    if max is None or liczba > max:
            max = liczba
    if min in None or liczba < min:
            min = liczba
    
     
print(f'Maksimum wynosi {max}')
print(f'Minimum wynosi {min}')
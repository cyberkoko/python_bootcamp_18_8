min = max = None

while True:
    txt = input('Podaj kolejną liczbę: ')
    if txt == 'koniec':
        break
    # w tej wersji ignorujemy teksty nie będące liczbami
    try:
        liczba = int(txt)
        if max is None or liczba > max:
            max = liczba
        if min is None or liczba < min:
            min = liczba
    except Exception:
        pass

print(f'Maksimum: {max}')
print(f'Minimum: {min}')

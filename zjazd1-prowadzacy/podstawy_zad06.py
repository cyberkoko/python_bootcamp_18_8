liczba = int(input('Podaj liczbę"'))

warunek1 = liczba > 10
warunek2 = liczba <= 15
warunek3 = liczba % 2 == 0

print(f'Większa od 10: {warunek1}')
print(f'Mniejsza równa 15: {warunek2}')
print(f'Podzielna przez 2: {warunek3}')

# Inne podejscie:
print(f'Większa od 10: {liczba > 10}')
print(f'Mniejsza równa 15: {liczba <= 15}')
print(f'Podzielna przez 2: {liczba % 2 == 0}')

# Program ma w pętli pytać o liczbę całkowitą,
# a zakończyć się po podaniu liczby podzielnej przez 7

print('Startujemy...')

while True:
    liczba = int(input('Podaj kolejną liczbę: '))
    if liczba % 7 == 0:
        break
    print('To nie jest liczba podzielna przez 7, próbuj dalej.')
    
print('Koniec')

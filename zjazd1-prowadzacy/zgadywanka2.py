# "Program sprawdzający znajomość tabliczki mnożenia"
# Program losuje dwie liczby i pyta użytkownika 'Ile wynosi iloczyn tych liczb'
# Użytkownik wprowadza swoją odpowiedź, program sprawdza czy odpowiedź jest prawidłowa.
# Program pyta o kolejne propozycje tak długo, aż użytkownik poda prawidłową odpowiedź.
# Na końcu program wypisuje gratulacje i informację o tym w której próbie udało się podać poprawny wynik.

from random import randint

ZAKRES = 10

x = randint(1, ZAKRES)
y = randint(1, ZAKRES)
proby = 0

while True:
    liczba = int(input(f'Jaki jest wynik {x} * {y} ? '))
    proby += 1
    if liczba == x * y:
        print('Dobrze!')
        break
    else:
        print('Źle')
    
print(f'Koniec. Udało się w {proby} próbie.')

# program do sprawdzania znajomosci tabliczki mnozenia
#program ma losowac dwie liczby, pyta uzytkownika ile wynosi iloczyn tych liczb
#uzytkownik wprowadza swoja odpowiedz, program sprawdza czy jest to poprawne
#program pyta dalej az uzytkownik poda poprawna odpowiedz
#na koncu program wypisuje gratulacje oraz ilosc prob jakie prowadzily do sukcesu


from random import randint
zakres = 10
x = randint(1,zakres)
y = randint(1,zakres)
print(f'X = {x} Y = {y} ')
p=0
t1 = x * y
while True:
    t2 = float(input('Ile wynosi iloczyn tych liczb ? ')) 
    p += 1
    if t1 == t2:
        break  
print(f'Gratulacje, to poprawna odpowiedz, udało Ci sié po {p} próbach')    
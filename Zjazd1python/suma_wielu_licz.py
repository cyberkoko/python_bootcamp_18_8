#pytanie o kolejne liczbe calkowite, moze byc ich dowolnie wiele
#aby zakonczyc uzytkownik podaje tekst "KONIEC"
# na samym koncu program wypisuje sume wszystkich podanych liczba

suma = 0 
licznik = 0 
while True:
    txt = input('Podaj kolejną liczbę ')
    if txt == 'koniec':
        break
    liczba = int(txt) 
    licznik += 1
    suma += liczba 
print(f'Podano {licznik} liczb')            
print(f'Suma wynosi {suma}')    
if licznik > 0:
    srednia = suma / licznik

print(f'Średnia wynosi {srednia}')
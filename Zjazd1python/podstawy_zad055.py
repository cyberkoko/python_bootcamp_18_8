print('Pierwsze miasto')
a = input()
print('Drugie miasto')
b = input()
print('Odległość')
c = float (input())
print('Cena paliwa')
p = float(input())
print ('Podaj spalanie na 100 km')
s = float(input())

koszt = int(c*p*s / 100) 
#koszt = int(koszt)
print(f'Odległość wynosi {c}KM')
print(f'Koszt wynosi {koszt} PLN')

#cena = float(input('Cena za kg: ')) tak mozna to szybciej zrobic <---

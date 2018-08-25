from random import randint
zakres = 10

x = randint(1,zakres)
y = randint(1,zakres)

gr1 = randint(1,zakres)
gr2 = randint(1,zakres)

print(f'Jesteś na pozycji X = {gr1} Y = {gr2} ')
while True:
    
    kierunek = input('Podaj kierunek ruchy ')
    if kierunek == 'w': 
        gr1 += 1
    if kierunek == 's':
        gr1 -= 1
    if kierunek == 'a':
        gr2 += 1
    if kierunek == 'd':
        gr2 -= 1
print(f'Jesteś na pozycji {gr1}{gr2}')    

    
    
    
    if x ==gr1 and y == gr2:
        break
    print('Znalazłeś skarb')   
    
    
    
    
    
x = int(input('Podaj pozycje gracza X:'))
y = int(input('Podaj pozycje gracza Y:'))
if x <0 or x >100 or y <0 or y >100:
    print ('Gracz jest poza planszą')
elif x<10 and y< 10:
    print('Lewy dolny róg')
elif x<10 and y<90:
    print ('Lewa krawędz')

    
 
if 10 <= x <= 90 and 10 <= y <=90:
    print ('Gracz jest w centrum')
elif 0 <= x <=10: 
    print ('Gracz jest na lewej krawdzędzi')
else:
    print ('Gracz jest w górnym lewym rogu')
    
    

   
ile_dni = 7
temp = 1
suma = 0 
while temp <=ile_dni:
    x = float(input('Jaka jest temperatura ?'))
    suma += x
    temp += 1
srednia = suma / ile_dni     
     
    
       
print(f'Średnia temperatura wynosi {srednia}')
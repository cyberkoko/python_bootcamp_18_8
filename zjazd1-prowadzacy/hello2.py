print('Hello world')
print("Ala's cat")
print('Ala ma kota')
print('Ola ma psa')
# Ta linia jest komentarzem
print('Ala\'s cat')
print('Ola ma\tpsa')
print('Jedna linia\nDruga linia')

# Ten print nie przejdzie do nowej linii
print('Ala', end='')
print('Ola', end='')
print('Ela')

# Domyślnie wartością parametru end jest '\n'
print('Kasia', end='\n')

print('Ala', 'Ola', 'Ela')
print('Ala', 'Ola', 'Ela', sep=';', end='*\n')

print('Koniec')

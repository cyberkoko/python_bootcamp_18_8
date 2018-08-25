imie1 = 'Ala'
imie2 = 'Ola'

x = 5
y = 10

print('%s ma %d kotów' % (imie1, x))
print('%s ma %d psów' % (imie2, y))
s = '%s ma %d psów' % (imie2, y)
print(s)
print()

print(f'{imie1} ma {x} kotów')
print(f'{imie2} ma {y} psów')
s = f'{imie2} ma {y} psów'
print(s)

print(f'{imie2:5} ma {y} psów')

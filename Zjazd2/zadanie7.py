samogloski_liczba = 0

SAMOGLOSKI = 'aeiouy'

txt=input('Podaj napis ')

for i in txt:
    if i.lower() in SAMOGLOSKI:
        samogloski_liczba += 1



print('liczba samoglosek', (samogloski_liczba))







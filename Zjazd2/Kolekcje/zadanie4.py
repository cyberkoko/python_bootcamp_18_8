ile_podzielnych = 0

for i in range(101):
    if i % 3 == 0 or i % 5 == 0:
        ile_podzielnych += 1
        print(i)
print('Podzielne', (ile_podzielnych))
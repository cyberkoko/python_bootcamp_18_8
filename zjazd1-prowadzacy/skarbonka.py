# Program ma wyświetlać aktualną wartość skarbonki,
# pytać użytkownika o kolejną wpłatę (użytkownik podaje liczbę)
# tak długo, aż w skarbonce zbierze się odpowiednia kwota (np. 100)

skarbonka = 20
plan = 100
print(f'Początkowa wartość skarbonki to {skarbonka}, a planujemy zebrać {plan}')

while skarbonka < plan:
    wplata = int(input('Ile wpłacasz? '))
    skarbonka += wplata
    print(f'Po wpłaceniu {wplata} w skarbonce jest {skarbonka}')

print('Osiągnąłeś swój cel :)')

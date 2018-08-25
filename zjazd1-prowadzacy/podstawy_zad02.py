a = 3
b = 9
h = 6.5

# Lepiej wynik obliczenia zapisać na dodatkowej zmiennej - to zwiększy czytelność kodu
pole_trapezu = (a + b) * h / 2

# Gdy chcemy ładnie wypisać wynik wraz z tekstem, mamy takie możliwości:
# Najpierw napis, a potem wynik:
print('Pole trapezu wynosi: ', end='')
print(pole_trapezu)

print('Pole trapezu wynosi:', pole_trapezu)

# Uwaga: nie działa to co w Javie lub C#:
#print('Pole trapezu wynosi: ' + pole_trapezu)

# Ewentualnie można konwertując liczbę na napis:
print('Pole trapezu wynosi: ' + str(pole_trapezu))

# Sposób popularny w Pythonie 2 i po drobnych zmianach wciąż dostępny:
print('Pole trapezu wynosi: %d' % pole_trapezu)

# Od Pythona 3.6 można użyć składni fstring:
# Obecnie to jest najbardziej zalecane podejście
print(f'Pole trapezu wynosi: {pole_trapezu}')

# Można nawet tak, ale nie polecam
print(f'Pole trapezu wynosi: {(a + b) * h / 2}')

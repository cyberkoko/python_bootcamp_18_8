liczba = 15

if liczba > 10:
    print('AAA')
    print('Ala')
print('Za pierwszym ifem')

if liczba > 20:
    print('BBB')

print('Za drugim ifem')

if liczba % 5 == 0:
	print('Liczba jest podzielna przez 5')
else:
	print('Liczba NIE jest podzielna przez 5')

# W Pythonie bloki nie mogą być puste. Jeśli potrrzebujemy bloku, który nic nie robi, to używamy instrukcji pustej pass
if liczba % 2 == 0:
    pass
else:
    print('Liczba nieparzysta')

# Można zagnieżdżać if i else, ale jeśli przesadzimy, to program jest nieczytelny
if liczba < 10:
	print('Liczba mniejsza niż 10')
else:
    if liczba < 20:
		print('Liczba >= 10 i < 20')
	else:
        if liczba < 30:
		    print('Liczba >= 20 i < 30')
	    else:
		    print('Liczba >= 30')

# W Pythonie istnieje słowo kluiczowe elif, które ułatwia pisanie takich ciągów warunków
if liczba < 10:
    print('Liczba mniejsza niż 10')
elif liczba < 20:
    print('Liczba >= 10 i < 20')
elif liczba < 30:
    print('Liczba >= 20 i < 30')
else:
    print('Liczba >= 30')

rok_urodzenia = int(input('Podaj rok urodzenia: '))

#if 2018 - rok_urodzenia >= 18:
#    print('Jesteś osobą pełnoletnią')
#else:
#    print('Jesteś osobą niepełnoletnią')

# Można uprościć - zakładając, że dzisiejszy rok to 2018
#if rok_urodzenia <= 2000:
#    print('Jesteś osobą pełnoletnią')
#else:
#    print('Jesteś osobą niepełnoletnią')

rok_biezacy = 2018
wiek = rok_biezacy - rok_urodzenia
	
if wiek >= 18:
    print('Jesteś osobą pełnoletnią')
else:
    print('Jesteś osobą niepełnoletnią')

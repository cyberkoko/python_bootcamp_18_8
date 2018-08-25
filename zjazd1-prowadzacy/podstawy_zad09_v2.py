import datetime

rok_urodzenia = int(input('Podaj rok urodzenia: '))
rok_biezacy = datetime.datetime.today().year
# wyjaśnienie składni: z modułu datetime pobieram klasę datetime, wywołuję na niej metodę statyczną today(), ona zwraca obiekt - bieżąca data i czas - a tego obiektu odczytuję pole year

wiek = rok_biezacy - rok_urodzenia

if wiek >= 18:
    print('Jesteś osobą pełnoletnią')
else:
    print('Jesteś osobą niepełnoletnią')

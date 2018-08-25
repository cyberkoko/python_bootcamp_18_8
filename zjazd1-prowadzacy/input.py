print('Napisz coś')
tekst = input()
print(f'Napisałeś {tekst}')

imie = str(input('Jak masz na imię?'))  # Użycie str w tym momencie nie jest konieczne, ale czasami tak też się pisze, aby zwiększyć czytewlnośc (żeby było wiadomo, że wczytujemy napis)
print(f'Hello {imie}!')

r = float(input('Podaj promień koła: '))
print(f'Na zmiennej r jest wartość typu {type(r)}')
PI = 3.14
pole_kola = PI*r*r
print(f'Pole koła jest równe {pole_kola}')


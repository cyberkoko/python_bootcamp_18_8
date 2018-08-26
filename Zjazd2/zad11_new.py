liczby=set()

while True:
    komenda = input("Podaj liczbę lub wpisze k aby zakonczyć ")
    if komenda == "k":
        break
    else:
        liczba=int(komenda)
        liczby.add(liczba)
print(f'Podano liczbe unikalnych liczb ',len(liczby))

liczby_parzyste=set(range(0,101,2))
print(f'Parzystych w zakresie 0-100 jest ', len(liczby_parzyste&liczby))
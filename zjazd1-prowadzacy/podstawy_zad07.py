liczba = int(input('Podaj liczbę:'))

print(liczba % 2 == 0 and liczba % 3 == 0 \
	and liczba > 10 or liczba == 7)

# W Pythonie (ze względów historycznych) istnieją też operatory logiczne pisane jako & i |  (pojedyncze!!!)
# Ale one mają inne priorytety, są też dostepne dla liczb (operatory bitowe) i dlatego zniechęcamy do ich używania. Należy używać słów and i or.
print(((liczba % 2 == 0) & (liczba % 3 == 0) & (liczba > 10)) | (liczba == 7))

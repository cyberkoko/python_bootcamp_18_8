#tuple czyli krotka dla pythona
#            0       1           2       3
imiona=('Robert','Piotrek','Karolina','Paweł')
print(type(imiona))
print(imiona)
print(len(imiona))

print('Robert'in (imiona))
print('Kuba'in (imiona))


for imie in imiona:
    print (imie)


print("pierwsze imie",imiona[0])

print("ostatnie imie",imiona[-1])

print("pare imion",imiona[1:3])

print('Zabawa ile jest imion Karolina',imiona.count('Karolina'))

print('Zabawa indeksem Karolina',imiona.index('Karolina'))




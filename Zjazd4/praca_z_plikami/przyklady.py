plik = open("pliki_wejsciowe/dane.txt")
print(plik)
plik.close()

with open("pliki_wejsciowe/dane.txt") as plik:
    for i in plik:
        print(i)
with open (r"nowy_plik.txt", 'w', encoding='utf-8') as f:
    f.write("Nowe dane wyjsciowe")
print(plik)





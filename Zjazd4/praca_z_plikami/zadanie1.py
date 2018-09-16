

plik = open("pliki_wejsciowe/dane.txt")
print(plik)
plik.close()

with open("pliki_wejsciowe/dane.txt", encoding="utf-8") as plik:
    for i in plik:
        print(i)
print(plik)






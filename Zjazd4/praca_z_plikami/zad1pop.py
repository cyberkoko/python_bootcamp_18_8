import sys
print (sys.argv)

try:
    wejscie = sys.argv[1]
    with open(sys.argv[1]) as f:
        dane = f.read()
        dane = dane.splitlines()
        i = 0
        for linia in dane:
            i += 1
            print(linia)


except IndexError:
    print("Podaj nazwe pliku")
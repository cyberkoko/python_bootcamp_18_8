def policz_znaki(napis, start="<", end=">"):
    if start == end:
        raise ValueError("parametry start i end nie moga być takie same")
    ile_znakow = 0
    poziom = 0
    for litera in napis:
        if litera == start:
            poziom += 1
            continue
        elif litera == end:
            poziom -= 1
            continue
        ile_znakow += poziom

    return ile_znakow
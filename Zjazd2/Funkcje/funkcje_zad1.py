
def czy_jest_pierwsza(n):
    for dzielnik in range(2, n):
        if n % dzielnik == 0:
            return False
    return True


def test_czy_jest_pierwsza_dla_liczby():
    assert czy_jest_pierwsza(3)  # tu powinno byc zwrocone true


def test_czy_jest_pierwsza_dla_liczby_drugiej():
    assert not czy_jest_pierwsza(4)  # tu powinno byc zwrocone false

def hello_world(name="World"):
    return f"Hello {name}"


def dodaj(a, b):
    if type(b) == str:
        a = str(a)
    return a + b


def pomnoz(a, b):
    return a * b


def test_dodaj():
    assert dodaj(1, 1) == 2
    assert dodaj(1, -1) == 0
    assert dodaj(0, 0) == 0
    assert dodaj(1, 'a') == '1a'
    # assert dodaj('a', 2) == 'a2'


def test_pomnoz():
    assert pomnoz(1, 2) == 2
    assert pomnoz(0, 1) == 0
    # assert pomnoz('a', 'a') == 'aa'


def test_kombinacja_dzialan():
    a = 1
    b = 2
    c = 3
    tmp = dodaj(a, b)

    assert pomnoz(tmp, c) == 10

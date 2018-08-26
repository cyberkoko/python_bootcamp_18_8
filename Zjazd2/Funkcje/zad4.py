def formatuj(*napisy, **cena):
    napisy = '\n' .join(napisy)
    napisy = napisy.replace('cena'str(cena))

    return '\n' .join(napisy)


def test_formatuj_napis_bez_znacznikow ():
    assert formatuj("hello world") == "hello world"


def test_formatuj_napisy_bez_znacznikow ():
    assert formatuj("hello world", 'Jam jest Rafał') == "hello world", "\nJam jest Rafał"


def test_formatuj_napis_ze_znacznikiem ():
    assert formatuj('koszt $cena PLN', 'kwota $cena brutto', cena=10) == "koszt 10 PLN\nkwota 10 brutto"












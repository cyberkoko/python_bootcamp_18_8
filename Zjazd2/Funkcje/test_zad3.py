import pytest
from .zad3_ver2 import policz_znaki

def test_policz_znaki_w_pustym_napisie():
    assert policz_znaki("") == 0

def test_policz_znaki_gdy_brak_nawiasow():
    assert policz_znaki("Ala ma kota") == 0

def test_policz_znaki_z_nawiasami_jeden_poziom():
    assert policz_znaki("Ala <ma> kota") == 2
    assert policz_znaki("Ala <ma ko>ta") == 5
    assert policz_znaki("Ala <ma> <ko>ta") == 4
    assert policz_znaki("a <a<a<a>>>") == 6

def test_policz_znaki_z_podanymi_parametrami():
    assert policz_znaki('ala [kota [a kot]] ma [ale]', '[', ']') == 18
    assert policz_znaki('ala {kota {a kot}} ma {ale}', '{', '}') == 18

def test_raise_error():
    with pytest.raises(ValueError):
        policz_znaki("AAA", ".", ".")
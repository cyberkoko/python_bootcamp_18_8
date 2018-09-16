from Zjazd4.mathematica.geometry.figures import triangle_area, square_area


def test_square_area():
    assert square_area(2) == 4
    assert square_area(3) == 9


def test_triangle_area():
    assert triangle_area(5, 4) == 10
    assert triangle_area(4, 3) == 6

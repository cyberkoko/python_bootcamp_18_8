from math import sqrt


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # na chwile zakladamy

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        v_ret = Vector(new_x, new_y)
        return v_ret

    def __sub__(self, other):
        new_x2 = self.x - other.x
        new_y2 = self.y - other.y
        v_ret = Vector(new_x2, new_y2)
        return v_ret

    def __mul__(self, other):
        new_x3 = self.x * other.x
        new_y3 = self.y * other.y
        v_ret = Vector(new_x3, new_y3)
        return v_ret

    @property
    def lenght(self, agrt=None):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __eq__(self, other):
        return self.lenght == other.lenght

    def __gt__(self, other):
        return self.lenght > other.lenght

    def __ge__(self, other):
        return self.lenght < other.lenght

    def __ne__(self, other):
        return self.lenght != other.lenght

    def __lt__(self, other):
        return self.lenght < other.lenght

    def __le__(self, other):
        return self.lenght <= other.lenght

    @property
    def __str__(self):
        return f"V{(self.x) , (self.y), (self.lenght)}"


def test_creat():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    assert v1.x == 1
    assert v1.y == 2


def test_add():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = v1 + v2
    assert v3.x == 4
    assert v3.y == 6


def test_sub():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v4 = v1 - v2
    assert v4.x == -2
    assert v4.y == -2


def test_multi():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v5 = v1 * v2
    assert v5.x == 3
    assert v5.y == 8


def test_gretest_then():
    v1 = Vector(4, 4)
    v2 = Vector(3, 4)
    assert v1 > v2


def test_equali1():
    v1 = Vector(1, 2)
    v2 = Vector(1, 2)
    assert v1 == v2


def test_equali2():
    v1 = Vector(1, 2)
    v2 = Vector(-1, 2)
    assert v1 == v2


def test_equali3():
    v1 = Vector(1, 2)
    v2 = Vector(1, 2)
    assert v1 == v2


def test_sortet_list():
    v1 = Vector(1, 2)
    v2 = Vector(0, 1)
    v3 = Vector(3, 2)

    lista = [v1, v2, v3]
    assert sorted(lista) == [v2, v1, v3]

    print(lista)

from Zjazd4.mathematica.algebra import matrices


def test_add_matices():
    m1 = [
        (1, 2, 3),
        (4, 5, 6)

    ]
    m2 = [
        (7, 8, 9),
        (10, 11, 12)
    ]

    rezults = matrices.add_matrices(m1, m2)
    expeceted = [
        (8, 10, 12),
        (14, 16, 18)

    ]

    assert rezults == expeceted


def sub_matrices():
    m1 = [
        (1, 2, 3),
        (4, 5, 6)
    ]
    m2 = [
        (7, 8, 9),
        (10, 11, 12)
    ]

    rezults = matrices.sub_matrices(m1, m2)
    expeceted = [
        (-6, -6, -6),
        (-6, -6, -6)

    ]
    assert rezults == expeceted

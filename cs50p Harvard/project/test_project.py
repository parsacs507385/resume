from project import add, sub, mul, fdiv


def test_add():
    assert add(2, 5) == 7
    assert add(5, 5) == 10
    assert add(0, 5) == 5
    assert add(56, 5) == 61


def test_sub():
    assert sub(2, 5) == -3
    assert sub(5, 5) == 0
    assert sub(0, 5) == -5
    assert sub(56, 5) == 51


def test_mul():
    assert mul(2, 5) == 10
    assert mul(5, 5) == 25
    assert mul(0, 5) == 0
    assert mul(56, 5) == 280


def test_fdiv():
    assert fdiv(2, 5) == 0
    assert fdiv(5, 5) == 1
    assert fdiv(0, 5) == 0
    assert fdiv(56, 5) == 11


# test_add()
# test_sub()
# test_mul()
# test_fdiv()

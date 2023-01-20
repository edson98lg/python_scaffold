from hello import add


def test_add():
    assert add(1, 2) == 3
    assert add(1, 4) == 5
    assert add(1, 10) == 11
    assert add(1, 2) == 3
    assert add(1, 2) == 3
    assert add(1, 2) == 3

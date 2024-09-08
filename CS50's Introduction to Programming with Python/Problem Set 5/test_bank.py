from bank import value

def test_value_hello():
    assert value("hello, world") == 0

def test_value_Hello():
    assert value("Hello, world") == 0

def test_value_h():
    assert value("heisenberg") == 20

def test_value_H():
    assert value("Hamburguer") == 20

def test_value_else():
    assert value("else") == 100

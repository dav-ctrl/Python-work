from project import validate_name, convertion, final

def test_1():
    assert validate_name("David  Ortiz") == False

def test_2():
    assert convertion(50, "USD", "EUR") == 44.79082683866344

def test_3():
    assert final("David Ortiz", "Santander", "50", "EUR") == f"DAVID ORTIZ has 50 EUR in bank SANTANDER"


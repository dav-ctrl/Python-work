from plates import is_valid

def test_valid():
    assert is_valid("CS50") == True

def test_0():
    assert is_valid("CS05") == False

def test_punct():
    assert is_valid("PI3.14") == False

def test_min_char():
    assert is_valid("H") == False

def test_max_char():
    assert is_valid("OUTATIME") == False

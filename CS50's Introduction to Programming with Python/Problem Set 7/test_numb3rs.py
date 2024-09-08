from numb3rs import validate

def test_first_number():
    assert validate("275.2.4.24") == False

def test_bool():
    assert validate("cat") == False

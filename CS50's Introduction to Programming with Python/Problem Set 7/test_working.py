from working import convert

def test_convert1():
    assert convert("9:30 AM to 5 PM") == "9:30 to 17:00"

def test_convert2():
    assert convert("9:60 PM to 6 AM") == ValueError("Not a valid hour")

def test_convert3():
    assert convert("8:45 PM - 9 PM") == ValueError("Not a valid format")


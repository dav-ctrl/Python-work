from fuel import convert, gauge

def test_convert():
    assert convert("3/4") == 75

def test_gauge():
    assert gauge(75) == "75%"

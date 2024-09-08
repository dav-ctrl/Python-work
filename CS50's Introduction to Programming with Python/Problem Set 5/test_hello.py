from twttr import shorten

def test_lower():
    assert shorten("hello") == "hll"

def test_upper():
    assert shorten("HELLO") == "HLL"

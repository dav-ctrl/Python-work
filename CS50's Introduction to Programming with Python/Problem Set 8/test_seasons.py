from seasons import validate
from seasons import get_minutes

def test_validate():
    assert validate("January 1, 1999") == False

def test_get_minutes():
    assert get_minutes("2024-08-29") == 1440

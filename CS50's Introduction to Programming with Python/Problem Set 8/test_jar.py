from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def test_str():
    jar = Jar()
    assert str(jar) == "0 cookies"
    jar.deposit(1)
    assert str(jar) == "1 cookie"
    jar.deposit(11)
    assert str(jar) == "12 cookies"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5

def test_withdraw():
    jar = Jar(12,12)
    jar.withdraw(5)
    assert jar.size == 7

from um import count

def test_count1():
    assert count("album") == 0

def test_count2():
    assert count("Um, thanks um...") == 2

def test_count3():
    assert count("Um, thanks for the album") == 1

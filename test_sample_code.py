from sample_code import add, sub

def test_add():
    assert add(1, 2) == 3

def test_add_zero():
    assert add(1, 0) == 1

def test_sub():
    assert sub(3, 1) == 2

def test_sub_zero():
    assert sub(3, 0) == 3

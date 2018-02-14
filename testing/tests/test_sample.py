from .fun import func

def test_correct_func():
    assert func(4) == 5

def test_incorrect_func():
    assert func(3) == 5

def test_float_func():
    test_float = func(3.5)
    assert test_float == 4.5
    assert isinstance(test_float, float)


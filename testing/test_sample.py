# Ok, to get started I'll define a simple function and then
# define one test that passes and another that fails

# Create a really simple function
def func(x):
    return x + 1

def test_correct_func():
    assert func(4) == 5

def test_incorrect_func():
    assert func(3) == 5

# Ok, pause here.  On the command line, try running `pytest`:

# $ pytest

# pytest will run all files of the form test_*.py or *_test.py
# in the current directory and its subdirectories

# You should see 1 failed and 1 passed

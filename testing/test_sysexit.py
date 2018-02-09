# Now we will use `assert` that a certain error is raised

# use `raises` helper to asser that some code raises an exception
import pytest

def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()

# Ok, another pause.  Execute the test function with 'quiet' reporting mode (-q):

# $ pytest -q test_sysexit.py

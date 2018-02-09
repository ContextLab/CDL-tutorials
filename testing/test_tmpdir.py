# You can also request a unique temporary directory for functional tests

def test_needsfiles(tmpdir):
    print (tmpdir)
    assert 0

# List the name tmpdir in the test function signature and pytest will lookup
# and call a fixture factory to create the resource before performing the test
# function call. Before the test runs, pytest creates a
# unique-per-test-invocation temporary directory:

# $pytest -q test_tmpdir.py


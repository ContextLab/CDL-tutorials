# So now, you've got a ton of tests
# you may want to group multiple tests in a class

# pytest makes it easy to create a class containing more than one test:

class TestClass(object):
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')



# finds both test_ prefixed functions. There is no need to subclass anything.

#  In this example we will run the module by passing its filename:

# $ pytest -q test_class.py

# The first test passed and the second failed. You can easily see the intermediate
# values in the assertion to help you understand the reason for the failure.
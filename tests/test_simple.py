from hello_python.subpackage.math import add_two

class TestClass:
    def test_add_two(self):
        assert add_two(1, 2) == 3

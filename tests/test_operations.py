# we test the correctness of methods written in src/math_operations.py
# to do that, we need to import those methods
from src.math_operations import add, sub


# test cases for 'add' method
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(10,6) == 16

def test_sub():
    assert(5,3) == 2
    assert(-10,2) == -12
"""
from calculator import squared

def main():
    test_squared()

def test_squared():
    assert squared(2) == 4
    assert squared(3) == 9
    assert squared(-2) == 4
    assert squared(-3) == 9
    assert squared(0) == 0

if __name__ == "__main__":
    main()
"""
# To run the test program, reaname the 21_calculator.py file to calculator.py as per the pythonic naming conventions.


# To test with pytest, in the cli
# pytest 21_test_calculator2.py 



# Pytest actually takes care of the try and except part and gives you suggestion on test result utilizing the assert keyword

"""
from calculator import squared

def main():
    test_positive()
    test_negetive()
    test_zero()

def test_positive():
    assert squared(2) == 4, "Square(2) is not 4"
    assert squared(3) == 9, "Square(3) is not 9"
    assert squared(4) == 16, "Square(4) is not 16"

def test_negetive():
    assert squared(-2) == 4, "Square(-2) is not 4"
    assert squared(-3) == 9, "Square(-3) is not 9"
    assert squared(-4) == 16, "Square(-4) is not 16"

def test_zero():
    assert squared(0) == 0, "Square(0) is not 0"

if __name__ == "__main__":
    main()
"""


# TypeError incase of a str input

import pytest
from calculator import squared

def main():
    test_positive()
    test_negetive()
    test_zero()

def test_positive():
    assert squared(2) == 4
    assert squared(3) == 9
    assert squared(4) == 16

def test_negetive():
    assert squared(-2) == 4
    assert squared(-3) == 9
    assert squared(-4) == 16

def test_zero():
    assert squared(0) == 0

def test_string():
    with pytest.raises(TypeError):
        squared("cat")

if __name__ == "__main__":
    main()
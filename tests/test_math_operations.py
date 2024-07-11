import sys
import os

# Add the module directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'module')))

from module import addition



def test_add_two_numbers() -> None:
    assert addition.add_two_numbers(a=1, b=2) == 3
    assert addition.add_two_numbers(-1, 1) == 0
    assert addition.add_two_numbers(0, 0) == 0
    assert addition.add_two_numbers(-5, -5) == -10
    assert addition.add_two_numbers(100, 200) == 300
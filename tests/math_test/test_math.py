# This is not a PyTest
import pytest


def add_two_numbers(a, b):
    return a + b


# PyTest should always start with test_
@pytest.mark.math   # Marks are similar to tags
def test_small_numbers():
    assert add_two_numbers(1, 2) == 30, "The sum of 1 and 2 should be 3"


# PyTest should always start with test_
@pytest.mark.math   # Marks are similar to tags
def test_large_numbers():
    assert add_two_numbers(100, 300) == 400, "The sum of 100 and 300 should be 400"

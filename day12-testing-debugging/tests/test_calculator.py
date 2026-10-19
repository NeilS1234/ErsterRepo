import pytest

from src.calculator import add, average 

# Normal-case tests
def test_add_two_positive_numbers() -> None:
    assert add(2, 3) == 5 

def test_add_negative_number() -> None:
    assert add(-2, 3) == 1

def test_average_multiple_numbers() -> None:
    assert average([2, 4, 6]) == 4   

#Edge-case tests 
def test_add_zero() -> None:
    assert add(0, 5) == 5


def test_average_single_number() -> None:
    assert average([7]) == 7


def test_average_all_zeros() -> None:
    assert average([0, 0, 0]) == 0


# Invalid-input tests
def test_average_empty_list() -> None:
    with pytest.raises(ValueError, match="must not be empty"):
        average([])



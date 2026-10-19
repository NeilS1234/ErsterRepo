
def add(a: float, b: float) -> float:
    """Add two numbers.

    Args:
        a: First number.
        b: Second number.

    Returns:
        The sum of both numbers.
    """
    return a + b


def average(numbers: list[float]) -> float:
    """Calculate the average of a list of numbers.

    Args:
        numbers: List of numbers.

    Returns:
        The average value.

    Raises:
        ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("The list must not be empty.")

    return sum(numbers) / len(numbers)

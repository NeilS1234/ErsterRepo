
def add(a: int, b: int) -> int:
    """Add two numbers.

    Args:
        a: First number.
        b: Second number.

    Returns:
        The sum.
    """
    return a + b


def main() -> None:
    """Run the program."""
    result = add(2, 3)
    print(result)


if __name__ == "__main__":
    main()

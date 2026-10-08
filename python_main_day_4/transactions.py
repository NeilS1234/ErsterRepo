transactions = [25, 60, 15, 100, 45]


def validate_input(transaction: int | float) -> bool:
    """Prüft, ob eine Transaktion eine Zahl ist."""
    return isinstance(transaction, (int, float))


def calculate_total(transactions: list[int | float]) -> int | float:
    """Berechnet die Summe aller gültigen Transaktionen."""
    total = 0

    for transaction in transactions:
        if validate_input(transaction):
            total += transaction

    return total


def classify_record(transaction: int | float) -> str:
    """Klassifiziert eine Transaktion."""
    if transaction >= 50:
        return "Große Transaktion"
    else:
        return "Kleine Transaktion"


def format_output(transaction: int | float, classification: str) -> str:
    """Formatiert die Transaktion und ihre Klassifizierung."""
    return f"{transaction} -> {classification}"



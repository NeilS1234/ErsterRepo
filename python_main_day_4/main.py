from transactions import (
    validate_input,
    calculate_total,
    classify_record,
    format_output
)


transactions = [25, 60, 15, 100, 45]


def main() -> None:
    """Führt die Prüfung, Klassifizierung und Summierung aus."""
    for transaction in transactions:
        if validate_input(transaction):
            classification = classify_record(transaction)

            print(format_output(transaction, classification))

            if transaction >= 50:
                print("Passt zur Bedingung:", transaction)
        else:
            print("Ungültige Eingabe:", transaction)

    total = calculate_total(transactions)
    print("Gesamtbetrag:", total, "Euro")


if __name__ == "__main__":
    main()
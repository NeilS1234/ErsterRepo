transactions = [25, 60, 15, 100, 45]


def validate_input(transaction):
    return isinstance(transaction, (int, float))


def calculate_total(transactions):
    total = 0

    for transaction in transactions:
        total = total + transaction

    return total


def classify_record(transaction):
    if transaction >= 50:
        return "Große Transaktion"
    else:
        return "Kleine Transaktion"


def format_output(transaction, classification):
    return str(transaction) + " -> " + classification


# Transaktion überprüfen und klassifizieren
for transaction in transactions:

    if validate_input(transaction):
        classification = classify_record(transaction)

        print(format_output(transaction, classification))

        # Transaktionen ab 50 Euro anzeigen
        if transaction >= 50:
            print("Passt zur Bedingung:", transaction)
    else:
        print("Ungültige Eingabe:", transaction)


# Gesamtbetrag berechnen
total = calculate_total(transactions)

# Gesamtbetrag ausgeben
print("Gesamtbetrag:", total, "Euro")

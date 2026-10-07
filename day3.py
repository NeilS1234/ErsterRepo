transactions = [25, 60, 15, 100, 45]

total = 0

for transaction in transactions:

    # Bedingung nur einmal prüfen
    ist_gross = transaction >= 50

    # Datensatz klassifizieren
    if ist_gross:
        print(f"{transaction} -> Große Transaktion")
        print(f"Passt zur Bedingung: {transaction}")
    else:
        print(f"{transaction} -> Kleine Transaktion")

    # Gesamtbetrag berechnen
    total = total + transaction

print(f"Gesamtbetrag: {total} Euro")




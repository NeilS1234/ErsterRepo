transactions = [25, 60, 15, 100, 45] 

total = 0

for transaction in transactions:

    # Datensatz klassifizieren
    if transaction >= 50:
        print(transaction, "-> Große Transaktion")
    else:
        print(transaction, "-> Kleine Transaktion")

    # Transaktionen ab 50 € finden
    if transaction >= 50:
        print("Passt zur Bedingung:", transaction)

    # Gesamtbetrag berechnen
    total = total + transaction

print("Gesamtbetrag:", total, "Euro")

#Was macht das Programm?

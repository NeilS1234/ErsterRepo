import csv
import os

# Ordner herausfinden, in dem dieses Python-Programm liegt
ordner = os.path.dirname(os.path.abspath(__file__))

# Pfad zur CSV-Datei erstellen
csv_datei = os.path.join(ordner, "records.csv")

# Pfad für die Ergebnisdatei erstellen
ergebnis_datei = os.path.join(ordner, "result.csv")


# CSV-Datei öffnen
try:
    with open(csv_datei, "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        valid_records = []
        invalid_records = 0

        # Jede Zeile lesen
        for row in reader:

            name = row["Name"]
            alter = row["Alter"]
            stadt = row["Stadt"]

            # Prüfen, ob etwas fehlt
            if name == "" or alter == "" or stadt == "":
                invalid_records += 1
                continue

            # Prüfen, ob Alter eine Zahl ist
            try:
                alter = int(alter)

            except ValueError:
                invalid_records += 1
                continue

            # Prüfen, ob Alter sinnvoll ist
            if alter < 0 or alter > 120:
                invalid_records += 1
                continue

            # Datensatz ist gültig
            valid_records.append(row)


except FileNotFoundError:
    print("FEHLER: records.csv wurde nicht gefunden.")
    print("Gesuchter Ort:")
    print(csv_datei)
    exit()


# Zusammenfassung
print()
print("----- Zusammenfassung -----")
print("Gültige Datensätze:", len(valid_records))
print("Ungültige Datensätze:", invalid_records)
print("Gesamt:", len(valid_records) + invalid_records)


# Ergebnis speichern
with open(ergebnis_datei, "w", newline="", encoding="utf-8") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["Name", "Alter", "Stadt"]
    )

    writer.writeheader()

    for record in valid_records:
        writer.writerow(record)


print()
print("Fertig!")
print("Die Datei result.csv wurde erstellt.")



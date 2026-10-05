import csv

# CSV-Datei öffnen
with open("records.csv", "r") as file:
    reader = csv.DictReader(file)

    valid_records = []
    invalid_records = 0

    # Jede Zeile lesen
    for row in reader:

        name = row["Name"]
        alter = row["Alter"]
        stadt = row["Stadt"]
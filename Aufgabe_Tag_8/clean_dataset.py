import pandas as pd
from pathlib import Path

# Ordner finden
ordner = Path(__file__).parent

# 1. CSV-Datei erstellen, falls sie leer ist
datei = ordner / "messy_dataset.csv"

if not datei.exists() or datei.stat().st_size == 0:
    daten = """vorname,alter,Stadt,Gehalt,Datum
 max mustermann ,25,Berlin,3000,15.01.2024
ANNA SCHMIDT,32,berlin,4200,15.02.2023
Peter Müller,150,Hamburg,3500,10.03.2023
Lisa Weber,28,Munich,2800,20.04.2024
John Smith,35,London,5000,12.05.2022
John Smith,35,London,5000,12.05.2022
Maria Garcia,,Madrid,3900,18.06.2023
Tom Brown,29,HAMBURG,-1200,22.07.2024
Sarah Jones,31,London,4500,falsches_datum
David Lee,27,Berlin,NA,14.09.2023
emma wilson,24,munich,3200,01.10.2024
"""
    datei.write_text(daten, encoding="utf-8")

# 2. CSV-Datei laden
df = pd.read_csv(datei)

report = []

print("Original data:")
print(df)


# 3. Missing values
# Fehlendes Alter durch 21 ersetzen

anzahl = df["alter"].isna().sum()

if anzahl > 0:
    df["alter"] = df["alter"].fillna(21)

    report.append([
        "Missing age",
        "Replaced missing age with 21",
        "A value is needed for this example",
        anzahl
    ])


# 4. Removing duplicates

anzahl = df.duplicated().sum()

if anzahl > 0:
    df = df.drop_duplicates()

    report.append([
        "Duplicate rows",
        "Removed duplicate rows",
        "Duplicates can cause incorrect results",
        anzahl
    ])


# 5. Correcting data types

df["alter"] = pd.to_numeric(df["alter"], errors="coerce")
df["Gehalt"] = pd.to_numeric(df["Gehalt"], errors="coerce")

# Negative salaries are invalid for this example
anzahl = (df["Gehalt"] < 0).sum()

if anzahl > 0:
    df.loc[df["Gehalt"] < 0, "Gehalt"] = pd.NA

    report.append([
        "Negative salary",
        "Changed negative salary to an empty value",
        "Salary should not be negative",
        anzahl
    ])


# 6. Cleaning strings

for spalte in ["vorname", "Stadt"]:
    vorher = df[spalte].copy()

    df[spalte] = df[spalte].str.strip()
    df[spalte] = df[spalte].str.title()

    anzahl = (vorher != df[spalte]).sum()

    if anzahl > 0:
        report.append([
            "Inconsistent text in " + spalte,
            "Removed spaces and used title case",
            "Text should be consistent",
            anzahl
        ])


# 7. Working with dates

alte_daten = df["Datum"].copy()

df["Datum"] = pd.to_datetime(
    df["Datum"],
    format="%d.%m.%Y",
    errors="coerce"
)

anzahl = (alte_daten.notna() & df["Datum"].isna()).sum()

if anzahl > 0:
    report.append([
        "Invalid dates",
        "Changed invalid dates to empty values",
        "The correct date is unknown",
        anzahl
    ])


# 8. Renaming columns

df = df.rename(columns={
    "vorname": "Name",
    "alter": "Alter"
})

report.append([
    "Column names",
    "Renamed vorname to Name and alter to Alter",
    "Clear column names are easier to understand",
    2
])


# 9. Save cleaned CSV

df.to_csv(
    ordner / "cleaned_dataset.csv",
    index=False,
    date_format="%Y-%m-%d"
)


# 10. Save cleaning report

bericht = pd.DataFrame(report, columns=[
    "Issue Found",
    "Chosen Correction",
    "Reason",
    "Affected Records"
])

bericht.to_csv(
    ordner / "cleaning_report.csv",
    index=False
)


# 11. Show results

print("\nCleaned data:")
print(df)

print("\nCleaning report:")
print(bericht)

print("\nFinished!")
print("Created: cleaned_dataset.csv")
print("Created: cleaning_report.csv")
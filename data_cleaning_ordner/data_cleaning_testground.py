import pandas as pd


df = pd.read_csv("C:\\Users\\2918965\\OneDrive - EDEKA\\Desktop\\ErsterRepo\\data_cleaning_ordner\\arbeiter.csv")

# 1. Handling missing values
# Fehlende Werte durch einen bestimmten Wert ersetzen
df["Alter"] = df["Alter"].fillna(21)


# 2. Removing duplicates
# Doppelte Zeilen entfernen
df = df.drop_duplicates()


# 3. Correcting data types
# Datentyp einer Spalte ändern
df["Alter"] = df["Alter"].astype(int)


# 4. Cleaning strings
# Leerzeichen entfernen und Text formatieren
df["Name"] = df["Name"].str.strip()
df["Name"] = df["Name"].str.title()


# 5. Working with dates
# String in ein richtiges Datum umwandeln
df["Datum"] = pd.to_datetime(df["Datum"], format="%d.%m.%Y")


# 6. Renaming columns
# Spaltennamen ändern
df = df.rename(columns={
    "vorname": "Name",
    "alter": "Age"
})

print (df)
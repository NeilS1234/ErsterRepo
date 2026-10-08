import pandas as pd

# CSV-Datei einlesen

df = pd.read_csv(r"C:\Users\2918965\OneDrive - EDEKA\Desktop\ErsterRepo\exercise_day_7\kundendaten.csv") 

print(df)


# Erste 5 Zeilen anzeigen
print("Erste 5 Zeilen:")
print(df.head())

# Spalten anzeigen
print("\nSpalten:")
print(df.columns)

# Datentypen anzeigen
print("\nDatentypen:")
print(df.dtypes)

# Übersicht über die Daten
print("\nÜbersicht:")
df.info()

# Anzahl der Zeilen
print("\nAnzahl der Zeilen:")
print(df.shape[0])

# Anzahl der Spalten
print("\nAnzahl der Spalten:")
print(df.shape[1])

# Erste Zeile auswählen
print("\nErste Zeile:")
print(df.iloc[0])

# Kunden über 30 Jahre
print("\nKunden über 30 Jahre:")
print(df[df["Alter"] > 30])

# Kunden mit einem Jahreseinkommen über 50.000 €
print("\nKunden mit einem Jahreseinkommen über 50.000 €:")
print(df.query("Jahreseinkommen > 50000"))

# Durchschnittliches Alter
print("\nDurchschnittliches Alter:")
print(df["Alter"].mean())

# Median des Alters
print("\nMedian des Alters:")
print(df["Alter"].median())

# Jüngster Kunde
print("\nJüngster Kunde:")
print(df["Alter"].min())

# Ältester Kunde
print("\nÄltester Kunde:")
print(df["Alter"].max())

# Anzahl der Kunden
print("\nAnzahl der Kunden:")
print(df["Alter"].count())

# Summe aller Käufe
print("\nSumme aller Käufe:")
print(df["Anzahl_Kaeufe"].sum())

# Standardabweichung des Alters
print("\nStandardabweichung des Alters:")
print(df["Alter"].std())

# Numerische Zusammenfassung
print("\nNumerische Zusammenfassung:")
print(df.describe())

# Fehlende Werte
print("\nFehlende Werte:")
print(df.isnull().sum())

# Duplikate
print("\nAnzahl der Duplikate:")
print(df.duplicated().sum())

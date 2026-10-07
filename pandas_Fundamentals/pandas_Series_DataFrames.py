import pandas as pd

daten = pd.read_csv("mitarbeiter.csv")


print(daten.head())
print(daten.columns)
print(daten.dtypes)

buero = daten[daten["abteilung"] == "Büro"]

print(daten.describe())




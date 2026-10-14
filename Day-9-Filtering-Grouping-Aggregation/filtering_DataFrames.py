import pandas as pd 

df = pd.read_csv(r"C:\Users\2918965\OneDrive - EDEKA\Desktop\ErsterRepo\Day-9-Filtering-Grouping-Aggregation\data.csv")

#Prüft welche Spalten überhaupt vorhanden sind
print(df.columns)

print(df[df["Preis"] >= 3])

print(df[(df["Preis"] >= 3) & (df["Menge"] > 5)])

#vom günstigsten zum teuersten sortieren
print(df.sort_values("Preis"))

#vom teuersten zum günstigsten sortieren
print(df.sort_values("Preis", ascending=False)) 

#mehrere Spalten sortieren, zuerst nach Kategorie und dann nach Preis 
print(df.sort_values(["Kategorie", "Preis"]))

#Gruppieren nach Kategorie und die Summe der Menge berechnen
print(df.groupby("Kategorie")["Menge"].sum())

#Durchschnittpreis aller Produkte 
print(df["Preis"].mean())

#mehrere Kennzahlen auf einmal berechnen, min, max, mean, sum
print(df["Preis"].agg(["min", "max", "mean", "sum"]))

#durchschnittspreis und Maximalpreis pro Kategorie berechnen
print(df.groupby("Kategorie")["Preis"].agg(["mean", "max"]))

#Gesamtwert pro Produkt berechnen, Preis * Menge
df["Gesamtwert"] = df["Preis"] * df["Menge"]
print(df)

#Rabattpreis berechnen, 10% Rabatt auf den Preis
df["Rabattpreis"] = df["Preis"] * 0.9
print(df)
#Das Prodkt als teuer kennzeichnen 
df["Teuer"] = df["Preis"] >= 3
print(df)
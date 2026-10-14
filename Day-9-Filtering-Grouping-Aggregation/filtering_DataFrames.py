import pandas as pd 

df = pd.read_csv(r"C:\Users\2918965\OneDrive - EDEKA\Desktop\ErsterRepo\Day-9-Filtering-Grouping-Aggregation\data.csv")

#Prüft welche Spalten überhaupt vorhanden sind
print(df.columns)

print(df[df["Preis"] >= 3])

print(df[(df["Preis"] >= 3) & (df["Menge "] > 5)])

#vom günstigsten zum teuersten sortieren
print(df.sort_values("Preis"))

#vom teuersten zum günstigsten sortieren
print(df.sort_values("Preis", ascending=False)) 

#mehrere Spalten sortieren, zuerst nach Kategorie und dann nach Preis 
print(df.sort_values(["Kategorie", "Preis"]))

#Gruppieren nach Kategorie und die Summe der Menge berechnen
print(df.groupby("Kategorie")["Menge "].sum())
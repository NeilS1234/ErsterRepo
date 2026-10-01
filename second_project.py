# 3 Datenstrukturen: Tupel, Dictionaries und eine Liste

# 1. Ein Tupel für Abteilungen (das sind feste Werte, die bleiben)
abteilungen = ("Büro", "Lager")

# 2. Dictionaries für unsere 5 Mitarbeiter (Name und Job)
alle_mitarbeiter = [
{"name": "Anna", "job": "Chefin", "abteilung": "Büro"},
{"name": "Ben", "job": "Helfer", "abteilung": "Lager"},
{"name": "Clara", "job": "Planerin", "abteilung": "Büro"},
{"name": "David", "job": "Fahrer", "abteilung": "Lager"},
{"name": "Eva", "job": "Verkäuferin", "abteilung": "Büro"}
]

#  1. Alle Datensätze anzeigen 
print("\n1. Alle Datensätze:")
print(alle_mitarbeiter)


#  2. Gesamtzahl der Datensätze 
anzahl = len(alle_mitarbeiter)
print(f"\n2. Gesamtzahl der Mitarbeiter: {anzahl}")


#  3. Ausgewählte Informationen 
print("\n3. Name und Job:")
print(f"{alle_mitarbeiter[0]['name']} — {alle_mitarbeiter[0]['job']}")
print(f"{alle_mitarbeiter[1]['name']} — {alle_mitarbeiter[1]['job']}")
print(f"{alle_mitarbeiter[2]['name']} — {alle_mitarbeiter[2]['job']}")
print(f"{alle_mitarbeiter[3]['name']} — {alle_mitarbeiter[3]['job']}")
print(f"{alle_mitarbeiter[4]['name']} — {alle_mitarbeiter[4]['job']}")



#    4. Eine kleine Zusammenfassung 
print("\n4. Zusammenfassung:")
print(f"Anzahl: {anzahl}")
print(f"Abteilungen: {abteilungen}") 

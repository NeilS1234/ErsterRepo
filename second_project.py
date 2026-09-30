# 3 Datenstrukturen: Tupel, Dictionaries und eine Liste

# 1. Ein Tupel für Abteilungen (das sind feste Werte, die bleiben)
abteilungen = ("Büro", "Lager")

# 2. Dictionaries für unsere 5 Mitarbeiter (Name und Job)
mitarbeiter_1 = {"name": "Anna", "job": "Chefin"}
mitarbeiter_2 = {"name": "Ben", "job": "Helfer"}
mitarbeiter_3 = {"name": "Clara", "job": "Planerin"}
mitarbeiter_4 = {"name": "David", "job": "Fahrer"}
mitarbeiter_5 = {"name": "Eva", "job": "Verkäuferin"}

# 3. Eine Liste, in die alle 5 Mitarbeiter reingepackt werden
alle_mitarbeiter = [mitarbeiter_1, mitarbeiter_2, mitarbeiter_3, mitarbeiter_4, mitarbeiter_5]


#  1. Alle Datensätze anzeigen 
print("\n1. Alle Datensätze:")
print(alle_mitarbeiter)


#  2. Gesamtzahl der Datensätze 
print("\n2. Gesamtzahl der Mitarbeiter:")
anzahl = len(alle_mitarbeiter)
print(anzahl)


#  3. Ausgewählte Informationen 
print("\n3. Nur Name und Job:")
for m in alle_mitarbeiter:
    print(m["name"], "-", m["job"])


#    4. Eine kleine Zusammenfassung 
print("\n4. Zusammenfassung:")
print("Anzahl:", anzahl)
print("Abteilungen:", abteilungen)

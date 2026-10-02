print(bool("False"))  # Output: True

students_count = 30
rating = 4.5
is_published = False 
course_name = "Python Programming"
print(students_count)


name = "Anna"        # String (Text)
alter = 25           # Integer (Ganze Zahl)
preis = 19.99        # Float (Kommazahl mit Punkt)
ist_aktiv = True     # Boolean (Wahr oder Falsch)




# Liste (veränderlich, eckige Klammern)
fruechte = ["Apfel", "Banane", "Kirsche"]

# Tupel (unveränderlich, runde Klammern)
wochentage = ("Montag", "Dienstag", "Mittwoch")

# Dictionary (Schlüssel-Wert-Paare, geschwungene Klammern)
benutzer = {"name": "Max", "punkte": 42}

# Set (nur eindeutige Werte, keine doppelten Einträge)
einzigartig = {1, 2, 3, 3}  # Die zweite 3 wird ignoriert




name = "Tim"
alter = 20

# Das 'f' vor den Anführungszeichen erlaubt es, Variablen direkt einzubauen:
text = f"Hallo, ich heiße {name} und bin {alter} Jahre alt."
print(text)


#New task if else elif

age = int(input("Bitte geben Sie Ihr Alter ein: "))

if age < 18:
    print("Du bist minderjährig.")
elif age == 18:
    print("Du bist genau 18.")
elif age == 19:
    print("Du bist genau 19.")
else:
    print("Du bist volljährig.")

#new task logische operatoren 

print("Willkommen in der Lotterie!")
n1 = int(input("Bitte geben Sie die erste Zahl ein (zwischen 1 und 50): "))
n2 = int(input("Bitte geben Sie die zweite Zahl ein (zwischen 1 und 50): "))
n3 = int(input("Bitte geben Sie die dritte Zahl ein (zwischen 1 und 50): "))


#Gewinnzahlen 1:7
#Gewinnzahlen 2:14
#Gewinnzahlen 3:21

if n1 == 7:
    if n2 == 14:
        if n3 == 21:
            print("Herzlichen Glückwunsch! Sie haben alle drei Gewinnzahlen getroffen!")
        else:
            print("Du hast verloren!")
    else:
        print("Du hast verloren!")
else:
    print("Du hast verloren!")
    

if n1 == 7 and n2 == 14 and n3 == 21: # vereinfacht die verschachtelten if-Bedingungen 
    print("Herzlichen Glückwunsch! Sie haben alle drei Gewinnzahlen getroffen!")
else:
    print("Du hast verloren!")



#new task while loop
counter = 5
while counter < 10:
    print("Hier steht Code , der wiederholt ausgeführt wird")
    counter += 1  # Erhöht den Zähler um 1, um eine Endlosschleife zu vermeiden 


# for loop
for element in [1, 2, 3, 4, 5]:
    print(element)  # Gibt jedes Element der Liste aus

# Zählerschschleife 
for element in range(5, 10,  2):  # range(5, 10) erzeugt die Zahlen 5 bis 9
    print(element)  # Gibt die Zahlen von 5 bis 9 aus


zahlen = [10, 20, 30]
gesamt = sum(zahlen)


def say_hello(first_name, last_name):
    print("Hallo " + first_name + " " + last_name)
    print("Willkommen zu meinem Programm.")



print(type(say_hello("Fabian", "Mustermann")))



def maximum(a, b):
    if a > b:
        return a
    else:
        return b

result = maximum(5, 10)  # Gibt 10 zurück
print(result)  # Ausgabe: 10
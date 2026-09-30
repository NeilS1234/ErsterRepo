# Feedback 1 — Tag 1 und Tag 2

## Gesamtbewertung

Du hast einen guten Anfang gemacht. Die wichtigsten Python-Programme für Tag 1 und Tag 2 laufen erfolgreich, und die Lösung für Tag 2 zeigt, dass du Listen, Tupel, Dictionaries, Schleifen und `len()` verstanden hast.

**Status:** Die grundlegenden Anforderungen der Aufgaben sind erfüllt. Bei der Dokumentation, dem Codestil und dem GitHub-Workflow sind noch einige Verbesserungen erforderlich.

## Aufgabe von Tag 1

Die Aufgabe bestand darin, das Repository `python-apprenticeship` zu erstellen, eine README-Datei hinzuzufügen, ein Python-Programm mit einer Begrüßung und grundlegenden persönlichen Informationen zu schreiben und die Arbeit auf GitHub hochzuladen.

### Was du gut gemacht hast

- Du hast ein GitHub-Repository erstellt und eine README-Datei hinzugefügt.
- `first_project.py` läuft ohne Fehler.
- Das Programm gibt eine Begrüßung und die angeforderten persönlichen Informationen aus.
- Dein Commit-Verlauf zeigt, dass du experimentiert, Dateien korrigiert und Git-Befehle geübt hast.

### Was du verbessern solltest

- Die README enthält noch Platzhalter aus der Vorlage, zum Beispiel „An in-depth paragraph about your project.“ Ersetze sie durch eine echte Projektbeschreibung.
- Vervollständige die README-Abschnitte zur Ausführung des Programms und zur Hilfe. Füge einen Beispielbefehl wie `python first_project.py` hinzu.
- Korrigiere Rechtschreibfehler wie `ptoject`, `requiered` und `git`, wenn Git gemeint ist.
- Ergänze die verwendeten YouTube-Quellen, eine kurze Zusammenfassung des Gelernten und noch offene Fragen. Diese Informationen gehören zu den täglichen Abgabeanforderungen.
- Verwende f-Strings für die Ausgabe von Werten, zum Beispiel: `print(f"Name: {name}")`.

## Aufgabe von Tag 2

Die Aufgabe bestand darin, Informationen zu fünf Mitarbeitern oder Produkten zu speichern, mindestens drei Datenstrukturen zu verwenden, alle Datensätze anzuzeigen, die Gesamtzahl der Datensätze auszugeben, ausgewählte Informationen aus jedem Datensatz darzustellen und eine formatierte Zusammenfassung auszugeben.

### Was du gut gemacht hast

- `second_project.py` läuft ohne Fehler.
- Du hast genau fünf Mitarbeiterdatensätze erstellt.
- Du hast drei verlangte Datenstrukturen verwendet: ein Tupel, Dictionaries und eine Liste.
- Du hast alle Datensätze angezeigt und mit `len()` die richtige Gesamtzahl berechnet.
- Du hast eine Schleife verwendet, um Name und Tätigkeit jedes Mitarbeiters auszugeben.
- Deine Kommentare machen die Lernabsicht gut nachvollziehbar.

### Was du verbessern solltest

- Erstelle die Mitarbeiterliste direkt, anstatt zuerst fünf nummerierte Variablen anzulegen. Das ist kürzer und lässt sich leichter erweitern.
- Ordne jedem Mitarbeiter eine Abteilung zu. Derzeit wird das Abteilungs-Tupel ausgegeben, ist aber mit keinem Mitarbeiterdatensatz verbunden.
- Verwende f-Strings für die Mitarbeiter- und Zusammenfassungsausgabe, zum Beispiel: `print(f"{employee['name']} — {employee['job']}")`.
- Gib alle Datensätze mit einer Schleife aus, anstatt die rohe Liste zu drucken. Dadurch wird die Ausgabe besser lesbar.
- In `training_field.py` ergibt `bool("False")` den Wert `True`, weil jede nicht leere Zeichenkette als wahr gilt. Stelle sicher, dass du den Unterschied zwischen der Zeichenkette `"False"` und dem booleschen Wert `False` erklären kannst.
- Ergänze die verwendeten Videos, die Lernzusammenfassung und die offenen Fragen für Tag 2.

## Ergebnisse der Codequalitätsprüfung

- Alle drei Python-Dateien werden erfolgreich ausgeführt.
- mypy meldet keine Probleme.
- Ruff meldet mit den aktuellen Standardregeln keine Probleme.
- Flake8 meldet Stilprobleme, darunter eine Zeile mit mehr als 79 Zeichen, Leerzeichen am Zeilenende, zu viele Leerzeilen und eine Leerzeile am Dateiende.

Diese Stilprobleme verhindern die Ausführung der Programme nicht. Ihre Behebung macht den Code jedoch professioneller und leichter überprüfbar.

## Feedback zu Git und GitHub

- Du hast 19 Commits erstellt. Das zeigt, dass du Git regelmäßig geübt hast.
- Einige Commit-Nachrichten wie `commit` und `second_project.py` erklären die Änderung nicht. Verwende besser Nachrichten wie `feat: add employee summary assignment` oder `docs: complete project instructions`.
- Das Repository enthält derzeit nur den Branch `main` und keine Pull Requests. Erstelle für die nächste Aufgabe einen eigenen Branch, lade ihn hoch, öffne einen Pull Request und merge ihn nach dem Review.
- Vermeide es, unfertige Experimente direkt auf `main` zu committen. Ein Lern- oder Feature-Branch bietet dir einen sicheren Ort zum Üben.

## Erforderliche nächste Verbesserungen

1. Ersetze alle README-Platzhalter durch echte Projektinformationen und Ausführungsanweisungen.
2. Ergänze die Lernquellen, die Lernzusammenfassungen und die Fragen für Tag 1 und Tag 2.
3. Überarbeite `second_project.py` zu einer einzigen Liste von Mitarbeiter-Dictionaries und füge jedem Mitarbeiter eine Abteilung hinzu.
4. Verwende f-Strings und verbessere die Formatierung der Ausgabe.
5. Behebe alle Flake8-Meldungen.
6. Reiche die nächste Aufgabe über einen Branch und einen Pull Request ein.

Du hast den wichtigen funktionalen Teil beider Aufgaben abgeschlossen. Dein nächster Schritt ist, das Repository genauso klar und professionell zu gestalten wie den funktionierenden Code.

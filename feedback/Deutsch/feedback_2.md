# Feedback 2 — Tag 3 bis Tag 6

## Umfang des Reviews

Dieses Review umfasst die nach Feedback 1 bis zum 6. Oktober 2026 vorgenommenen Commits. Bewertet werden die Aufgaben für Tag 3, 4 und 5, der aktuelle Stand von Tag 6, die in Feedback 1 verlangten Verbesserungen sowie der Git- und GitHub-Workflow.

## Übersicht der Abgaben

| Arbeitstag | Erwartete Aufgabe | Aktivität im Repository | Status |
|---|---|---:|---|
| 1. Oktober 2026 | Tag 3 | 13 Commits einschließlich Merges | Abgegeben |
| 2. Oktober 2026 | Tag 4 | 7 Commits einschließlich Merges | Abgegeben |
| 5. Oktober 2026 | Tag 5 | 10 Commits | Abgegeben |
| 6. Oktober 2026 | Tag 6 | 3 Commits zum Zeitpunkt des Reviews | In Bearbeitung |

In diesem Review-Zeitraum gibt es keinen Arbeitstag ohne Commit. Der 3. und 4. Oktober waren Wochenendtage und werden nicht als fehlende Abgaben gezählt.

## Nachverfolgung von Feedback 1

### Erledigte Verbesserungen

- Die README enthält jetzt eine echte Projektbeschreibung und dokumentiert die Lerntage.
- Du hast für mehrere Tage YouTube-Lernquellen hinzugefügt.
- `second_project.py` verwendet jetzt eine einzige Liste mit Mitarbeiter-Dictionaries.
- Die Abteilungen sind nun einzelnen Mitarbeiterdatensätzen zugeordnet.
- Du hast f-Strings in die Lösung für Tag 2 aufgenommen.
- Du hast Branches erstellt und sechs Pull Requests erfolgreich gemergt.

### Noch offene Verbesserungen

- Gib die Mitarbeiter mit einer Schleife aus, anstatt einzeln auf die Positionen `0` bis `4` zuzugreifen.
- Ergänze klare Ausführungsanweisungen in der README.
- Ergänze für jeden Tag eine kurze Lernzusammenfassung und offene Fragen, nicht nur Links zu Lernquellen.
- Entferne den verbleibenden Vorlagentext aus den Abschnitten Author und Acknowledgments.
- Behebe die noch offenen mypy-, Ruff- und Flake8-Meldungen.

## Tag 3 — Bedingungen und Schleifen

### Was du gut gemacht hast

- `day3.py` läuft erfolgreich.
- Das Programm klassifiziert jede Transaktion als groß oder klein.
- Es erkennt Transaktionen, die die Bedingung erfüllen.
- Es berechnet die korrekte Gesamtsumme von 245 Euro.
- Die Lösung verwendet eine `for`-Schleife und Bedingungen.
- Du hast für diese Aufgabe Branches und Pull Requests geübt.

### Was du verbessern solltest

- Die Bedingung `transaction >= 50` wird zweimal geprüft. Speichere das Ergebnis oder fasse die zusammengehörenden Ausgaben zusammen, um doppelte Logik zu vermeiden.
- Verwende f-Strings, damit die Ausgabe klarer und mit dem vorherigen Lernthema konsistent ist.
- Verwende aussagekräftigere Commit-Nachrichten. Nachrichten wie `updat...` erklären nicht, was geändert wurde.
- Liste die tatsächlich angesehenen Videos einzeln auf, anstatt nur zu erwähnen, dass weitere Videos aus der Reihe angesehen wurden.

**Bewertung:** Abgeschlossen. Die funktionalen Anforderungen sind erfüllt.

## Tag 4 — Funktionen und Module

### Was du gut gemacht hast

- `day4.py` läuft erfolgreich und erzeugt das erwartete Ergebnis.
- Die Logik von Tag 3 wurde in Funktionen für Validierung, Berechnung, Klassifizierung und Formatierung aufgeteilt.
- Die Funktionsnamen beschreiben ihre Zuständigkeiten verständlich.
- Die Funktionen geben Werte zurück, anstatt die gesamte Logik direkt in Print-Anweisungen zu platzieren.

### Was du verbessern solltest

- `calculate_total()` verwendet die Validierungslogik nicht. Ein ungültiger Eintrag würde bei der Ausgabe übersprungen, könnte aber dennoch die Summenberechnung zum Absturz bringen.
- Platziere die Programmausführung in einer `main()`-Funktion und rufe sie mit `if __name__ == "__main__":` auf.
- Ergänze Type Hints und kurze Docstrings, damit die erwarteten Ein- und Ausgaben jeder Funktion klar sind.
- Verwende in `format_output()` einen f-String anstelle einer String-Verkettung.
- Der Themenbereich „Module“ wird noch nicht demonstriert. Verschiebe als nächsten Schritt wiederverwendbare Funktionen in ein separates Modul und importiere sie in das Hauptprogramm.

**Bewertung:** Abgeschlossen, mit einigen empfohlenen strukturellen Verbesserungen.

## Tag 5 — Dateien und Fehlerbehandlung

### Was du gut gemacht hast

- `aufgabe_tag_5/aufgabe_5.py` liest Daten aus einer CSV-Datei und schreibt eine Ergebnisdatei.
- Das Programm prüft auf fehlende Werte, ungültige Zahlen und unrealistische Alterswerte.
- Es zählt gültige und ungültige Datensätze und gibt eine hilfreiche Zusammenfassung aus.
- Es behandelt eine fehlende Eingabedatei.
- Das Programm funktioniert bei der Ausführung und erzeugt aus der aktuellen Eingabedatei fünf gültige Datensätze.
- Zusätzliche Übungsdateien zeigen CSV, JSON, Exceptions, Dataclasses und Imports.

### Was du verbessern solltest

- Die eingecheckte Datei `result.csv` enthält nur vier Datensätze, während die aktuelle Eingabedatei fünf gültige Datensätze enthält. Erzeuge Ausgabedateien neu, wenn sich Eingabedaten oder Verarbeitungslogik ändern.
- Teile die CSV-Verarbeitung in Funktionen zum Lesen, Validieren, Zusammenfassen und Schreiben auf.
- Ergänze einen `main()`-Einstiegspunkt, anstatt alles direkt auf Modulebene auszuführen.
- Behandle fehlende CSV-Spalten kontrolliert, anstatt davon auszugehen, dass `Name`, `Alter` und `Stadt` immer vorhanden sind.
- Das konvertierte Alter wird nicht in den Datensatz zurückgeschrieben und bleibt deshalb in `valid_records` eine Zeichenkette.
- Ergänze eine Python-`.gitignore`. Die kompilierte Datei `data/__pycache__/person.cpython-313.pyc` wird aktuell von Git verfolgt und sollte nicht eingecheckt werden.
- Ergänze eine Abhängigkeitsdatei, falls externe Pakete benötigt werden. Dokumentiere mindestens, dass das Programm von Tag 5 nur die Python-Standardbibliothek verwendet.
- `data/main.py` öffnet die Ausgabedatei im Append-Modus und schreibt den Header bei jeder Ausführung erneut. Dadurch können doppelte Header und Datensätze entstehen.

**Bewertung:** Abgeschlossen. Die Kernaufgabe funktioniert, aber Repository-Hygiene und Konsistenz der Ausgabedateien müssen verbessert werden.

## Tag 6 — NumPy-Grundlagen

### Aktueller Fortschritt

- NumPy wird korrekt importiert.
- Eine Python-Liste wird in ein NumPy-Array umgewandelt.
- Das Programm demonstriert vektorisierte Multiplikation und vergleicht sie mit einer List Comprehension.
- Es demonstriert einen expliziten NumPy-Integer-Datentyp.

### Noch erforderliche Arbeit

Die Aufgabe für Tag 6 ist zum Zeitpunkt des Reviews noch nicht abgeschlossen. Folgende Werte müssen noch berechnet werden:

- Summe
- Mittelwert
- Median
- Minimum und Maximum
- Standardabweichung
- Prozentuale Abweichung jedes Werts vom Mittelwert

Verwende für diese Berechnungen NumPy-Operationen und beschrifte jede Ausgabe eindeutig. Ergänze außerdem die YouTube-Quellen, die Lernzusammenfassung und die offenen Fragen für Tag 6 in der README.

**Bewertung:** In Bearbeitung am 6. Oktober 2026.

## Ergebnisse der Codequalitätsprüfung

- `day3.py`, `day4.py`, die Aufgabe von Tag 5 und das aktuelle NumPy-Programm werden erfolgreich ausgeführt.
- mypy meldet 4 Fehler in `data/person.py` und `training_field.py`.
- Ruff meldet 2 Probleme: eine doppelt definierte Funktion und einen Import unterhalb von ausführbarem Code.
- Flake8 meldet 60 Stilprobleme im Repository. Die meisten betreffen Leerzeichen, Leerzeilen, Einrückung, Zeilenlänge und fehlende abschließende Zeilenumbrüche.

Die wichtigsten inhaltlichen Meldungen sind:

- `Person.from_dict()` kann fehlende Werte oder ein Alter als Zeichenkette an Felder übergeben, die als `str` und `int` deklariert sind.
- `say_hello()` ist in `training_field.py` zweimal definiert.
- `data/main2.py` enthält einen Import nach bereits ausgeführtem Code.

## Feedback zu Git und GitHub

- Du hast gut auf das vorherige Feedback reagiert und Branches sowie Pull Requests verwendet.
- Sechs Pull Requests wurden gemergt. Damit hast du den vollständigen GitHub-Kollaborationsablauf demonstriert.
- Für dasselbe kleine Transaktionsprogramm wurden mehrere Pull Requests geöffnet. Versuche, eine Aufgabe in einem fokussierten Branch und Pull Request abzuschließen, sofern keine wirklich separate Korrektur notwendig ist.
- Viele Commit-Nachrichten sind weiterhin zu allgemein, darunter Varianten von `update_readme`, `training_save` und `numpy_test`.
- Verwende semantische und handlungsorientierte Nachrichten wie `feat: complete day 5 CSV validation` oder `docs: add day 6 learning resources`.
- Verwende für zukünftige Arbeiten das Branch-Format des Unternehmens, zum Beispiel `feature/day6NumpyAnalysis` oder `bugfix/day5ResultSync`.

## Erforderliche nächste Schritte

1. Vervollständige alle Berechnungen für Tag 6 mit NumPy.
2. Erzeuge die korrekte `result.csv` für Tag 5 neu und committe sie.
3. Ergänze `.gitignore` und entferne Python-Cache-Dateien aus der Versionsverwaltung.
4. Behebe alle mypy- und Ruff-Fehler und arbeite anschließend die Flake8-Meldungen ab.
5. Ergänze für jeden Tag die genauen Lernquellen, eine Lernzusammenfassung und offene Fragen.
6. Bearbeite jede zukünftige Aufgabe in einem fokussierten Branch und Pull Request mit klaren Commit-Nachrichten.

Du machst gute Fortschritte und hast mehrere Punkte aus Feedback 1 sichtbar umgesetzt. Der nächste Entwicklungsschritt besteht darin, aus funktionierendem Code konsistent strukturierten, geprüften und reproduzierbaren Code zu machen.

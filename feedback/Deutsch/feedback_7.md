# Feedback 7 — 16. Oktober 2026

## Umfang des Reviews

Nachträgliches Mentor-Feedback vom 19. Oktober für Freitag, den 16. Oktober. Bewertet werden die Abschlussabgabe von Tag 10 und das erste Projekt zur Wartbarkeit aus Tag 11. Die Lerntage im PDF sind keinen festen Kalenderdaten zugeordnet.

## Übersicht der Abgaben

| Arbeit | Datierter Nachweis | Bewertung |
|---|---|---|
| Analyse und Ausgaben von Tag 10 | PRs [#17](https://github.com/NeilS1234/ErsterRepo/pull/17) und [#18](https://github.com/NeilS1234/ErsterRepo/pull/18), am 16. Oktober gemergt | Geforderte Artefakte vorhanden; Kennzahlen nachgerechnet; Methodik und Reproduzierbarkeit müssen verbessert werden |
| Projekt von Tag 11 | [PR #19](https://github.com/NeilS1234/ErsterRepo/pull/19), am 16. Oktober gemergt | Sinnvolle Strukturdemo; gefordertes Refactoring einer früheren Aufgabe nicht nachgewiesen |
| Projekt-README von Tag 11 | [58a15ab](https://github.com/NeilS1234/ErsterRepo/commit/58a15abde61323160560d204c3464cff9b7a8074), auf dem Lernbranch auf den 16. Oktober datiert; PR #20 am 19. Oktober gemergt | Dokumentation vorhanden, aber bis Freitag nicht in main integriert |

Die Abgabe von Tag 12 und die am 19. Oktober dokumentierten PRs #20–23 liegen außerhalb der Implementierungsbewertung für letzte Woche. Das Datum von PR #20 dient hier nur zur Einordnung der README-Integration.

## Tag 10 — Was du gut gemacht hast

- Du verbindest Weltbankdaten zu BIP pro Kopf und Lebenserwartung über Ländercode und Jahr.
- Das Skript speichert einen zusammengeführten Datensatz, ein Streudiagramm, einen Zeitverlauf, ein horizontales Balkendiagramm und einen Ergebnisbericht. Die umbenannten Ausgaben liegen unter `output_Day_10/`.
- Eine Abhängigkeitsdatei nennt pandas, Matplotlib und requests.
- Der gespeicherte Datensatz enthält **6.098 Zeilen** und keine doppelten Kombinationen aus Ländercode und Jahr.
- Alle fünf berichteten Kennzahlen stimmen nach gleicher Rundung mit der Nachrechnung aus diesem Datensatz überein: **0,62** Korrelation für 2023; **65,0** beziehungsweise **81,3** Jahre für das untere und obere BIP-Quartil; mediane Lebenserwartung **69,1** im Jahr 2000 und **73,8** im Jahr 2023; Monaco mit ungefähr **256.800 US-Dollar** BIP pro Kopf im Jahr 2023.
- Der Bericht nennt fehlende Daten, Grenzen des BIP und den Unterschied zwischen Korrelation und Kausalität.

## Tag 10 — Was du verbessern solltest

- Der Filter auf dreistellige Codes beschränkt die Daten nicht auf Länder. Die eingecheckte CSV enthält auch Aggregate wie **World, Arab World und European Union**. Schließe solche Einheiten anhand der Quellenmetadaten aus und erzeuge die Ländervergleiche neu. Bis dahin sind die Berechnungen reproduzierbar, ihre Beschreibung als reine Ländervergleiche aber ungenau.
- Erkläre, dass die Quartile über BIP pro Kopf gebildet werden, die Korrelation die ursprünglichen BIP-Werte verwendet, obwohl die Streudiagrammachse logarithmisch ist, und der jährliche Median die verfügbaren Einheiten ungewichtet berücksichtigt. Fehlende Beobachtungen können die Stichprobe zwischen den Jahren verändern.
- Das Programm schreibt weiterhin nach `output/`, während der eingecheckte Ordner `output_Day_10/` heißt. Lege einen dokumentierten Ausgabeort fest, damit ein erneuter Lauf keine konkurrierenden Ergebnisse erzeugt.
- Dokumentiere Arbeitsverzeichnis, Installation, Ausführungsbefehl, Indikator-IDs, Abrufdatum und eine Reproduktion aus gespeicherten Eingaben. Eine spätere Live-API-Antwort kann sich ändern.
- Ergänze Prüfungen von Antwortstruktur, Seitennavigation und eindeutigen Schlüsseln vor dem Merge, zähle nicht zugeordnete Zeilen und behandle Verbindungsfehler oder leere Daten verständlich.
- Verschiebe die Ausführung hinter einen `main()`-Einstiegspunkt, damit ein Import keine Netzwerkanfragen und Schreibvorgänge auslöst.

## Tag 11 — Was du gut gemacht hast

- `my_project_day_11/src/main.py` enthält ein Quellcode-Verzeichnis, typisierte Funktionen `add()` und `main()`, einen Docstring mit Args/Returns und einen geschützten Einstiegspunkt.
- Berechnung und Ausgabe sind getrennt. Die unveränderte Datei gibt bei der Ausführung in einer isolierten Kopie **5** aus.
- Die Branch-README beschreibt das Additionsbeispiel und nennt gelernte Inhalte.

## Tag 11 — Was noch erforderlich ist

Der Plan verlangt das Refactoring **einer früheren Aufgabe**, deren Verhalten in einem strukturierten Projekt erhalten bleibt. Ein neues Additionsbeispiel zeigt die Struktur, weist diese Anforderung aber nicht nach. Überarbeite die Transaktions-, CSV-Bereinigungs- oder pandas-Aufgabe zu kleinen typisierten Funktionen, dokumentiere sie und erhalte das ursprüngliche Verhalten.

Im main-Stand vom Freitag ist die Projekt-README leer; die dokumentierte Branch-Version wurde am 19. Oktober gemergt. Die Dokumentationsarbeit wird anerkannt. Ergänze aber die Projektstruktur und eine klare Angabe zum Arbeitsverzeichnis: `python src/main.py` muss innerhalb von `my_project_day_11/` ausgeführt werden; alternativ nenne den vollständigen Befehl relativ zum Repository.

## Git, Dokumentation und offene Punkte

- Eigene Branches und PRs gehören inzwischen zu deinem Ablauf. Für PRs #17 und #19 liegen keine abgegebenen Reviews vor; ein Merge allein weist keine unabhängige Prüfung nach.
- Verwende einen zusammenhängenden Aufgaben-PR mit aussagekräftigen Commit-Nachrichten und dem bereits verlangten Branch-Format des Unternehmens, zum Beispiel `feature/day11Refactor`.
- Python-Cache-Dateien werden weiterhin versioniert; im geprüften main-Baum fehlt eine zentrale `.gitignore`. Dieser Punkt aus Feedback 2 ist noch offen.
- Quellenlinks und übernommene Aufgabenbeschreibungen ersetzen keine eigene Lernzusammenfassung und Fragen. Die Branch-README von Tag 11 ist ein Anfang; ergänze Schwierigkeiten, Lösungsweg und offene Punkte.

## Erforderliche nächste Schritte

1. Repariere die noch nicht integrierte Anwendung von Tag 8 und reiche sie wie in Feedback 4 beschrieben ein.
2. Korrigiere die Grundgesamtheit und den Ausgabepfad von Tag 10 und erzeuge und erläutere die Ergebnisse erneut.
3. Überarbeite eine frühere Aufgabe für Tag 11 und vervollständige die Ausführungsdokumentation.
4. Entferne versionierte Caches, ergänze Ignore-Regeln und dokumentiere erfolgreiche Qualitätsprüfungen des überarbeiteten Projekts.
5. Ergänze tägliche Lernnotizen und hole vor dem Merge ein Review ein.

Du hast dich von einzelnen pandas-Übungen zu einer Analyse mit Daten, Diagrammen und schriftlichem Bericht weiterentwickelt. Jetzt stehen korrekte methodische Entscheidungen und eine wartbare Struktur für eine echte frühere Aufgabe im Vordergrund.

## Nachweise und Validierung

Geprüft wurden der [main-Stand vom Freitag](https://github.com/NeilS1234/ErsterRepo/tree/5e323eaf3a53f3a1585d7f6c3c2fdcd04636ddca), Tag-10-Skript, Abhängigkeiten, gespeicherte CSV und Erkenntnisse, Tag-11-Quellcode, datierte Branch-README und relevante PR-Metadaten. Alle fünf Erkenntnisse wurden aus der eingecheckten CSV nachgerechnet; das kleine Tag-11-Programm wurde ausgeführt. Die Diagrammdateien wurden als vorhanden bestätigt; ihre Darstellung und ein neuer Weltbankabruf wurden nicht validiert. Ruff, mypy, Flake8 und eine vollständige Testsuite wurden nicht ausgeführt; Prüfzahlen aus früherem Feedback werden nicht als aktuelle Ergebnisse dargestellt.

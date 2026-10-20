# Feedback 6 — 15. Oktober 2026

## Umfang des Reviews

Nachträgliches Mentor-Feedback vom 19. Oktober für Donnerstag, den 15. Oktober, zu den bis dahin verfügbaren Übungen zum Zusammenführen und Visualisieren von Daten aus Tag 10.

## Übersicht der Abgaben

**Status: Übungen abgegeben; die vollständige Aufgabe von Tag 10 ist für dieses Datum noch nicht nachgewiesen.**

[PR #16](https://github.com/NeilS1234/ErsterRepo/pull/16) hat am 15. Oktober fünf Übungsskripte integriert. Die abschließende Analyse, der zusammengeführte Datensatz, drei Diagrammdateien und die Erkenntnisse wurden mit [PR #17](https://github.com/NeilS1234/ErsterRepo/pull/17) vom 16. Oktober ergänzt. Dieser spätere Fortschritt gehört zum Freitagsfeedback.

## Was du gut gemacht hast

- Du zeigst `merge()` über einen ID-Schlüssel und `join()` über übereinstimmende Indizes.
- Du kombinierst Monatsdatensätze mit `concat(..., ignore_index=True)`.
- Die Balkendiagramm-Übung enthält einen Titel und Beschriftungen für beide Achsen.
- Eine separate Übung berechnet Mittelwert, Minimum und Maximum.
- Du hast die Arbeit über einen eigenen Branch und Pull Request eingereicht.

Das sind sinnvolle Einzeldemonstrationen der Lernthemen von Tag 10.

## Was noch erforderlich ist

Die PDF-Aufgabe verlangt zwei zusammengehörige Datensätze in einer gemeinsamen Analyse, einen zusammengeführten Datensatz, drei aussagekräftige Diagramme, fünf datenbasierte Erkenntnisse und eine kurze Erläuterung der Grenzen. Die fünf Übungsskripte liefern diese vollständige Abgabe noch nicht:

- Die Beispiele verwenden getrennte kleine Datensätze im Code statt einer gemeinsamen Analyse.
- Die Diagrammübung zeigt mit `plt.show()` ein Balkendiagramm; drei gespeicherte Diagramme fehlen.
- Drei ausgegebene Kennzahlen sind noch keine fünf interpretierten Erkenntnisse.
- Ein zusammenhängender Ergebnisbericht mit Grenzen und reproduzierbaren Ausführungsanweisungen ist in der datierten Abgabe nicht vorhanden.

Damit ist die Aufgabe zum Donnerstag-Stichtag unvollständig. Das bedeutet nicht, dass die Abschlussaufgabe heute im Repository fehlt.

## Was du verbessern solltest

- Wähle eine Frage, die sich durch das Verbinden zweier zusammengehöriger Datensätze beantworten lässt, und erkläre Schlüssel und Join-Typ.
- Prüfe eindeutige Schlüssel und Zeilenanzahlen vor und nach dem Merge und identifiziere nicht zugeordnete Zeilen.
- Wähle drei Diagramme für unterschiedliche Fragen. Speichere sie mit klaren Beschriftungen, Einheiten und relevanten Zeitangaben.
- Belege jede Erkenntnis durch eine Zahl oder konkrete Beobachtung und beschreibe wichtige Grenzen.
- Ergänze Abhängigkeiten, genauen Ausführungsbefehl, verwendete Quellen, Lernzusammenfassung und Fragen oder Hindernisse. Der Abschnitt zu Tag 10 in der zentralen README wurde am 16. Oktober committet und wird deshalb nicht dem Donnerstag zugerechnet.
- Entferne das Leerzeichen vor der Dateiendung in `Writing_Data_Driven_Conclusions .py` und verwende konsistente, aussagekräftige Dateinamen.

## Erforderliche nächste Schritte

1. Verbinde die Übungen zu einer vollständigen, reproduzierbaren Analyse.
2. Reiche Datensatz, drei gespeicherte Diagramme, fünf Erkenntnisse und Grenzen gemeinsam ein.
3. Erkläre die Merge-Prüfungen und ergänze die täglichen Lernnotizen.
4. Verwende für die vollständige Aufgabe einen fokussierten PR und fordere ein Review an.

Die Bausteine hast du gezeigt. Jetzt sollen sie eine zusammenhängende Analyse ergeben, deren Schlussfolgerungen sich auf die kombinierten Daten zurückführen lassen.

## Nachweise und Validierung

Geprüft wurden der [main-Stand vom 15. Oktober](https://github.com/NeilS1234/ErsterRepo/tree/dba58439ba644da20868d87bbd73df07d9099f91/day_10_Combining_and_Visualizing_Data), die fünf Skripte, PR #16 und die Zeitangaben des nachfolgenden PR #17. Die Bewertung beruht auf Quellcode- und Historienprüfung. Die GUI-Diagrammübung und die Analyse mit Live-API wurden nicht ausgeführt; bestandene automatisierte Qualitätsprüfungen werden nicht behauptet.

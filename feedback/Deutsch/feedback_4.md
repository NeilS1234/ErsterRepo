# Feedback 4 — 13. Oktober 2026

## Umfang des Reviews

Nachträgliches Mentor-Feedback vom 19. Oktober für Dienstag, den 13. Oktober. Der Lernplan enthält keine Kalenderdaten; die an diesem Datum dokumentierte Arbeit betrifft Tag 8 — Datenbereinigung.

## Übersicht der Abgaben

**Status: Umfangreiche Umsetzung auf einem Branch abgegeben; mit der zuletzt eingecheckten Eingabe nicht reproduzierbar und nicht in main integriert.**

Der Branch `data-cleaning` enthält drei Commits vom 13. Oktober: [44ae294](https://github.com/NeilS1234/ErsterRepo/commit/44ae294efc807789667a08b0fcdc466fee5d80d7), [0490e50](https://github.com/NeilS1234/ErsterRepo/commit/0490e5078142488832923f59870a1b2daccc3da8) und [5b8e244](https://github.com/NeilS1234/ErsterRepo/commit/5b8e2446a766096d3f1755dbd36df4606792e8ad). Die Aufgabe liegt unter `Aufgabe_Tag_8/`. Der frühere PR #10 hat am 8. Oktober die Übung gemergt, enthält aber diese späteren Aufgaben-Commits nicht. In der geprüften PR-Liste gibt es keinen anschließenden PR für diese Commits.

## Was du gut gemacht hast

- Du hast das Bereinigungsskript, die ursprüngliche Eingabe, das bereinigte Ergebnis und einen separaten Bereinigungsbericht ergänzt.
- Die Dateipfade verwenden `Path(__file__).parent`. Damit ist diese Anwendung portabler als das Übungsskript.
- Der Code entfernt ein exaktes Duplikat, vereinheitlicht Texte, konvertiert Zahlen und Datumswerte, kennzeichnet ein negatives Gehalt als fehlend und benennt Spalten um.
- Der Bericht enthält Korrekturen, Begründungen und Anzahlen. Das eingecheckte Ergebnis umfasst nach Entfernung eines Duplikats zehn statt ursprünglich elf Datensätze.
- Ungültige Datumswerte werden als fehlend behandelt, statt ein Ersatzdatum zu erraten.

## Was du verbessern solltest

1. **Repariere zuerst die eingecheckte Eingabe.** Der letzte Commit ergänzt den PowerShell-Rahmen `@'` und einen abschließenden `Set-Content`-Befehl innerhalb von `messy_dataset.csv`. Das sind Shell-Anweisungen und keine CSV-Inhalte. Eine lokale Ausführung mit exakt den eingecheckten Dateien scheitert mit `KeyError: 'alter'`. Committe nur die CSV-Kopfzeile und die Datensätze und erzeuge anschließend beide Ausgaben neu. Die vorhandenen Ausgaben belegen nicht, dass die letzte Eingabe funktioniert.
2. Das Alter 150 bleibt im bereinigten Ergebnis erhalten. Definiere einen begründeten Gültigkeitsbereich und dokumentiere, ob solche Werte markiert, entfernt oder als fehlend behandelt werden.
3. Das Ersetzen eines unbekannten Alters durch 21 erfindet einen Wert. Begründe diese Regel für die Übung oder erhalte den fehlenden Wert mit einem passenden nullable Datentyp. Ein beliebiger Standardwert ist keine bestätigte Tatsache.
4. Davids ursprünglich fehlendes Gehalt bleibt leer, hat aber keinen eigenen Berichtseintrag. Unterscheide ursprünglich fehlende Werte von Werten, die durch die Validierung fehlen, und dokumentiere ihre Behandlung.
5. Der Eintrag zur Spaltenumbenennung nennt zwei unter „Affected Records“, zählt aber Spalten. Korrigiere die Einheit. Ergänze Prüfungen von Zeilenanzahl, Duplikaten, Datentypen sowie verbleibenden ungültigen und fehlenden Werten.
6. Erzeuge bei fehlender Eingabe nicht stillschweigend Ersatzdaten. Trenne die Erstellung von Beispieldaten von der Verarbeitung, damit ein falscher Eingabepfad sichtbar wird.
7. Ergänze aufgabenspezifische Installations- und Ausführungsanweisungen, Lernzusammenfassung, verwendete Quellen und Fragen oder Hindernisse. Der Abschnitt zu Tag 8 mit Themen und Quellen auf main wurde erst am 14. Oktober ergänzt und belegt deshalb keine Dokumentation am Dienstag.

## Feedback zu Git und GitHub

Der eigene Branch ist sinnvoll. Für die vollständige Aufgabe fehlt aber noch ein eigener PR. Ein bereits gemergter PR übernimmt spätere Branch-Commits nicht automatisch. Beschreibe die Eingabekorrektur in einer aussagekräftigen Commit-Nachricht und fordere vor dem Merge ein Review an.

## Erforderliche nächste Schritte

1. Entferne den PowerShell-Rahmen aus der CSV und führe die eingecheckte Anwendung erneut aus.
2. Kläre und dokumentiere die offenen Alters- und Gehaltsprobleme und erzeuge Ergebnis und Bericht gemeinsam neu.
3. Ergänze Prüfungen nach der Bereinigung und die täglichen Lernnotizen.
4. Öffne einen PR mit der vollständigen Aufgabe von Tag 8.

Gegenüber der Übung ist das ein klarer Fortschritt: Anwendung und Prüfbericht sind vorhanden. Jetzt muss sichergestellt werden, dass die eingecheckten Eingaben die abgegebenen Ergebnisse tatsächlich reproduzieren.

## Nachweise und Validierung

Geprüft wurden der [letzte datierte Branch-Stand](https://github.com/NeilS1234/ErsterRepo/tree/5b8e2446a766096d3f1755dbd36df4606792e8ad/Aufgabe_Tag_8), Skript, beide CSV-Datensätze, Bericht, Commit-Diffs und PR-Historie. Skript und Eingabe von Tag 8 wurden unverändert in einer isolierten Kopie ausgeführt und scheiterten wie beschrieben. Die eingecheckten Ausgaben wurden separat geprüft. Bestandene Ruff-, mypy-, Flake8- oder vollständige Testläufe werden nicht behauptet.

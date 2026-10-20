# Feedback 8 — 19. Oktober 2026

## Umfang der Bewertung

Am 20. Oktober anhand des vierwöchigen Lernplans geprüft. Dieser Eintrag behandelt Tag 12 und die Integration der README von Tag 11. Tag 12 war beim vorherigen Review bereits vorhanden und wurde in Feedback 7 ausdrücklich ausgeklammert; diese Arbeit wurde nicht erst nach diesem Review gepusht.

## Eingereichte Arbeit

- [PR #20](https://github.com/NeilS1234/ErsterRepo/pull/20) integrierte die README des Tag-11-Projekts am 19. Oktober.
- [PR #22](https://github.com/NeilS1234/ErsterRepo/pull/22) integrierte den Rechner und die Tests für Tag 12 am 19. Oktober. PR #23 synchronisierte main zurück in den Test-Branch.
- Geprüft wurden `day12-testing-debugging/src/calculator.py`, `tests/test_calculator.py` und `pyproject.toml` innerhalb dieses Projekts.

**Status:** Sinnvolle Testübung; die Aufgabe ist teilweise erfüllt. Der Plan verlangt Tests für die refaktorierte frühere Aufgabe und erfolgreiche Ergebnisse von pytest, mypy, Ruff und Flake8.

## Was dir gut gelungen ist

- Sieben automatisierte Tests decken Addition, Mittelwerte, negative Zahlen, null, einen Einzelwert und eine leere Liste ab.
- Der Test für die leere Liste prüft den Ausnahmetyp und die Fehlermeldung.
- Die Funktionen besitzen Type Hints und Google-Style-Docstrings.
- Du hast pytest, striktes mypy und Ruff konfiguriert und Lernressourcen für Tag 12 in der Haupt-README ergänzt.
- Die README von Tag 11 ist jetzt in main integriert. Damit ist die in Feedback 7 beschriebene Integrationslücke geschlossen.

## Reproduzierte Qualitätsprüfungen

Die Prüfungen liefen am 20. Oktober in einer isolierten Kopie der drei unveränderten Textdateien aus dem Tag-12-Projektverzeichnis. Verfügbar war Python 3.14 statt des konfigurierten Python 3.11; damit ist keine Validierung unter Python 3.11 nachgewiesen.

| Prüfung | Ergebnis |
|---|---|
| `python -m pytest -q` | 7 Tests bestanden |
| `pytest -q` | Test-Erfassung scheitert: `ModuleNotFoundError: No module named 'src'` |
| `mypy src tests` | Fehler: calculator wird als `calculator` und `src.calculator` gefunden |
| `ruff check src tests` | Fehler I001 bei der Importformatierung der Testdatei |
| `ruff format --check src tests` | Beide Dateien müssen formatiert werden |
| `flake8 src tests` | Fehler W291, E302, E265 und W391 |

Bezeichne die Qualitätsprüfungen erst dann als erfolgreich, wenn sie aus einer dokumentierten, sauberen Umgebung bestehen.

## Was du verbessern solltest

1. Verbinde die Tests mit der für Tag 11 refaktorierten früheren Aufgabe. Ein separater Rechner zeigt Testtechniken, belegt aber nicht den Erhalt des ursprünglichen Verhaltens.
2. Vereinheitliche Paketstruktur und Imports, damit pytest und mypy dasselbe Modul erkennen. Dokumentiere Arbeitsverzeichnis und genaue Befehle.
3. Korrigiere Importformatierung, nachgestellte Leerzeichen, Leerzeilen und Kommentarabstände. Führe alle vier geforderten Werkzeuge erneut aus und halte die Ergebnisse fest.
4. Dokumentiere Python- und Abhängigkeitsversionen, Installation, deine tatsächlichen Lernerkenntnisse und offene Fragen.
5. Entferne in einer späteren Bereinigung versionierte Python-Caches und ergänze passende Ignore-Regeln. Cache-Dateien sind kein Nachweis bestandener Tests.
6. Verwende aussagekräftige Commit- und PR-Titel sowie die bereits gewünschte Branch-Konvention, beispielsweise `feature/day12Tests`.

## Nächste Abgabe

Reiche die getestete, refaktorierte Aufgabe mit reproduzierbarer Einrichtung und erfolgreichen Ausgaben von pytest, mypy, Ruff und Flake8 ein. Behalte die sieben funktionierenden Tests bei und verbessere Projektintegration und Stil.

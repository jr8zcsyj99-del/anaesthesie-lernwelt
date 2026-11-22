# anaesthesie-lernwelt

## Lernbibliothek 1.0

22 ursprüngliche Themen mit je einer kompakten strukturierten Fortbildung, sechs Lernkarten und einem neuen PNG-Pocketguide (1080 × 1920). Die vorhandenen Originaldateien liegen unverändert unter `originale/`; ihre SHA-256-Prüfsummen stehen in `data/originals-sha256.json`. Alte Bildguides sind Archivmaterial, keine geprüften Dosierungsanleitungen.

Inhalte: `data/build_content.py`. Build: `python3 data/build_site.py` (Python 3, Pillow und DejaVu Sans). Der Build erzeugt `data/topics.json`, bindet die Inhalte in `index.html` ein und rendert alle 22 Pocketguides mit Überlaufkontrollen. `app.js` und `styles.css` sind direkt statisch nutzbar. Keine kostenpflichtige API und kein Backend.

Online-Abgleich der verlinkten medizinischen Quellen: 22.11.2026. Volltextzugriff und Evidenzgrenzen sind in den Themen benannt, soweit relevant. Fiktive Praxisfälle dienen dem Lernen. Keine klinisch freigegebene SOP; keine erfundenen Lehrbuchseiten oder Zitate.

Prüfung: 22 eindeutige Themen, 154 Abschnitte, 132 Karten, 22 PNGs mit exaktem 9:16-Verhältnis; sämtliche internen Dateiverweise und Originalprüfsummen kontrolliert. Browser-Stichproben: Suche, Kategorien, Favoriten, Kartenwechsel, Formate, HTML-Export und Offline-Speicher erfolgreich. Ein langer Browserdurchlauf wurde am Zeitlimit unterbrochen. Kein Test auf einem physischen iPhone und kein Flugmodustest.

Veröffentlichung im bestehenden GitHub-Pages-Repository. Seitenadresse, Manifest und iPhone-Icons bleiben unverändert.
Digitale Lernbibliothek für die Fachweiterbildung Anästhesiepflege

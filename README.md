<<<<<<< HEAD
# ProtoPoC
=======

# ProtoPoC – Bauteil-Datenbank-Prototyp

**ProtoPoC** (Prototype Proof of Concept) ist ein Python-basiertes Tool zum Importieren, Strukturieren und Analysieren von technischen Bauteillisten aus Excel-Dateien (.xlsm). Es nutzt eine SQLite-Datenbank, um Bauteilarten zentral zu speichern und projektbezogene Verwendungen zu verknüpfen.

---

## 🔧 Funktionen des aktuellen Prototyps (Meilenstein 1)

- Import aus `.xlsm`-Dateien (z. B. `Moria1000.xlsm`)
- Trennung von:
  - **Statischen Bauteildaten** → `Bauteile_Master`
  - **Projektdaten je Bauteil** → `Projekt_Bauteile`
- Automatische Vergabe von `call_id`s pro Bauteilart
- Zentrale Definition von Systemregeln (`system_rules.json`)
- Dokumentation und Visualisierung (`docs/`)

---

## 🧪 Setup & Ausführung

### Voraussetzungen
- Python 3.8+
- Installierte Pakete:
  ```bash
  pip install pandas openpyxl
  ```

### Ausführen des Imports:
```bash
python src/import_arma.py
```

Das Script:
1. Liest die `.xlsm`-Datei im `data/`-Ordner
2. Schreibt alle Daten in die Datenbank `db/moria.db`
3. Erstellt Tabellen:
   - `Arma_Import`
   - `Bauteile_Master`
   - `Projekt_Bauteile`

---

## 📁 Projektstruktur

```
ProtoPoC/
├── data/                # Originaldaten (Excel, CSV)
├── db/                  # SQLite-Datenbank
├── docs/                # Visualisierungen, Diagramme
├── rules/               # Regeln als JSON & Text
├── src/                 # Python-Code (Import etc.)
└── README.md            # Diese Datei
```

---

## 🧠 Nächste Schritte (geplant)
- Benutzerrollen & Bearbeitungssperren
- Revisionsverwaltung
- Vergleich über mehrere Projekte
- Visuelle Oberfläche (z. B. mit Streamlit)

---

## 🧑‍💻 Autor & Betreuung
Dieses Projekt wurde Schritt für Schritt mit Unterstützung durch KI gebaut und dient als Lern- und Praxisprojekt.
>>>>>>> 0a41516 (Initial upload)

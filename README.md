# ProtoPoC

**ProtoPoC** ist ein modulares System zur Verwaltung, Bearbeitung und Visualisierung von Projektdaten – insbesondere Armaturenlisten – mit einer sauberen Trennung von Backend (FastAPI), Frontend (React + AgGrid) und Datenimport (Python-Skripte). Es eignet sich besonders für Teams, die mehrere technische Projekte gleichzeitig verwalten und dabei eine revisionssichere, datenbankgestützte Lösung suchen.

---

## 📁 Projektstruktur

```bash
ProtoPoC/
├── backend/             # FastAPI REST-API
│   ├── main.py          # Startpunkt der API
│   ├── api.py           # Definition aller HTTP-Endpunkte
│   └── db.py            # Zugriff auf SQLite, alle SELECT/UPDATE-Operationen
│
├── frontend/            # React App mit AgGrid-UI
│   ├── src/
│   │   ├── App.js               # Root-Komponente mit Buttons zum Ansichtswechsel
│   │   ├── AgGridTable.jsx     # Projektliste mit Bearbeitung & Speichern
│   │   ├── MasterTable.jsx     # Mastertabelle mit Dropdown & Save-Button
│   │   ├── AgGridColors.css    # Styling für farbige Header
│   │   └── index.js            # Einstiegspunkt für React
│   └── public/index.html       # HTML-Hülle für React
│
├── import/              # Datenmigration und -verarbeitung
│   ├── hash_import_lotr.py          # Importiert mehrere Excel-Sheets in SQLite mit Hash-Duplikat-Prüfung
│   ├── generate_master_project_call_ID.py  # Erstellt Master-/Projekttrennung mit automatischen Call-IDs
│
├── db/                  # SQLite-Datenbank
│   └── LordOfRings.db
│
├── data/                # Rohdaten aus Excel
│   └── *.xlsm
│
├── README.md
└── requirements.txt     # Python-Abhängigkeiten
```

---

## 🚀 Funktionen

- 🧠 Import von `.xlsm`-Dateien mit Hashprüfung (keine Duplikate)
- 📋 Projektansicht (Bearbeitung von `Bauteil`, `Revision`, `Beschreibung`)
- 🧱 Masteransicht mit Dropdown (`Magische-Relevanz`) & Schreibschutz (`Revision`)
- 💾 Speicherung von Änderungen über FastAPI direkt in `LordOfRings.db`
- 🖱 Tabs für einfache Navigation zwischen Projektlisten & Mastertabelle
- 🔌 Vollständig getrennte Logik: Backend ↔ Frontend via HTTP

---

## 🧪 Lokaler Start

### 🔧 Backend starten (FastAPI)
```bash
cd backend
uvicorn backend.main:app --reload
```
- Läuft auf: `http://localhost:8000`
- Doku: `http://localhost:8000/docs`

### ⚛ Frontend starten (React)
```bash
cd frontend
npm install
npm start
```
- Läuft auf: `http://localhost:3000`

---

## 📄 Erklärung der Hauptdateien (für Einsteiger)

### `backend/main.py`
- Startet FastAPI-Anwendung
- Aktiviert CORS (damit das Frontend kommunizieren darf)
- Bindet die API-Routen aus `api.py` ein

### `backend/api.py`
- Definiert die API-Endpunkte:
  - `/projects` → Liste verfügbarer Projekte
  - `/project/{id}` → Projektdaten abrufen
  - `/update_row` → Projektzeile aktualisieren
  - `/master` → Mastertabelle laden
  - `/update_master_row` → Masterzeile speichern

### `backend/db.py`
- `get_all_projects()` → gibt Projekt-IDs zurück
- `get_project_data(projekt_id)` → macht JOIN zwischen Projekt + Master
- `update_project_row(row)` → speichert Änderungen in `Projekt_Bauteile`
- `get_all_master_data()` → lädt `Bauteile_Master`
- `update_master_row_data(row)` → speichert Änderungen in `Bauteile_Master`

### `frontend/src/App.js`
- Zeigt die Navigation (Buttons für Projekt- & Masteransicht)
- Bindet `AgGridTable` und `MasterTable` ein

### `frontend/src/AgGridTable.jsx`
- Zeigt Projektdaten
- Felder editierbar (außer `call_id`, `Ort`)
- Speichert Änderungen via `axios.post`

### `frontend/src/MasterTable.jsx`
- Zeigt statische Masterdaten
- `Magische-Relevanz` ist Dropdown (`"", "M", "MS"`)
- `Revision` ist geschützt
- Speichert Änderungen mit `axios.post`

### `import/hash_import_lotr.py`
- Importiert `.xlsm`-Dateien
- Entfernt leere Spalten & Filterzeile
- Verhindert doppelte Zeilen durch Hashbildung

### `import/generate_master_project_call_ID.py`
- Trennt Bauteile in Master & Projektansicht
- Erstellt `call_id` aus Herstellername + Nummerierung (z. B. `NOL001`)

---

## 📦 Geplant

- 🧾 Revisionsverfolgung pro Änderung
- 👥 Rollen (Admin, Viewer, Entwickler)
- 📤 Export als Excel/PDF
- 🔐 Login-System für Projektmitglieder

---

## ✨ Autor

[Pablo Ferreres](https://github.com/PabloFerreres)

---
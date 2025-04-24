# ProtoPoC

**ProtoPoC** ist ein modulares System zur Verwaltung, Bearbeitung und Visualisierung von Projektdaten – insbesondere Armaturenlisten – auf Basis von SQLite, React, FastAPI und Excel-Importen.

---

## 📁 Projektstruktur

```bash
ProtoPoC/
├── backend/             # FastAPI REST-API für Projekte & Masterdaten
├── frontend/            # React + AgGrid – Excel-artige Web-UI
├── import/              # Python-Skripte für Migration/Import
├── db/                  # SQLite-Datenbank (LordOfRings.db)
├── data/                # Original Excel-Dateien (.xlsm)
├── README.md
└── requirements.txt     # Python-Abhängigkeiten
```

---

## 🚀 Funktionen

- Excel-Import von `.xlsm`-Dateien mit Aufteilung in Projekt- und Mastertabellen
- Projektansicht mit editierbaren Feldern (z. B. `Bauteil`, `Beschreibung`, `Revision`)
- Masteransicht mit Dropdown-Auswahl für `Magische-Relevanz` und Schreibschutz für `Revision`
- Speichern direkt in SQLite-Datenbank (`Projekt_Bauteile` & `Bauteile_Master`)
- Web-Frontend mit AgGrid (Excel-Stil), React + Axios
- Tabs zur Navigation zwischen Projektlisten und Masterdaten

---

## 🧑‍💻 Lokale Entwicklung

### 📦 Backend starten (FastAPI)
```bash
cd backend
uvicorn backend.main:app --reload
```

### ⚛ Frontend starten (React)
```bash
cd frontend
npm install
npm start
```

---

## 🔄 Nächste Schritte (geplant)

- Revisionsverfolgung automatisiert (statt manuell)
- Benutzerrollen (Admin, Viewer, Entwickler)
- Export als Excel oder PDF
- Historie & Änderungsverlauf pro Bauteil

---

## ✨ Autor

[Pablo Ferreres](https://github.com/PabloFerreres)

---
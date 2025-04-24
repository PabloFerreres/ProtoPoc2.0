
# ProtoPoC

**ProtoPoC** ist eine modulare Plattform zur Verwaltung, Bearbeitung und Visualisierung von Projektkomponenten (z. B. Armaturenlisten) mit vollständiger Trennung zwischen Datenimport, API und Benutzeroberfläche.

---

## 📁 Projektstruktur

```bash
ProtoPoC/
├── backend/             # FastAPI – REST API für Projekte & Bauteile
├── frontend/            # React + AgGrid – UI im Excel-Stil
├── data/                # Excel-Dateien (.xlsm)
├── db/                  # SQLite-Datenbank
│   └── LordOfRings.db
├── requirements.txt     # Python-Abhängigkeiten für Backend
└── README.md
```

---

## 🚀 Funktionen

- Automatischer Import von Excel-Daten in SQLite
- Trennung von Master- und Projekt-Bauteilen
- API-Schnittstelle für externe Zugriffe (z. B. React-UI)
- Web-UI im Excel-Stil mit AgGrid (Bearbeitung möglich)
- Projektübergreifende Analyse und Revisionsplanung möglich

---

## 🧑‍💻 Lokale Entwicklung

### 1. Backend starten (FastAPI)

```bash
cd backend
uvicorn main:app --reload
```

Erreichbar unter: [http://localhost:8000](http://localhost:8000)  
Dokumentation: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### 2. Frontend starten (React)

```bash
cd frontend
npm install
npm start
```

Öffnet die Web-App unter [http://localhost:3000](http://localhost:3000)

---

## 📦 Noch geplant

- Benutzerrollen & Login
- Revisionsverfolgung mit History
- Vergleich mehrerer Projektstände
- Automatisierter Import mit Validierung

---

## ✨ Autor

[Pablo Ferreres](https://github.com/PabloFerreres)

---


ProtoPoC 2.0

BESCHREIBUNG
------------
ProtoPoC 2.0 ist ein vollständiger Prototyp einer Webapplikation, die eine Datenbanktabelle in einem Browser visuell und dynamisch anzeigt.

Ziel:
- Einfaches Bearbeiten und Anpassen der Tabellenansicht
- Layout-Änderungen speichern (Spalten verschieben/breiten)
- Beim Neuladen automatisch gespeichertes Layout anwenden

Technologien:
- Backend: FastAPI + SQLite
- Frontend: React + ag-Grid

---------------------------------------

PROJEKTSTRUKTUR
---------------
ProtoPoC2.0/
├── backend/
│   ├── main.py         (FastAPI Serverstart)
│   ├── api.py          (API-Endpunkte)
│   └── db.py           (SQLite Zugriff)
├── db/
│   └── SimpleTest.db   (Testdatenbank)
├── frontend/
│   └── src/
│       ├── App.js
│       ├── AgGridTable.jsx
│       └── components/
│           ├── BaseTable.jsx
│           ├── BaseViewTable.jsx
│           └── AgGridColors.css

---------------------------------------

KURZ ERKLÄRT
------------
- React lädt Daten aus FastAPI-Backend
- ag-Grid zeigt die Daten als dynamische Tabelle
- Layout-Änderungen werden gespeichert
- Farben im Header alle 5 Spalten unterschiedlich

---------------------------------------

SCHNELLSTART
------------
Backend starten:
> cd backend
> uvicorn main:app --reload

Frontend starten:
> cd frontend
> npm install
> npm start

---------------------------------------

Viel Erfolg beim Arbeiten mit ProtoPoC 2.0!

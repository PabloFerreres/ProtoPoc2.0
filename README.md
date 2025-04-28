
# ProtoPoC 2.0

## 📕 Beschreibung

ProtoPoC 2.0 ist ein vollständiger Prototyp einer Webapplikation, die eine Datenbanktabelle in einem Browser visuell und dynamisch anzeigt.

Das Ziel:

- Einfaches Bearbeiten und Anpassen der Tabellenansicht
- Layout änderungen (Spalten verschieben, Spaltenbreiten ändern) speichern
- Beim Neuladen automatisch das gespeicherte Layout anwenden

Dieses Projekt eignet sich besonders gut für Anfänger, die **FastAPI** (Backend) und **React + ag-Grid** (Frontend) verstehen möchten.

---

## 📊 Projektstruktur

```
ProtoPoC2.0/
├── backend/
│   ├── main.py         # FastAPI Serverstart
│   ├── api.py          # API-Endpunkte (Daten holen/speichern)
│   └── db.py           # Datenbankzugriffe (SQLite)
├── db/
│   └── SimpleTest.db   # SQLite Testdatenbank
├── frontend/
│   └── src/
│       ├── App.js              # Einstiegspunkt der React-App
│       ├── AgGridTable.jsx     # Tabelle + API-Anbindung
│       └── components/
│           ├── BaseTable.jsx       # Wrapper-Komponente für Tabellenlayout
│           ├── BaseViewTable.jsx   # Ag-Grid Tabelle mit Farben und Layout-Logik
│           └── AgGridColors.css    # Header-Farbgebung für jede 5 Spalten
```

---

## 🌌 Technologien

### Backend: FastAPI 🔢

- **FastAPI**: Ein leichtgewichtiges, schnelles Framework für Web-APIs.
- **SQLite**: Eine kleine lokale Datenbank.
- Funktionen:
  - `/project/TestBauteile` holt alle Daten aus der Tabelle.
  - `/save_layout` speichert Spaltenanpassungen.
  - `/layout/TestBauteile` lädt gespeicherte Layout-Daten.

### Frontend: React + ag-Grid 📈

- **React**: JavaScript-Framework für UI-Entwicklung.
- **ag-Grid**: Profi-Datentabelle mit Features wie:
  - Spalten anpassen, sortieren, filtern
  - Sehr performant für viele Daten

**Interaktion:**

- `AgGridTable.jsx` kommuniziert per **Axios** mit dem Backend.
- Tabelle wird in `BaseViewTable.jsx` gerendert (ag-Grid-Komponente).
- Farblogik: Jede 5 Spalten erhalten dieselbe Headerfarbe zur besseren Übersicht (gesteuert über `AgGridColors.css`).

---

## 🚀 Schnellstart

### 1. Backend starten (FastAPI)

```bash
cd backend
uvicorn main:app --reload
```
Server läuft auf: [http://localhost:8000](http://localhost:8000)

### 2. Frontend starten (React)

```bash
cd frontend
npm install
npm start
```
Frontend läuft auf: [http://localhost:3000](http://localhost:3000)

### 3. GitHub Synchronisation (Projekt hochladen)

- Lokales Projekt initialisieren (falls noch nicht geschehen):

```bash
git init
git remote add origin https://github.com/DEIN_USERNAME/ProtoPoC2.0.git
```

- Alle Änderungen hinzufügen und hochladen:

```bash
git add .
git commit -m "Erster Commit für ProtoPoC2.0"
git push -u origin main
```

---

## 📅 Funktionsweise (für Anfänger erklärt)

- Beim Öffnen der Seite ruft das Frontend alle Datensätze aus der Datenbank ab (API `/project/TestBauteile`).
- Wenn der Nutzer Spalten verschiebt oder die Größe ändert, werden diese Änderungen automatisch gespeichert (API `/save_layout`).
- Beim nächsten Laden ruft das Frontend das gespeicherte Layout ab (API `/layout/TestBauteile`) und wendet es auf die Tabelle an.

Alles passiert automatisch im Hintergrund — der Benutzer merkt davon nichts!

---

## 🌈 Header Farbanpassungen
### Wie wird die Farben für Header in ag-Grid angewendet?
- Die Farben für jede 5. Spalte im **ag-Grid** werden durch **CSS-Klassen** (`header-group-1`, `header-group-2`, ...) gesetzt, wobei jede Gruppe eine unterschiedliche Farbe hat.
- Beispiel: Erste 5 Spalten erhalten eine Farbe, die nächsten 5 eine andere usw.
- **CSS**: Farbgebung wird durch **`AgGridColors.css`** definiert.


## 🎉 Highlights

- 🌟 Layout bleibt erhalten, auch nach Refresh
- 🛢️ Farben für bessere Spaltenübersicht
- 🛠️ Vollständig modularer Aufbau (Backend/Frontend getrennt)
- 📊 Ideal für Einsteiger

---

## 📅 TODO (optional für Zukunft)

- Zellen direkt im Grid editierbar machen
- Undo/Redo bei Layout-Änderungen
- Responsive Optimierungen

---

## 🙌 Viel Spaß beim Testen und Verstehen von ProtoPoC 2.0!

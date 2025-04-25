# ProtoPoC – Projektverwaltungssystem

## 📦 Projektüberblick

Ein modulares System zur Verwaltung von Projekttabellen (Armaturenlisten) mit:
- 💠 Zentraler Mastertabelle
- 📋 Projektspezifischen Bauteil-Ansichten
- 🔁 Geplanter Revisionslogik
- ✅ AgGrid-Frontend mit FastAPI-Backend
- 📂 SQLite Datenbank (LordOfRings.db)

---

## 📁 Verzeichnisstruktur

```
ProtoPoC/
│
├── backend/             # FastAPI Backend (startbar aus Hauptverzeichnis!)
│   └── main.py
│
├── db/
│   └── LordOfRings.db   # SQLite-Datenbank mit Projekttabellen
│
├── frontend/
│   ├── src/
│   │   ├── AgGridTable.jsx      # Projektansicht mit Projektauswahl
│   │   ├── MasterTable.jsx      # Masteransicht
│   │   └── components/
│   │       └── BaseTable.jsx    # Gemeinsame Tabellenkomponente
│   └── package.json
│
└── README.md
```

---

## 🚀 Startanweisungen

### 📡 Backend (FastAPI)

```bash
cd ProtoPoC
uvicorn backend.main:app --reload
```

> ⚠️ Achtung: **Nicht aus `backend/` heraus starten!**

### 🎛 Frontend (React)

```bash
cd frontend
npm install     # Nur beim ersten Mal nötig
npm start
```

---

## 🔄 GitHub Synchronisation

### 💾 Lokale Änderungen committen

```bash
git add .
git commit -m "Kurze Nachricht zum Update"
```

### ⬆️ Änderungen hochladen

```bash
git push
```

Falls Konflikte auftreten:
- `.gitignore` → `node_modules/`, `.cache/` etc.
- ggf. Git LFS verwenden: [https://git-lfs.github.com](https://git-lfs.github.com)

---

## ✅ Aktuelle Features

- ✅ Projektauswahl per Dropdown
- ✅ Zoomfunktion mit %-Anzeige
- ✅ AutoFit + Zeilenhöhe
- ✅ Farbige Header nach Excel-Vorbild
- ✅ Schutz statischer Spalten (readonly)
- ✅ Zentrale BaseTable-Komponente

---

## 📌 Nächste Schritte

- 🔁 Revisionslogik (Versionierung)
- ➕ Neue Bauteile einfügen
- 📤 Export (Excel/PDF)
- 🔐 Login & Rollensteuerung

---

Projektstand: **Lauffähiger Prototyp mit klarer Struktur – bereit zur Erweiterung.**
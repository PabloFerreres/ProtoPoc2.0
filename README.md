# ProtoPoC - Custom Excel-Style Table

## 📕 Projektbeschreibung

Dieses Projekt zeigt eine moderne Webanwendung zur Visualisierung von Tabellendaten mit **ag-Grid** und **React**,  
erweitert um **eigene Filterfunktionen**, **Filterstatus-Anzeige** und **Filter-Reset**.

---

## 🌟 Features

- **Custom Excel-Style Filter**:
  - Eigene Checkboxen für jede Spalte.
  - Auswahl einzelner Werte oder "Alle auswählen/abwählen".
  - Sofortige Filteraktualisierung ohne Verzögerung.

- **Filter-Status-Anzeige**:
  - Grün: Kein Filter aktiv ✅
  - Rot: Mindestens ein Filter aktiv ⚠️
  - Dynamische Aktualisierung basierend auf Benutzeraktionen.

- **Filter-Reset-Button**:
  - Ein Klick löscht alle gesetzten Filter.
  - Tabelle zeigt wieder alle ursprünglichen Daten.

- **Modulares System**:
  - `BaseViewTable.jsx` für Layout und Steuerung.
  - `CustomSetFilter.jsx` für individuelles Filtern.
  - `FilterStatus.jsx` für Status- und Reset-Steuerung.
  
- **Weitere Features**:
  - Farben und Hover-Effekte im Header.
  - AutoSize-Button für automatische Spaltenbreitenanpassung.
  - Zoom-Funktion (Skalierung der Tabelle).

---

## 🛠 Technologien

- **Frontend**: React, ag-Grid Community Edition
- **Styles**: CSS (ag-Grid Alpine Theme + eigene Anpassungen)
- **Struktur**: Vollständig modulare Komponentenstruktur

---

## 📂 Projektstruktur

```
/src
├── components
│   ├── BaseViewTable.jsx      # Haupt-Komponente für Tabellenlayout und Steuerung
│   ├── CustomSetFilter.jsx     # Eigener Checkbox-Filter
│   ├── FilterStatus.jsx        # Filterstatus-Anzeige mit Reset-Button
│   └── AgGridColors.css        # Farbgestaltung für Header-Zellen
├── App.js                      # Einstiegspunkt der React-App
├── index.js                    # ReactDOM Renderpunkt
```

---

## 🚀 Schnellstart

1. **Projekt klonen:**

```bash
git clone https://github.com/DEIN_USERNAME/ProtoPoC-CustomFilter.git
cd ProtoPoC-CustomFilter
```

2. **Abhängigkeiten installieren:**

```bash
npm install
```

3. **Projekt starten:**

```bash
npm start
```

Frontend läuft auf: [http://localhost:3000](http://localhost:3000)

---

## 📅 Wie funktioniert der Filter?

- Jeder Spaltenfilter basiert auf einem **Checkbox-Menü**.
- Beim An-/Abwählen wird die Tabelle **sofort aktualisiert**.
- Die **FilterStatus-Komponente** zeigt live an, ob Filter aktiv sind.
- Über den **„Filter zurücksetzen“-Button** werden alle Filter entfernt.

---

## 🎯 TODO (Optionale Erweiterungen)

- Suchfeld im Filter-Menü integrieren 🔍
- Filter-Status schöner animieren
- Unterstützung für mehrere Filter kombinieren (UND/ODER)

---

## 🙌 Vielen Dank für deine Zeit!

Dieses Projekt ist bewusst modular und sauber strukturiert,  
damit es leicht erweitert oder angepasst werden kann.

**Viel Spaß beim Weiterentwickeln! 🚀**

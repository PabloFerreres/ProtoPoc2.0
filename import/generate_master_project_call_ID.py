
import pandas as pd
import sqlite3
import hashlib
import re
from collections import defaultdict

# Feste Pfade
db_path = r"C:\Users\ferreres\PycharmProjects\ProtoPoC\db\LordOfRings.db"

# Verbindung zur DB
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Lade Arma_Import
df = pd.read_sql_query("SELECT * FROM Arma_Import", conn)

# Definiere Feldgruppen
static_fields = ["Material", "Gewicht", "Größe", "Hersteller", "Spell", "Magische-Relevanz", "Lieferant"]
project_fields = ["projekt_id", "Bauteil", "Kommentar", "Revision","Ort", "Beschreibung","Gebäude", "Einbauort"]

# Einzigartige Bauteile (statisch)
unique_static = df[static_fields].drop_duplicates().reset_index(drop=True)

# Call-ID Logik pro Hersteller
def get_prefix(hersteller):
    if pd.isna(hersteller) or not hersteller.strip():
        return "XXX"
    clean = re.sub(r'\W+', '', hersteller.upper())
    return clean[:3] if len(clean) >= 3 else clean.ljust(3, "X")

hersteller_counter = defaultdict(int)

# Tabellen löschen und neu erstellen
cursor.execute("DROP TABLE IF EXISTS Bauteile_Master")
cursor.execute("DROP TABLE IF EXISTS Projekt_Bauteile")

# Bauteile_Master Tabelle erstellen
cursor.execute(f"CREATE TABLE Bauteile_Master (call_id TEXT PRIMARY KEY, {', '.join([f'"{col}" TEXT' for col in static_fields])})")

# Projekt_Bauteile Tabelle erstellen
cursor.execute(f"CREATE TABLE Projekt_Bauteile (id INTEGER PRIMARY KEY AUTOINCREMENT, call_id TEXT, {', '.join([f'"{col}" TEXT' for col in project_fields])})")

# Mapping: Kombination → call_id
row_to_call_id = {}
for _, row in unique_static.iterrows():
    hersteller = row["Hersteller"]
    prefix = get_prefix(hersteller)
    hersteller_counter[prefix] += 1
    call_id = f"{prefix}{hersteller_counter[prefix]:03d}"

    cursor.execute(
        f"INSERT INTO Bauteile_Master (call_id, {', '.join([f'"{col}"' for col in static_fields])}) VALUES ({', '.join(['?'] * (len(static_fields) + 1))})",
        (call_id, *[row.get(col, "") for col in static_fields])
    )
    row_to_call_id[tuple(row.get(field, "") for field in static_fields)] = call_id

# Projekt-Bauteile einfügen
inserted = 0
for _, row in df.iterrows():
    key = tuple(row.get(field, "") for field in static_fields)
    call_id = row_to_call_id.get(key)
    cursor.execute(
        f"INSERT INTO Projekt_Bauteile (call_id, {', '.join([f'"{col}"' for col in project_fields])}) VALUES ({', '.join(['?'] * (len(project_fields) + 1))})",
        (call_id, *[row.get(col, "") for col in project_fields])
    )
    inserted += 1

conn.commit()
conn.close()
print(f"Erstellt: {len(unique_static)} Bauteile_Master, {inserted} Projekt_Bauteile.")

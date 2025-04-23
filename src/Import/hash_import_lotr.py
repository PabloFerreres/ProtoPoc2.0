
import pandas as pd
import sqlite3
import os
import hashlib

# Pfade
base_dir = os.path.dirname(os.path.dirname(__file__))
excel_path = r"C:\Users\ferreres\PycharmProjects\ProtoPoC\data\Moria1000.xlsm"
db_path = r"C:\Users\ferreres\PycharmProjects\ProtoPoC\db\LordOfRings.db"

# Lade alle .Arma-Sheets
sheet_names = pd.ExcelFile(excel_path).sheet_names
arma_sheets = [name for name in sheet_names if ".Arma" in name]

# Verbindung zur Datenbank
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Daten sammeln
all_rows = []
columns = None

for sheet in arma_sheets:
    df = pd.read_excel(excel_path, sheet_name=sheet, engine="openpyxl", header=0)
    df = df.drop(index=1)
    df = df.loc[:, ~df.columns.str.contains("^Unnamed")]
    df = df.iloc[1:]
    non_data_cols = ["projekt_id", "hash"]
    data_cols = [col for col in df.columns if col not in non_data_cols]
    # Strip whitespace, convert to empty, prüfen ob alles leer oder NaN
    for col in data_cols:
        df[col] = df[col].astype(str).str.strip().replace("nan", "")
    df = df[~df[data_cols].eq("").all(axis=1)]

    projekt_id = sheet.replace(".", "_").replace(" ", "_")
    df.insert(0, "projekt_id", projekt_id)

    if columns is None:
        columns = df.columns.tolist()

    all_rows.append(df)

# Zusammenführen aller Daten
full_df = pd.concat(all_rows, ignore_index=True)

# Hash berechnen
def row_to_hash(row):
    row_dict = row.dropna().to_dict()
    raw_string = "|".join(f"{k}={v}" for k, v in sorted(row_dict.items()))
    return hashlib.sha256(raw_string.encode("utf-8")).hexdigest()

full_df["hash"] = full_df.apply(row_to_hash, axis=1)

# Tabelle neu erstellen
cursor.execute("DROP TABLE IF EXISTS Arma_Import")
col_defs = ",\n  ".join([f'"{col}" TEXT' for col in full_df.columns])
create_sql = f"CREATE TABLE Arma_Import (id INTEGER PRIMARY KEY AUTOINCREMENT,{col_defs})"
cursor.execute(create_sql)

# Daten einfügen mit Duplikatkontrolle
placeholders = ", ".join(["?"] * len(full_df.columns))
quoted_columns = ', '.join([f'"{col}"' for col in full_df.columns])
insert_sql = f'INSERT INTO Arma_Import ({quoted_columns}) VALUES ({placeholders})'

inserted = 0
skipped = 0

# Prüfe auf bestehende Hashes
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Arma_Import'")
table_exists = cursor.fetchone()

existing_hashes = set()
if table_exists:
    cursor.execute("SELECT hash FROM Arma_Import")
    existing_hashes = set(row[0] for row in cursor.fetchall())

for _, row in full_df.iterrows():
    if row["hash"] in existing_hashes:
        skipped += 1
        continue
    cursor.execute(insert_sql, tuple(row))
    inserted += 1

conn.commit()
conn.close()

print(f"Import abgeschlossen: {inserted} neue Zeilen eingefügt, {skipped} Duplikate übersprungen.")

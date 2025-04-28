import sqlite3
import json

DB_PATH = "db/SimpleTest.db"

def get_all_rows():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM TestBauteile")
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    conn.close()
    return [dict(zip(columns, row)) for row in rows]

def update_row(row):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    set_clause = ", ".join([f"{col} = ?" for col in row.keys() if col != "id"])
    values = tuple(row[col] for col in row.keys() if col != "id") + (row["id"],)
    cur.execute(f"""
        UPDATE TestBauteile
        SET {set_clause}
        WHERE id = ?
    """, values)
    conn.commit()
    conn.close()
    return {"status": "success", "message": "Row updated"}

def save_layout(projekt_id, view_type, column_settings):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Layouts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            projekt_id TEXT,
            view_type TEXT,
            column_settings TEXT
        )
    """)
    cur.execute("DELETE FROM Layouts WHERE projekt_id = ? AND view_type = ?", (projekt_id, view_type))
    cur.execute("""
        INSERT INTO Layouts (projekt_id, view_type, column_settings)
        VALUES (?, ?, ?)
    """, (projekt_id, view_type, json.dumps(column_settings)))
    conn.commit()
    conn.close()
    return {"status": "success", "message": "Layout gespeichert"}

def load_layout(projekt_id, view_type):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        SELECT column_settings FROM Layouts
        WHERE projekt_id = ? AND view_type = ?
    """, (projekt_id, view_type))
    row = cur.fetchone()
    conn.close()
    if row:
        return json.loads(row[0])
    return None

import sqlite3

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

if __name__ == "__main__":
    print("DB-Modul für TestBauteile bereit.")

import sqlite3

DB_PATH = "db/LordOfRings.db"

def get_all_projects():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT projekt_id FROM Projekt_Bauteile")
    result = [r[0] for r in cur.fetchall()]
    conn.close()
    return result

def get_project_data(projekt_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        SELECT 
            p.call_id AS "Call-ID", p.projekt_id AS "Ort", 
            m."Magische-Relevanz", p."Gebäude", 
            p.Bauteil, m.Gewicht, m.Material, m.Größe, m.Spell, 
            m.Hersteller, m.Lieferant, p."Einbauort", 
            p."Beschreibung", p.Revision
        FROM Projekt_Bauteile p
        LEFT JOIN Bauteile_Master m ON p.call_id = m.call_id
        WHERE p.projekt_id = ?
    """, (projekt_id,))

    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    conn.close()
    return [dict(zip(columns, row)) for row in rows]
def update_project_row(row):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        """
        UPDATE Projekt_Bauteile
        SET Bauteil = ?, Revision = ?, Beschreibung = ?
        WHERE call_id = ? AND projekt_id = ?
        """,
        (row["Bauteil"], row["Revision"], row["Beschreibung"], row["Call-ID"], row["Ort"])
    )
    conn.commit()
    conn.close()
    return {"status": "success", "message": "Row updated"}

def get_all_master_data():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Bauteile_Master")
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    conn.close()
    return [dict(zip(columns, row)) for row in rows]

def update_master_row_data(row):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        """
        UPDATE Bauteile_Master
        SET Material = ?, Gewicht = ?, Größe = ?, Hersteller = ?, Spell = ?, "Magische-Relevanz" = ?, Lieferant = ?
        WHERE call_id = ?
        """,
        (
            row["Material"], row["Gewicht"], row["Größe"], row["Hersteller"],
            row["Spell"], row["Magische-Relevanz"], row["Lieferant"],
            row["call_id"]
        )
    )
    conn.commit()
    conn.close()
    return {"status": "success", "message": "Masterdatensatz aktualisiert"}

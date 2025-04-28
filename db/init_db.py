import sqlite3

conn = sqlite3.connect("db/LordOfRings.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS GridLayouts (
    projekt_id TEXT,
    view_type TEXT, -- 'project' oder 'master'
    column_settings TEXT, -- z. B. {"Bauteil": {"width": 120, "order": 1}, ...}
    row_height INTEGER,
    PRIMARY KEY (projekt_id, view_type)
)
""")

conn.commit()
conn.close()

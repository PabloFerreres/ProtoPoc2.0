
import streamlit as st
import pandas as pd
import sqlite3

# Feste Pfade
db_path = r"C:\Users\ferreres\PycharmProjects\ProtoPoC\db\LordOfRings.db"

# Verbindung zur DB
conn = sqlite3.connect(db_path)

# Titel und Layout
st.set_page_config(page_title="ProtoPoC – Projekt Editor + Master", layout="wide")
st.title("🔧 ProtoPoC – Projektbearbeitung + Bauteile-Master")

# Projekt-IDs dynamisch laden
projekt_ids = pd.read_sql_query("SELECT DISTINCT projekt_id FROM Projekt_Bauteile ORDER BY projekt_id", conn)
projekt_liste = projekt_ids["projekt_id"].tolist()

# Auswahl + Master-Option
auswahl = st.selectbox("Wähle einen Bereich:", projekt_liste + ["📘 Bauteile_Master"])

# Wenn Master angezeigt werden soll
if auswahl == "📘 Bauteile_Master":
    df_master = pd.read_sql_query("SELECT * FROM Bauteile_Master", conn)
    st.subheader("📘 Bauteile_Master – Technische Eigenschaften")
    st.dataframe(df_master, use_container_width=True)

else:
    # JOIN Projekt_Bauteile + Bauteile_Master
    query = f'''
    SELECT 
        p.id, p.call_id, p.projekt_id, p.Bauteil, p.Kommentar, p.Revision,
        m.Material, m.Gewicht, m.Größe, m.Hersteller, m.Spell, m."Magische-Relevanz"
    FROM Projekt_Bauteile p
    LEFT JOIN Bauteile_Master m ON p.call_id = m.call_id
    WHERE p.projekt_id = ?
    ORDER BY p.id
    '''
    df = pd.read_sql_query(query, conn, params=[auswahl])

    original_df = df.copy()

    column_order = [
        "id", "projekt_id", "call_id",
        "Bauteil", "Kommentar", "Revision",
        "Material", "Gewicht", "Größe", "Hersteller", "Spell", "Magische-Relevanz"
    ]
    df = df[column_order]

    st.subheader(f"✏️ Projekt-Editor für: {auswahl}")
    edited_df = st.data_editor(
        df,
        use_container_width=True,
        disabled=["id", "projekt_id", "call_id", "Material", "Gewicht", "Größe", "Hersteller", "Spell", "Magische-Relevanz"]
    )

    if st.button("💾 Änderungen speichern"):
        updates = 0
        for _, row in edited_df.iterrows():
            orig_row = original_df.loc[original_df["id"] == row["id"]].iloc[0]
            if any([
                row["Bauteil"] != orig_row["Bauteil"],
                row["Kommentar"] != orig_row["Kommentar"],
                row["Revision"] != orig_row["Revision"]
            ]):
                conn.execute(
                    "UPDATE Projekt_Bauteile SET Bauteil = ?, Kommentar = ?, Revision = ? WHERE id = ?",
                    (row["Bauteil"], row["Kommentar"], row["Revision"], row["id"])
                )
                updates += 1
        conn.commit()
        st.success(f"✅ {updates} Zeilen aktualisiert.")

conn.close()

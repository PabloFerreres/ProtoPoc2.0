
import streamlit as st
import pandas as pd
import sqlite3
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, JsCode

def run_aggrid_editor():
    st.subheader("📊 Projekt-Bearbeitung – Excel-Header-Stil (mit Theme: Material)")

    db_path = r"C:\Users\ferreres\PycharmProjects\ProtoPoC\db\LordOfRings.db"
    conn = sqlite3.connect(db_path)

    projekt_ids = pd.read_sql_query("SELECT DISTINCT projekt_id FROM Projekt_Bauteile ORDER BY projekt_id", conn)
    projekt_liste = projekt_ids["projekt_id"].tolist()
    projekt_id = st.selectbox("Wähle ein Projekt-Teil:", projekt_liste)

    query = (
        "SELECT "
        "p.id, p.call_id AS 'Call-ID', Ort, p.projekt_id, m.'Magische-Relevanz', "
        "Gebäude, p.Bauteil, m.Gewicht, m.Material, m.Größe, m.Spell, "
        "m.Hersteller, m.Lieferant, Einbauort, Beschreibung, p.Revision "
        "FROM Projekt_Bauteile p "
        "LEFT JOIN Bauteile_Master m ON p.call_id = m.call_id "
        "WHERE p.projekt_id = ? "
        "ORDER BY p.id"
    )

    df = pd.read_sql_query(query, conn, params=[projekt_id])
    conn.close()

    column_order = [
        "Call-ID", "Ort", "Magische-Relevanz", "Gebäude", "Bauteil",
        "Gewicht", "Material", "Größe", "Spell", "Hersteller",
        "Lieferant", "Einbauort", "Beschreibung", "Revision"
    ]
    df = df[column_order]

    header_style = {
        "Call-ID": "#7e57c2",
        "Ort": "#c8e6c9",
        "Magische-Relevanz": "#dcedc8",
        "Gebäude": "#ffffff",
        "Bauteil": "#dcedc8",
        "Gewicht": "#bbdefb",
        "Material": "#bbdefb",
        "Größe": "#bbdefb",
        "Spell": "#bbdefb",
        "Hersteller": "#bbdefb",
        "Lieferant": "#bbdefb",
        "Einbauort": "#dcedc8",
        "Beschreibung": "#ffe0b2",
        "Revision": "#ffffff"
    }

    gb = GridOptionsBuilder.from_dataframe(df)
    editable_cols = ["Bauteil", "Kommentar", "Revision", "Beschreibung"]

    for col in df.columns:
        gb.configure_column(
            col,
            editable=col in editable_cols,
            headerClass=f'header_{col.replace(" ", "_")}',
            wrapText=True,
            autoHeight=True
        )

    css_blocks = []
    for col, color in header_style.items():
        class_name = f'header_{col.replace(" ", "_")}'
        css_block = f""".ag-theme-material .{class_name} {{
            background-color: {color} !important;
            font-weight: bold;
            color: black;
        }}"""
        css_blocks.append(css_block)

    st.markdown(f"<style>{''.join(css_blocks)}</style>", unsafe_allow_html=True)

    grid_return = AgGrid(
        df,
        gridOptions=gb.build(),
        update_mode=GridUpdateMode.MANUAL,
        allow_unsafe_jscode=True,
        theme="material",  # <- Theme geändert für funktionierende headerClass
        fit_columns_on_grid_load=True
    )

    if st.button("💾 Änderungen speichern"):
        updated_df = grid_return["data"]
        conn = sqlite3.connect(db_path)
        updates = 0
        for _, row in updated_df.iterrows():
            conn.execute(
                "UPDATE Projekt_Bauteile SET Bauteil = ?, Revision = ?, Beschreibung = ? WHERE call_id = ? AND projekt_id = ?",
                (row["Bauteil"], row["Revision"], row["Beschreibung"], row["Call-ID"], projekt_id)
            )
            updates += 1
        conn.commit()
        conn.close()
        st.success(f"✅ {updates} Zeilen gespeichert.")

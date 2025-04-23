
import streamlit as st
import pandas as pd
import sqlite3

def run_master_view():
    st.subheader("📘 Bauteile_Master – Technische Übersicht")

    db_path = r"C:\Users\ferreres\PycharmProjects\ProtoPoC\db\LordOfRings.db"
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM Bauteile_Master", conn)
    conn.close()

    st.dataframe(df, use_container_width=True)

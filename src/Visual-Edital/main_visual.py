
import streamlit as st

# Importierte Module
from edit_project_aggrid import run_aggrid_editor
from view_master import run_master_view

st.set_page_config(page_title="ProtoPoC – Visual Hub", layout="wide")
st.title("🧭 ProtoPoC – Visualisierung & Bearbeitung")

# Navigation
option = st.sidebar.radio(
    "📁 Navigation",
    [
        "🏗 Projekt-Bauteile bearbeiten (AgGrid)",
        "📘 Bauteile_Master anzeigen"
    ]
)

# Module ausführen je nach Auswahl
if option == "🏗 Projekt-Bauteile bearbeiten (AgGrid)":
    run_aggrid_editor()

elif option == "📘 Bauteile_Master anzeigen":
    run_master_view()

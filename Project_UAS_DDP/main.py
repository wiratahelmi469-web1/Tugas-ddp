import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

from datetime import datetime
from Dashboard import dashboard
from Database import database
from Dokumentasi import dokumentasi
from Laporan_Penjualan import laporan_penjualan

custom_css = """
<style>
[data-testid="stAppViewCountainer"]{
    background-color:white;
}
    
[data-testid="stHeader"]{
    background-color:#FFE8D7;
}

[data-testid="stSidebar"]{
    background-color:#ffcda5;
}

h1,h3{
    color:orage !important;
    font-weight: bold !important;
}


table{
    background-color:orage !important;
    font-weight: bold !important;
}

</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

DATA_FILE = "data_penjualan.csv"

st.set_page_config(page_title="Manajemen UMKM", layout="wide")


# INIT SESSION STATE 

if "data_penjualan" not in st.session_state:
    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE)
        df["Tanggal"] = pd.to_datetime(df["Tanggal"])
    else:
        df = pd.DataFrame(
            columns=["Tanggal", "Produk", "Jumlah", "Harga", "Total"]
        )

    st.session_state.data_penjualan = df

# SIDEBAR

menu = st.sidebar.radio(
    "Menu",
    ["Dashboard", "Database", "Laporan Penjualan", "Dokumentasi"]
)

if menu == "Dashboard":
    dashboard()
elif menu == "Database":
    database()
elif menu == "Laporan Penjualan":
    laporan_penjualan()
elif menu == "Dokumentasi":
    dokumentasi()
 
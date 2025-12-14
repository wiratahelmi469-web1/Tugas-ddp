import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import csv
from datetime import datetime

DATA_FILE = "data_penjualan.csv"

st.set_page_config(
    page_title="Manajemen UMKM",
    layout="wide"
)

# ===============================
# LOAD DATA (CSV PERSISTENT)
# ===============================
if os.path.exists(DATA_FILE):
    data_penjualan = pd.read_csv(DATA_FILE)
    data_penjualan["Tanggal"] = pd.to_datetime(data_penjualan["Tanggal"])
else:
    data_penjualan = pd.DataFrame(
        columns=["Tanggal", "Produk", "Jumlah", "Harga", "Total"]
    )

# ===============================
# INIT SESSION STATE
# ===============================
if "data_penjualan" not in st.session_state:
    st.session_state.data_penjualan = data_penjualan.copy()

def dashboard():
    st.title("Dashboard UMKM")
    st.markdown("### Ringkasan Penjualan")

    df = st.session_state.data_penjualan.copy()
    
    if df.empty:
        st.info("Belum ada data penjualan.")
        return

    total_penjualan = df["Total"].sum()
    rata_harian = df.groupby(df["Tanggal"].dt.date)["Total"].sum().mean()
    produk_terlaris = df.groupby("Produk")["Jumlah"].sum().idxmax()

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Penjualan", f"Rp {total_penjualan:,.0f}")
    col2.metric("Rata-rata Harian", f"Rp {rata_harian:,.0f}")
    col3.metric("Produk Terlaris", produk_terlaris)

    df["Bulan"] = df["Tanggal"].dt.to_period("M")
    bulanan = df.groupby("Bulan")["Total"].sum().reset_index()
    bulanan["Bulan"] = bulanan["Bulan"].astype(str)

    fig, ax = plt.subplots()
    sns.barplot(data=bulanan, x="Bulan", y="Total", ax=ax)
    ax.set_title("Penjualan Bulanan")
    plt.xticks(rotation=45)
    st.pyplot(fig)

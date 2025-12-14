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


# LOAD DATA (CSV PERSISTENT)

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

def laporan_penjualan():
    st.title("Laporan Penjualan UMKM")
    st.markdown("### Laporan Bulanan")

    df = st.session_state.data_penjualan.copy()
    if df.empty:
        st.info("Belum ada data.")
        return

    df["Bulan"] = df["Tanggal"].dt.month

    nama_bulan = {
        1: "Januari", 2: "Februari", 3: "Maret", 4: "April",
        5: "Mei", 6: "Juni", 7: "Juli", 8: "Agustus",
        9: "September", 10: "Oktober", 11: "November", 12: "Desember"
    }

    bulan = st.selectbox(
        "Pilih Bulan",
        options=range(1, 13),
        format_func=lambda x: nama_bulan[x]
    )

    laporan = df[df["Bulan"] == bulan]
    total = laporan["Total"].sum()

    st.metric(
        f"Total Penjualan Bulan {nama_bulan[bulan]}",
        f"Rp {total:,.0f}"
    )

    if laporan.empty:
        st.warning("Tidak ada data untuk bulan ini.")
        return

    st.dataframe(
        laporan.groupby("Produk")
        .agg(Jumlah=("Jumlah", "sum"), Total=("Total", "sum"))
        .reset_index(),
        use_container_width=True
    )

    fig, ax = plt.subplots()
    laporan.groupby("Produk")["Total"].sum().plot(
        kind="pie",
        autopct="%1.1f%%",
        ax=ax
    )
    ax.set_ylabel("")
    ax.set_title(f"Distribusi Penjualan {nama_bulan[bulan]}")
    st.pyplot(fig)
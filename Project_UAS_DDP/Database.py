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


# INIT SESSION STATE

if "data_penjualan" not in st.session_state:
    st.session_state.data_penjualan = data_penjualan.copy()
    
def database():
    st.title("Database UMKM")
    st.markdown("### Data Penjualan")

    df = st.session_state.data_penjualan
    df["Tanggal"] = pd.to_datetime(df["Tanggal"])

    produk_filter = st.multiselect(
        "Filter Produk",
        options=sorted(df["Produk"].dropna().unique()),
        default=sorted(df["Produk"].dropna().unique())
    )

    if not df.empty:
        min_tanggal = df["Tanggal"].min().date()
        max_tanggal = max(df["Tanggal"].max().date(), datetime.today().date())
    else:
        min_tanggal = max_tanggal = datetime.today().date()

    tanggal_filter = st.date_input(
        "Filter Tanggal",
        value=(min_tanggal, max_tanggal)
    )

    start_date = pd.to_datetime(tanggal_filter[0])
    end_date = pd.to_datetime(tanggal_filter[1]) + pd.Timedelta(days=1)

    filtered_data = df[
        (df["Produk"].isin(produk_filter)) &
        (df["Tanggal"] >= start_date) &
        (df["Tanggal"] < end_date)
    ]

    st.dataframe(filtered_data, use_container_width=True)

    # ===============================
    # TAMBAH DATA
    # ===============================
    st.markdown("### Tambah Data Baru")
    with st.form("tambah_data", clear_on_submit=True):
        tanggal = st.date_input("Tanggal", value=datetime.today())
        produk = st.text_input("Produk")
        jumlah = st.number_input("Jumlah", min_value=1, step=1)
        harga = st.number_input("Harga", min_value=1000, step=1000)
        submit = st.form_submit_button("Simpan")

        if submit:
            if not produk.strip():
                st.error("Nama produk tidak boleh kosong")
                return

            data_baru = {
                "Tanggal": pd.to_datetime(tanggal),
                "Produk": produk,
                "Jumlah": jumlah,
                "Harga": harga,
                "Total": jumlah * harga
            }

            st.session_state.data_penjualan = pd.concat(
                [df, pd.DataFrame([data_baru])],
                ignore_index=True
            )

            st.session_state.data_penjualan.to_csv(DATA_FILE, index=False)
            st.success("Data berhasil disimpan")
            st.rerun()
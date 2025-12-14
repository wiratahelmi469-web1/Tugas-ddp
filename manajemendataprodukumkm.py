import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime

# ===============================
# KONFIGURASI
# ===============================
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

# ===============================
# DASHBOARD
# ===============================
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

# ===============================
# DATABASE
# ===============================
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

# ===============================
# LAPORAN
# ===============================
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

# ===============================
# DOKUMENTASI
# ===============================
def dokumentasi():
     st.title('Dokumentasi UMKM')
     st.header('Informasi dan Dokumentasi UMKM buatan kelompok 1')
     st.markdown('Selamat datang di aplikasi UMKM. Aplikasi ini bertujuan untuk memberikan informasi lengkap mengenai Usaha Mikro, Kecil, dan Menengah (UMKM).')
     st.subheader('Apa itu UMKM?')
     st.markdown('UMKM adalah singkatan dari Usaha Mikro, Kecil, dan Menengah. UMKM memainkan peran penting dalam perekonomian Indonesia dengan menyumbang sebagian besar lapangan kerja dan produk domestik bruto (PDB).')
     st.subheader('Kategori UMKM')
     st.markdown('1. Usaha Mikro: Usaha yang dijalankan oleh individu atau kelompok dengan aset maksimal Rp10 juta dan omset tahunan maksimal Rp100 juta.\n2. Usaha Kecil:Usaha  yang dijayang memiliki aset antara Rp10 juta hingga Rp100 juta dan omset tahunan antara Rp300 juta hingga Rp2,5 miliar.\n3. Usaha Menengah: Memiliki aset antara Rp500 juta hingga Rp10 miliar dan omset tahunan antara Rp2,5 miliar hingga Rp50 miliar.')
     st.subheader('Manfaat UMKM')
     st.markdown('- Penciptaan Lapangan Kerja: UMKM menyerap tenaga kerja dalam jumlah besar, membantu mengurangi tingkat pengangguran.\n- Pemberdayaan Ekonomi Lokal: UMKM seringkali beroperasi di komunitas lokal, sehingga membantu meningkatkan perekonomian daerah.\n- Inovasi dan Kreativitas: UMKM seringkali menjadi sumber inovasi produk dan layanan baru yang sesuai dengan kebutuhan pasar lokal.')
     st.subheader('Dukungan untuk UMKM')
     st.markdown('- Pelatihan dan Pendidikan: Pemerintah dan berbagai organisasi menyediakan pelatihan untuk meningkatkan keterampilan manajemen dan teknis pelaku UMKM.\n- Akses Pembiayaan: Berbagai program pinjaman dan hibah disediakan untuk membantu UMKM mendapatkan modal usaha.\n- Pemasaran dan Promosi: Dukungan dalam hal pemasaran produk UMKM melalui pameran, platform digital, dan jaringan distribusi.')
     st.subheader('Kesimpulan')
     st.markdown('UMKM merupakan tulang punggung perekonomian Indonesia yang memberikan kontribusi signifikan terhadap penciptaan lapangan kerja dan pemberdayaan ekonomi lokal. Dukungan yang berkelanjutan dari pemerintah dan masyarakat sangat penting untuk memastikan pertumbuhan dan keberlanjutan UMKM di masa depan.')
     st.image('https://batambisnis.com/wp-content/uploads/2025/09/Pengertian-apa-itu-UMKM-780x470.jpeg', caption='Ilustrasi Dokumentasi UMKM')
     st.markdown('Terima kasih telah mengunjungi aplikasi UMKM kami. Semoga informasi ini bisa membantu kita dalam memahami pentingnya UMKM dalam perekonomian')
    
# ===============================
# NAVIGASI
# ===============================
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
 
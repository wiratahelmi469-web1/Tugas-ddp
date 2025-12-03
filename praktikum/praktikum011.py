import streamlit as st
st.title("Aplikasi pembayaran spp")
st.write("Silahkan isi form pembayaran spp dibawah ini")

with st.form("pembayaran_spp_form"):
    nama = st.text_input("Nama Lengkap")
    nisn = st.text_input("NISN")
    bulan = st.selectbox("Bulan Pembayaran", ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"])
    jumlah = st.number_input("Jumlah Pembayaran (Rp)", min_value=0, step=1000)
    metode_pembayaran = st.selectbox("Metode Pembayaran", ["Transfer Bank", "E-Wallet", "Tunai"])
    submit_button = st.form_submit_button("Bayar")

if submit_button:
    st.subheader("Detail Pembayaran SPP")
    st.write(f"**Nama Lengkap:** {nama}")
    st.write(f"**NISN:** {nisn}")
    st.write(f"**Bulan Pembayaran:** {bulan}")
    st.write(f"**Jumlah Pembayaran:** Rp {jumlah}")
    st.write(f"**Metode Pembayaran:** {metode_pembayaran}")
    st.success("Pembayaran SPP Anda telah berhasil diproses!")
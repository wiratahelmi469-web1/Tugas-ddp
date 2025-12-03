import streamlit as st

st.title("aplikasi data diri")
st.write("Silahkan isi data diri anda pada form dibawah ini")

with st.form("data_diri_form"):
    nama = st.text_input("Nama Lengkap")
    umur = st.number_input("Umur", min_value=0, max_value=120, step=1)
    alamat = st.text_area("Alamat")
    pekerjaan = st.selectbox("Pekerjaan", ["Pelajar", "Mahasiswa", "Karyawan", "Wiraswasta", "Lainnya"])
    email = st.text_input("Email")
    submit_button = st.form_submit_button("Kirim")


if submit_button:
    st.subheader("Data Diri Anda")
    st.write(f"**Nama Lengkap:** {nama}")
    st.write(f"**Umur:** {umur} tahun")
    st.write(f"**Alamat:** {alamat}")
    st.write(f"**Pekerjaan:** {pekerjaan}")
    st.success("Data diri Anda telah berhasil dikirim!")



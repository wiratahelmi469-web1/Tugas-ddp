import streamlit as st  
st.title("aplikasi aritmatika sederhana")
st.write("Silahkan masukkan dua angka untuk melakukan operasi aritmatika sederhana")

with st.form("aritmatika_form"):
    angka1 = st.number_input("Masukkan Angka Pertama", value=0)
    angka2 = st.number_input("Masukkan Angka Kedua", value=0)
    operasi = st.selectbox("Pilih Operasi", ["Penjumlahan", "Pengurangan", "Perkalian", "Pembagian"])
    submit_button = st.form_submit_button("Hitung")

if submit_button:
    if operasi == "Penjumlahan":
        hasil = angka1 + angka2
        st.write(f"Hasil Penjumlahan: {angka1} + {angka2} = {hasil}")
    elif operasi == "Pengurangan":
        hasil = angka1 - angka2
        st.write(f"Hasil Pengurangan: {angka1} - {angka2} = {hasil}")
    elif operasi == "Perkalian":
        hasil = angka1 * angka2
        st.write(f"Hasil Perkalian: {angka1} * {angka2} = {hasil}")
    elif operasi == "Pembagian":
        if angka2 != 0:
            hasil = angka1 / angka2
            st.write(f"Hasil Pembagian: {angka1} / {angka2} = {hasil}")
        else:
            st.error("Error: Pembagian dengan nol tidak diperbolehkan.")
    st.success("Operasi aritmatika selesai!")

    
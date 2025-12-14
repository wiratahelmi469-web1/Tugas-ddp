import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import csv
from datetime import datetime

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
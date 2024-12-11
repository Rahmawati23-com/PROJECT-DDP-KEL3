import streamlit as st
import pandas as pd
from datetime import datetime

# Inisialisasi data anggaran (simulasi database)
if 'anggaran' not in st.session_state:
    st.session_state.anggaran = pd.DataFrame(columns=['ID', 'Nama Anggaran', 'Jumlah', 'Tanggal Pengajuan', 'Status'])

# Fungsi untuk menambah anggaran
def ajukan_anggaran(nama_anggaran, jumlah):
    id_anggaran = len(st.session_state.anggaran) + 1
    tanggal_pengajuan = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = "Menunggu Persetujuan"
    
    # Menambahkan data ke dalam DataFrame
    anggaran_baru = pd.DataFrame([[id_anggaran, nama_anggaran, jumlah, tanggal_pengajuan, status]],
                                 columns=['ID', 'Nama Anggaran', 'Jumlah', 'Tanggal Pengajuan', 'Status'])
    st.session_state.anggaran = pd.concat([st.session_state.anggaran, anggaran_baru], ignore_index=True)
    
# Fungsi untuk menyetujui atau menolak anggaran
def proses_anggaran(id_anggaran, status):
    st.session_state.anggaran.loc[st.session_state.anggaran['ID'] == id_anggaran, 'Status'] = status

# Judul Aplikasi
st.title("Sistem Persetujuan Anggaran")

# Menampilkan daftar anggaran yang sudah diajukan
st.header("Daftar Anggaran yang Telah Diajukan")
st.dataframe(st.session_state.anggaran)

# Proses persetujuan anggaran
st.header("Proses Persetujuan Anggaran")
selected_id = st.selectbox("Pilih ID Anggaran yang akan diproses", st.session_state.anggaran['ID'])
status_persetujuan = st.radio("Status Persetujuan", ('Setujui', 'Tolak'))

if st.button("Proses Persetujuan"):
    if selected_id:
        status = 'Disetujui' if status_persetujuan == 'Setujui' else 'Ditolak'
        proses_anggaran(selected_id, status)
        st.success(f"Anggaran dengan ID {selected_id} telah {status.lower()}.")

# Menambahkan fitur untuk menampilkan status anggaran yang sudah diproses
st.header("Status Anggaran")
status_filter = st.selectbox("Tampilkan status", ['Semua', 'Menunggu Persetujuan', 'Disetujui', 'Ditolak'])

if status_filter != 'Semua':
    anggaran_filtered = st.session_state.anggaran[st.session_state.anggaran['Status'] == status_filter]
else:
    anggaran_filtered = st.session_state.anggaran

st.dataframe(anggaran_filtered)
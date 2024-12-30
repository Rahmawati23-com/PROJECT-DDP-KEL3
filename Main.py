import streamlit as st
from danasosial import DanaSosial
from dashboard import tampilkan_dashboard
from pemasukan import pencatatan_pemasukan
from pengeluaran import pencatatan_pengeluaran
from persetujuan import persetujuan_pengeluaran

if "dana_sosial" not in st.session_state:
    st.session_state.dana_sosial = DanaSosial()

dana_sosial = st.session_state.dana_sosial

st.sidebar.title("Aplikasi Pengelolaan Dana Sosial")
menu = st.sidebar.radio("Pilih Menu", [
    "🏠Dashboard", 
    "➕Pencatatan Pemasukan", 
    "💸Pencatatan Pengeluaran", 
    "✅Persetujuan Pengeluaran"
])

if menu == "Dashboard":
    tampilkan_dashboard(dana_sosial)
elif menu == "Pencatatan Pemasukan":
    pencatatan_pemasukan(dana_sosial)
elif menu == "Pencatatan Pengeluaran":
    pencatatan_pengeluaran(dana_sosial)
elif menu == "Persetujuan Pengeluaran":
    persetujuan_pengeluaran(dana_sosial)

import streamlit as st
from danasosial import DanaSosial
from streamlit_option_menu import option_menu
from dashboard import tampilkan_dashboard
from pemasukan import pencatatan_pemasukan
from pengeluaran import pencatatan_pengeluaran
from persetujuan import persetujuan_pengeluaran
from tentangkami import tentang_kami

if "dana_sosial" not in st.session_state:
    st.session_state.dana_sosial = DanaSosial()

dana_sosial = st.session_state.dana_sosial

with st.sidebar:
    st.title("Aplikasi Pengelolaan Dana Sosial")
    menu = option_menu(
        "Menu Utama",
        ["Dashboard", "Pencatatan Pemasukan", "Pencatatan Pengeluaran", 
         "Persetujuan Pengeluaran", "Tentang Kami"],
        icons=["house", "file-plus", "file-minus", "check-circle", "info-circle"],
        menu_icon="list",
        default_index=0,
    )

if menu == "Dashboard":
    tampilkan_dashboard(dana_sosial)
elif menu == "Pencatatan Pemasukan":
    pencatatan_pemasukan(dana_sosial)
elif menu == "Pencatatan Pengeluaran":
    pencatatan_pengeluaran(dana_sosial)
elif menu == "Persetujuan Pengeluaran":
    persetujuan_pengeluaran(dana_sosial)
elif menu == "Tentang Kami":
    tentang_kami() 

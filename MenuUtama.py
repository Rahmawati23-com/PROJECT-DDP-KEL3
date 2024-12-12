# Menu Utama
st.sidebar.title("Aplikasi Pengelolaan Dana Sosial")
menu = st.sidebar.radio("Pilih Menu", [
    "Dashboard", 
    "Pencatatan Pemasukan", 
    "Pencatatan Pengeluaran", 
    "Persetujuan Pengeluaran"
])

# Pemanggilan Fungsi 
if menu == "Dashboard":
    tampilkan_dashboard(dana_sosial)
elif menu == "Pencatatan Pemasukan":
    pencatatan_pemasukan(dana_sosial)
elif menu == "Pencatatan Pengeluaran":
    pencatatan_pengeluaran(dana_sosial)
elif menu == "Persetujuan Pengeluaran":
    persetujuan_pengeluaran(dana_sosial)

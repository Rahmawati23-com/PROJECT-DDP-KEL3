import streamlit as st
import pandas as pd
from datetime import datetime
import os

# **Class untuk Mengelola Dana Sosial**
class DanaSosial:
    def __init__(self):
        self.pemasukan_file = "pemasukan.csv"
        self.pengeluaran_file = "pengeluaran.csv"
        self.saldo = 0
        self._load_data()

    # **Load data dari file CSV**
    def _load_data(self):
        if os.path.exists(self.pemasukan_file):
            self.pemasukan = pd.read_csv(self.pemasukan_file)
        else:
            self.pemasukan = pd.DataFrame(columns=["Tanggal", "Sumber", "Jumlah", "Petugas"])

        if os.path.exists(self.pengeluaran_file):
            self.pengeluaran = pd.read_csv(self.pengeluaran_file)
        else:
            self.pengeluaran = pd.DataFrame(columns=["Tanggal", "Tujuan", "Jumlah", "Petugas", "Status"])

        # Hitung saldo dari data
        total_pemasukan = self.pemasukan["Jumlah"].sum() if not self.pemasukan.empty else 0
        total_pengeluaran = self.pengeluaran.loc[self.pengeluaran["Status"] == "Disetujui", "Jumlah"].sum() \
            if not self.pengeluaran.empty else 0
        self.saldo = total_pemasukan - total_pengeluaran

    # **Simpan data ke file CSV**
    def _save_data(self):
        self.pemasukan.to_csv(self.pemasukan_file, index=False)
        self.pengeluaran.to_csv(self.pengeluaran_file, index=False)

    # Fungsi untuk menambah pemasukan
    def tambah_pemasukan(self, jumlah, sumber, petugas):
        if jumlah > 0 and sumber and petugas:
            new_entry = pd.DataFrame([{
                "Tanggal": datetime.now().strftime("%Y-%m-%d"),
                "Sumber": sumber,
                "Jumlah": jumlah,
                "Petugas": petugas,
            }])
            self.pemasukan = pd.concat([self.pemasukan, new_entry], ignore_index=True)
            self._save_data()
            self._load_data()
            return True
        return False

    # Fungsi untuk mengajukan pengeluaran
    def tambah_pengeluaran(self, jumlah, tujuan, petugas):
        if jumlah > 0 and tujuan and petugas:
            new_entry = pd.DataFrame([{
                "Tanggal": datetime.now().strftime("%Y-%m-%d"),
                "Tujuan": tujuan,
                "Jumlah": jumlah,
                "Petugas": petugas,
                "Status": "Menunggu Persetujuan",
            }])
            self.pengeluaran = pd.concat([self.pengeluaran, new_entry], ignore_index=True)
            self._save_data()
            self._load_data()
            return True
        return False

    # Fungsi untuk menyetujui pengeluaran
    def setujui_pengeluaran(self, index):
        if 0 <= index < len(self.pengeluaran):
            pengeluaran_row = self.pengeluaran.iloc[index]
            if pengeluaran_row["Jumlah"] <= self.saldo:
                self.pengeluaran.loc[index, "Status"] = "Disetujui"
                self._save_data()
                self._load_data()
                return True
            else:
                return False  # Saldo tidak mencukupi
        return False

    # Fungsi untuk menolak pengeluaran
    def tolak_pengeluaran(self, index):
        if 0 <= index < len(self.pengeluaran):
            self.pengeluaran.loc[index, "Status"] = "Ditolak"
            self._save_data()
            self._load_data()
            return True
        return False

    # Fungsi untuk membuat laporan
    def download_laporan(self):
        laporan_file = "laporan_keuangan.xlsx"
        with pd.ExcelWriter(laporan_file, engine='xlsxwriter') as writer:
            self.pemasukan.to_excel(writer, sheet_name="Pemasukan", index=False)
            self.pengeluaran.to_excel(writer, sheet_name="Pengeluaran", index=False)
        return laporan_file

# **Inisialisasi Objek Dana Sosial**
if "dana_sosial" not in st.session_state:
    st.session_state.dana_sosial = DanaSosial()

dana_sosial = st.session_state.dana_sosial


# **Fungsi Dashboard**
def tampilkan_dashboard():
    st.header("Dashboard Keuangan")

    # Ringkasan keuangan
    st.write(f"**Saldo Kas:** Rp {dana_sosial.saldo:,.2f}")
    st.write("### Pemasukan")
    st.table(dana_sosial.pemasukan)
    st.write("### Pengeluaran")
    st.table(dana_sosial.pengeluaran)

    # Unduh laporan
    laporan_file = dana_sosial.download_laporan()
    with open(laporan_file, "rb") as file:
        st.download_button("Download Laporan Keuangan", data=file, file_name="laporan_keuangan.xlsx")


# **Fungsi Pencatatan Pemasukan**
def pencatatan_pemasukan():
    st.header("Pencatatan Pemasukan")
    with st.form("form_pemasukan"):
        jumlah = st.number_input("Jumlah Pemasukan (Rp):", min_value=0, step=1000)
        sumber = st.text_input("Sumber Pemasukan:")
        petugas = st.text_input("Nama Petugas:")
        submitted = st.form_submit_button("Tambah Pemasukan")
        if submitted:
            if dana_sosial.tambah_pemasukan(jumlah, sumber, petugas):
                st.success("Pemasukan berhasil ditambahkan!")
            else:
                st.error("Harap isi semua kolom dengan benar.")

# **Fungsi Pencatatan Pengeluaran**
def pencatatan_pengeluaran():
    st.header("Pencatatan Pengeluaran")
    with st.form("form_pengeluaran"):
        jumlah = st.number_input("Jumlah Pengeluaran (Rp):", min_value=0, step=1000)
        tujuan = st.text_input("Tujuan Pengeluaran:")
        petugas = st.text_input("Nama Petugas:")
        submitted = st.form_submit_button("Ajukan Pengeluaran")
        if submitted:
            if dana_sosial.tambah_pengeluaran(jumlah, tujuan, petugas):
                st.success("Pengeluaran berhasil diajukan!")
            else:
                st.error("Harap isi semua kolom dengan benar.")

# **Fungsi untuk Persetujuan Pengeluaran**
def persetujuan_pengeluaran():
    st.header("Persetujuan Pengeluaran")

    # Filter pengeluaran yang menunggu persetujuan
    pending_pengeluaran = dana_sosial.pengeluaran[dana_sosial.pengeluaran["Status"] == "Menunggu Persetujuan"]

    if pending_pengeluaran.empty:
        st.info("Tidak ada pengeluaran yang menunggu persetujuan.")
    else:
        st.write("### Daftar Pengeluaran Menunggu Persetujuan")
        st.table(pending_pengeluaran)


        # Pilih pengeluaran untuk diproses
        selected_index = st.selectbox(
            "Pilih pengeluaran berdasarkan nomor urut (index):",
            pending_pengeluaran.index.tolist()
        )

        if st.button("Setujui"):
            if dana_sosial.setujui_pengeluaran(selected_index):
                st.success("Pengeluaran berhasil disetujui!")
            else:
                st.error("Gagal menyetujui pengeluaran. Saldo tidak mencukupi!")
        if st.button("Tolak"):
            if dana_sosial.tolak_pengeluaran(selected_index):
                st.success("Pengeluaran berhasil ditolak!")
            else:
                st.error("Gagal menolak pengeluaran.")

    # Tampilkan pengeluaran yang sudah diproses
    st.write("### Daftar Semua Pengeluaran")
    st.table(dana_sosial.pengeluaran)


# **Menu Aplikasi dengan Persetujuan Pengeluaran**
st.sidebar.title("Aplikasi Pengelolaan Dana Sosial")
menu = st.sidebar.radio("Pilih Menu", [
    "Dashboard", 
    "Pencatatan Pemasukan", 
    "Pencatatan Pengeluaran", 
    "Persetujuan Pengeluaran"
])

# Tambahkan logika pemanggilan fungsi berdasarkan pilihan menu
if menu == "Dashboard":
    tampilkan_dashboard()
elif menu == "Pencatatan Pemasukan":
    pencatatan_pemasukan()
elif menu == "Pencatatan Pengeluaran":
    pencatatan_pengeluaran()
elif menu == "Persetujuan Pengeluaran":
    persetujuan_pengeluaran()
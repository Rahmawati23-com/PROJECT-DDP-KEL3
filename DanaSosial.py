import streamlit as st
import pandas as pd
from datetime import datetime
import os

class DanaSosial:
    def __init__(self):
        self.pemasukan_file = "pemasukan.csv"
        self.pengeluaran_file = "pengeluaran.csv"
        self.saldo = 0
        self._load_data()

    def _load_data(self):
        if os.path.exists(self.pemasukan_file):
            self.pemasukan = pd.read_csv(self.pemasukan_file)
        else:
            self.pemasukan = pd.DataFrame(columns=["Tanggal", "Sumber", "Jumlah", "Petugas"])

        if os.path.exists(self.pengeluaran_file):
            self.pengeluaran = pd.read_csv(self.pengeluaran_file)
        else:
            self.pengeluaran = pd.DataFrame(columns=["Tanggal", "Tujuan", "Jumlah", "Petugas", "Status"])

        total_pemasukan = self.pemasukan["Jumlah"].sum() if not self.pemasukan.empty else 0
        total_pengeluaran = self.pengeluaran.loc[self.pengeluaran["Status"] == "Disetujui", "Jumlah"].sum() \
            if not self.pengeluaran.empty else 0
        self.saldo = total_pemasukan - total_pengeluaran

    def _save_data(self):
        self.pemasukan.to_csv(self.pemasukan_file, index=False)
        self.pengeluaran.to_csv(self.pengeluaran_file, index=False)

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

    def setujui_pengeluaran(self, index):
        if 0 <= index < len(self.pengeluaran):
            pengeluaran_row = self.pengeluaran.iloc[index]
            if pengeluaran_row["Jumlah"] <= self.saldo:
                self.pengeluaran.loc[index, "Status"] = "Disetujui"
                self._save_data()
                self._load_data()
                return True
            else:
                return False
        return False

    def tolak_pengeluaran(self, index):
        if 0 <= index < len(self.pengeluaran):
            self.pengeluaran.loc[index, "Status"] = "Ditolak"
            self._save_data()
            self._load_data()
            return True
        return False

    def download_laporan(self):
        laporan_file = "laporan_keuangan.xlsx"
        with pd.ExcelWriter(laporan_file, engine='xlsxwriter') as writer:
            self.pemasukan.to_excel(writer, sheet_name="Pemasukan", index=False)
            self.pengeluaran.to_excel(writer, sheet_name="Pengeluaran", index=False)
        return laporan_file

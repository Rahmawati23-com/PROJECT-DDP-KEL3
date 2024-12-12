def tampilkan_dashboard(dana_sosial):
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

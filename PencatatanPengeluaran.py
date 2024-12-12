def pencatatan_pengeluaran(dana_sosial):
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

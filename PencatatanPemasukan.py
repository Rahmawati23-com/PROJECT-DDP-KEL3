def pencatatan_pemasukan(dana_sosial):
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

import streamlit as st

def persetujuan_pengeluaran(dana_sosial):
    st.header("Persetujuan Pengeluaran")
    pending_pengeluaran = dana_sosial.pengeluaran[dana_sosial.pengeluaran["Status"] == "Menunggu Persetujuan"]

    if pending_pengeluaran.empty:
        st.info("Tidak ada pengeluaran yang menunggu persetujuan.")
    else:
        st.write("### Daftar Pengeluaran Menunggu Persetujuan")
        st.table(pending_pengeluaran)

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
    st.write("### Daftar Semua Pengeluaran")
    st.table(dana_sosial.pengeluaran)

import streamlit as st

def tentang_kami():
    st.header("Tentang Kami")
    st.subheader("Aplikasi Penggalangan Dana Sosial Masjid")
    st.write("""
    Aplikasi **Penggalangan Dana Sosial Masjid** bertujuan untuk mempermudah masyarakat dalam berdonasi untuk kegiatan sosial 
    dan pembangunan masjid. Aplikasi ini dirancang untuk transparansi dan kemudahan akses bagi semua pengguna.
    
    **Fitur Utama:**
    - **Real-Time Dashboard::** Informasi saldo, pemasukan, dan pengeluaran dalam satu layar.
    - **Validasi Data:** Input pemasukan dan pengeluaran terjamin akurat.
    - **Status Pengeluaran:** Menampilkan pengeluaran berdasarkan status (Menunggu Persetujuan, Disetujui, Ditolak).
    - **Unduh Laporan Keuangan:** Laporan dalam format Excel yang rapi dan siap dibagikan.
    """)

    st.subheader("Visi dan Misi")
    st.write("""
    **Visi**: 
   Menjadi platform digital terpercaya dalam pengelolaan dana sosial masjid yang transparan, efisien, dan profesional untuk mendukung pemberdayaan umat serta meningkatkan kesejahteraan masyarakat.

    **Misi**:
    1. Menyediakan fitur pencatatan pemasukan dan pengeluaran yang transparan agar seluruh donatur dan pengurus masjid dapat memantau penggunaan dana secara akurat.
    2. Mempermudah proses pengelolaan keuangan masjid dengan dashboard yang informatif dan fitur persetujuan pengeluaran berbasis digital.
    3. Membangun kepercayaan antara pengurus masjid dan masyarakat melalui laporan keuangan yang sistematis dan real-time.
    4. Mendukung kegiatan sosial dan pembangunan masjid melalui sistem penggalangan dana yang mudah diakses oleh semua kalangan.
    5. Menyediakan aplikasi yang user-friendly sehingga dapat digunakan oleh pengurus masjid tanpa memerlukan keahlian teknis yang tinggi.
    """)

    st.subheader("Tim Kami")
    # Tim pengembang dengan foto dan informasi anggota
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("images/rahma.png", caption="Rahmawati Ibrahim", width=150)
        st.write("Ketua Kelompok - 0110124136")
    with col2:
        st.image("images/thia.png", caption="Muthia Fadly", width=150)
        st.write("Anggota - 0110124095")
    with col3:
        st.image("images/fauzil.png", caption="Ahmad Fauzil", width=150)
        st.write("Anggota - 0110124169")
    with col4:
        st.image("images/arya.png", caption="Arya Pamungkas", width=150)
        st.write("Anggota - 0110124163")

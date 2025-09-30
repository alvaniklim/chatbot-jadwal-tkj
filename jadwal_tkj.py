# Chatbot Jadwal Pelajaran TKJ (Streamlit Version)
# By: Fahruddin Arrasyid Alfansuri - Guru TKJ

import streamlit as st

# Dataset contoh (silakan ganti sesuai jadwal nyata)
jadwal = {
    "X TKJ 1": {
        "Senin": ["Matematika", "Bahasa Indonesia", "Produktif TKJ"],
        "Selasa": ["Pendidikan Agama", "Bahasa Inggris", "Olahraga"],
        "Rabu": ["Produktif TKJ", "Informatika", "Sejarah"],
        "Kamis": ["Fisika", "Kimia", "Produktif TKJ"],
        "Sabtu": ["Seni Budaya", "PPKN", "Kewirausahaan"],
    },
    "XI TKJ 1": {
        "Senin": ["Produktif TKJ", "Jaringan Dasar", "Basis Data"],
        "Selasa": ["Bahasa Indonesia", "Matematika", "Olahraga"],
        "Rabu": ["Bahasa Inggris", "PPKN", "Produktif TKJ"],
        "Kamis": ["Pemrograman Web", "Sistem Operasi", "Produktif TKJ"],
        "Sabtu": ["Agama", "Produktif TKJ", "Kewirausahaan"],
    },
    "XII TKJ 1": {
        "Senin": ["Produktif TKJ", "Proyek Akhir", "Bahasa Indonesia"],
        "Selasa": ["Agama", "Matematika", "Bahasa Inggris"],
        "Rabu": ["Proyek Akhir", "Basis Data", "PPKN"],
        "Kamis": ["Produktif TKJ", "Sistem Operasi", "Kewirausahaan"],
        "Sabtu": ["Seni Budaya", "Produktif TKJ", "Sejarah"],
    }
    # Lanjutkan untuk X TKJ 2, X TKJ 3, XI TKJ 2, XI TKJ 3, XII TKJ 2, XII TKJ 3
}

# ---------------- STREAMLIT APP ----------------
st.title("📚 Chatbot Jadwal Pelajaran TKJ")
st.write("Pilih kelas dan hari untuk melihat jadwal pelajaran.")

kelas = st.selectbox("Pilih Kelas:", list(jadwal.keys()))
hari = st.selectbox("Pilih Hari:", ["Senin", "Selasa", "Rabu", "Kamis", "Sabtu"])

if hari in ["Jumat", "Minggu"]:
    st.warning(f"📌 Hari {hari} adalah LIBUR.")
elif hari in jadwal[kelas]:
    st.success(f"👉 Jadwal {kelas} hari {hari}:")
    st.write(", ".join(jadwal[kelas][hari]))
else:
    st.error(f"❌ Jadwal {kelas} hari {hari} belum tersedia.")

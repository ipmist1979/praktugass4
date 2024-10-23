import streamlit as st
import pandas as pd

# Fungsi untuk menampilkan grafik berdasarkan pilihan
def tampilkan_grafik(df, kolom, jenis_grafik):
    if jenis_grafik == "Bar":
        st.bar_chart(df[kolom])
    elif jenis_grafik == "Line":
        st.line_chart(df[kolom])
    elif jenis_grafik == "Area":
        st.area_chart(df[kolom])
    else:
        st.write("Pilih jenis grafik yang valid")

# Judul Aplikasi
st.title("Visualisasi DataFrame dengan Streamlit")

# Input untuk mengunggah dataset
uploaded_file = st.file_uploader("Unggah file dataset (CSV)", type=["csv"])

if uploaded_file is not None:
    # Membaca dataset CSV
    df = pd.read_csv(uploaded_file)
    
    # Menampilkan preview dataset
    st.write("Dataset yang diunggah:")
    st.write(df)

    # Input untuk memilih kolom yang akan divisualisasikan
    kolom_dipilih = st.multiselect("Pilih kolom untuk ditampilkan", options=df.columns)

    # Input untuk memilih jenis grafik
    jenis_grafik = st.selectbox("Pilih jenis grafik", ["Bar", "Line", "Area"])

    # Menampilkan grafik untuk setiap kolom yang dipilih
    if kolom_dipilih:
        for kolom in kolom_dipilih:
            st.write(f"Visualisasi untuk kolom: {kolom}")
            tampilkan_grafik(df, kolom, jenis_grafik)
    else:
        st.write("Silakan pilih setidaknya satu kolom untuk ditampilkan.")
else:
    st.write("Silakan unggah file dataset.")

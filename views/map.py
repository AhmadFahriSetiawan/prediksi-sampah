import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium


def show_map():

    st.title("🗺️ Peta Prediksi Sampah")

    df = pd.read_csv("data/data_prediksi.csv")

    tahun = st.selectbox(
        "Pilih Tahun",
        sorted(df["Tahun"].unique())
    )

    df_filter = df[df["Tahun"] == tahun].copy()
    df_filter = df_filter.dropna(subset=["latitude", "longitude"])

    if df_filter.empty:
        st.warning("Tidak ada data koordinat untuk tahun ini.")
        return

    m = folium.Map(
        location=[-6.6, 106.8],
        zoom_start=10
    )

    def warna_marker(kategori):
        if kategori == "Rendah":
            return "green"
        elif kategori == "Sedang":
            return "orange"
        elif kategori == "Tinggi":
            return "red"
        else:  # Sangat Tinggi
            return "darkred"

    for _, row in df_filter.iterrows():

        popup_text = f"""
        <b>Wilayah:</b> {row['Wilayah']}<br>
        <b>Kecamatan:</b> {row['Kecamatan']}<br>
        <b>Tahun:</b> {row['Tahun']}<br>
        <b>Prediksi Penduduk:</b> {row['Prediksi_Penduduk']:,.0f}<br>
        <b>Prediksi Sampah:</b> {row['Prediksi_Timbulan_Sampah']:,.1f} m³/hari<br>
        <b>Kategori:</b> {row['Kategori']}
        """

        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=popup_text,
            icon=folium.Icon(
                color=warna_marker(row["Kategori"])
            )
        ).add_to(m)

    st_folium(m, width=1200, height=600)
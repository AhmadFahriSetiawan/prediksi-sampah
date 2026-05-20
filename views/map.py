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

    kapasitas_tpa = 5000

    df_filter["Persentase"] = (
        df_filter["Prediksi_Timbulan_Sampah"] / kapasitas_tpa
    ) * 100

    def status_kondisi(x):
        if x < 70:
            return "Aman"
        elif x <= 100:
            return "Rawan"
        else:
            return "Overload"

    df_filter["Status"] = df_filter["Persentase"].apply(status_kondisi)

    # PERBAIKI FORMAT KOORDINAT
    df_filter["latitude"] = (
        df_filter["latitude"]
        .astype(str)
        .str.replace(".", "", regex=False)
        .str.replace(r"^(-?\d)", r"\1.", regex=True)
    )

    df_filter["longitude"] = (
        df_filter["longitude"]
        .astype(str)
        .str.replace(".", "", regex=False)
        .str.replace(r"^(-?\d{3})", r"\1.", regex=True)
    )

    # UBAH KE FLOAT
    df_filter["latitude"] = pd.to_numeric(
        df_filter["latitude"],
        errors="coerce"
    )

    df_filter["longitude"] = pd.to_numeric(
        df_filter["longitude"],
        errors="coerce"
    )

    # HAPUS DATA KOSONG
    df_filter = df_filter.dropna(
        subset=["latitude", "longitude"]
    )

    # MAP
    m = folium.Map(
        location=[-6.6, 106.8],
        zoom_start=10
    )

    # WARNA MARKER
    def warna_marker(status):
        if "Aman" in status:
            return "green"
        elif "Rawan" in status:
            return "orange"
        else:
            return "red"

    # LOOP MARKER
    for _, row in df_filter.iterrows():

        popup_text = f"""
        <b>Wilayah:</b> {row['Wilayah']}<br>
        <b>Tahun:</b> {row['Tahun']}<br>
        <b>Prediksi Penduduk:</b> {row['Prediksi_Penduduk']}<br>
        <b>Prediksi Sampah:</b> {row['Prediksi_Timbulan_Sampah']} Ton<br>
        <b>Status:</b> {row['Status']}
        """

        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=popup_text,
            icon=folium.Icon(
                color=warna_marker(row["Status"])
            )
        ).add_to(m)

    # TAMPILKAN MAP
    st_folium(m, width=1200, height=600)
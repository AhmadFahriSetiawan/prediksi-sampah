import streamlit as st
import pandas as pd


def show_dashboard():

    st.title("📊 Dashboard Prediksi Sampah")

    df = pd.read_csv("data/data_prediksi.csv")

    tahun = st.selectbox(
        "Pilih Tahun",
        sorted(df["Tahun"].unique())
    )

    df_filter = df[df["Tahun"] == tahun].copy()

        # KATEGORI BERDASARKAN BATAS KUARTIL LAPORAN
    q1 = 4658.39
    q3 = 8607.91

    def kategori(x):
        if x < q1:
            return "Rendah"
        elif x <= q3:
            return "Sedang"
        else:
            return "Tinggi"

    df_filter["Kategori"] = (
        df_filter["Prediksi_Timbulan_Sampah"]
        .apply(kategori)
    )

    # KPI
    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Wilayah",
        df_filter["Wilayah"].nunique()
    )

    col2.metric(
        "Total Timbulan Sampah",
        f"{df_filter['Prediksi_Timbulan_Sampah'].sum():,.0f} Ton"
    )

    col3.metric(
        "Total Penduduk",
        f"{df_filter['Prediksi_Penduduk'].sum():,.0f}"
    )

    st.divider()

    # WARNA KATEGORI
    def warna_kategori(val):

        if val == "Rendah":
            return "color: #16a34a; font-weight: bold"

        elif val == "Sedang":
            return "color: #f59e0b; font-weight: bold"

        elif val == "Tinggi":
            return "color: #dc2626; font-weight: bold"

        return ""

    st.subheader("📋 Data Prediksi")

    kolom_tampil = [
        "Wilayah",
        "Tahun",
        "Prediksi_Penduduk",
        "Prediksi_Timbulan_Sampah",
        "Kategori"
    ]


    st.dataframe(
        df_filter[kolom_tampil].style.map(
            warna_kategori,
            subset=["Kategori"]
        ),
        use_container_width=True
    )

    
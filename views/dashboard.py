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

    kapasitas_tpa = 5000

    # HITUNG PERSENTASE
    df_filter["Persentase"] = (
        df_filter["Prediksi_Timbulan_Sampah"] / kapasitas_tpa
    ) * 100

    # STATUS
    def status_kondisi(x):

        if x < 70:
            return "Aman"

        elif x <= 100:
            return "Rawan"

        else:
            return "Overload"

    df_filter["Status"] = df_filter["Persentase"].apply(status_kondisi)

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

    # WARNA STATUS
    def warna_status(val):

        if val == "Aman":
            return "color: #16a34a; font-weight: bold"

        elif val == "Rawan":
            return "color: #f59e0b; font-weight: bold"

        elif val == "Overload":
            return "color: #dc2626; font-weight: bold"

        return ""

    st.subheader("📋 Data Prediksi")

    st.dataframe(
        df_filter.style.map(
            warna_status,
            subset=["Status"]
        ),
         use_container_width=True
)
import streamlit as st
import pandas as pd
import plotly.express as px


def show_analytics():

    st.title("📈 Analytics Timbulan Sampah")

    df = pd.read_csv("data/data_prediksi.csv")

    tahun = st.selectbox(
        "Pilih Tahun",
        sorted(df["Tahun"].unique())
    )

    df_filter = df[df["Tahun"] == tahun].copy()

    # WARNA KATEGORI (KONSISTEN DENGAN HALAMAN LAIN)
    warna_map = {
        "Rendah": "#16a34a",
        "Sedang": "#f59e0b",
        "Tinggi": "#ea580c",
        "Sangat Tinggi": "#dc2626"
    }

    # =========================
    # TOP 10 WILAYAH
    # =========================

    st.subheader("📊 Top 10 Timbulan Sampah")

    top10 = df_filter.sort_values(
        by="Prediksi_Timbulan_Sampah",
        ascending=False
    ).head(10)

    fig = px.bar(
        top10,
        x="Wilayah",
        y="Prediksi_Timbulan_Sampah",
        color="Kategori",
        color_discrete_map=warna_map,
        title="10 Wilayah Timbulan Sampah Tertinggi (m³/hari)",
        labels={"Prediksi_Timbulan_Sampah": "Timbulan Sampah (m³/hari)"}
    )

    st.plotly_chart(fig, use_container_width=True)

    # =========================
    # DISTRIBUSI KATEGORI
    # =========================

    st.subheader("📊 Distribusi Kategori Wilayah")

    kategori_count = (
        df_filter["Kategori"]
        .value_counts()
    )

    fig2 = px.pie(
        values=kategori_count.values,
        names=kategori_count.index,
        color=kategori_count.index,
        color_discrete_map=warna_map,
        title="Distribusi Kategori Wilayah"
    )

    st.plotly_chart(fig2, use_container_width=True)
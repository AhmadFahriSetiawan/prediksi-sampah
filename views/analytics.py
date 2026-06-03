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
        title="10 Wilayah Timbulan Sampah Tertinggi"
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
        title="Distribusi Kategori Wilayah"
    )

    st.plotly_chart(fig2, use_container_width=True)
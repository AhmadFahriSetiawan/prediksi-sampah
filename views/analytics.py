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

    df_filter = df[df["Tahun"] == tahun]

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

    st.subheader("📊 Top 10 Timbulan Sampah")

    top10 = df_filter.sort_values(
        by="Prediksi_Timbulan_Sampah",
        ascending=False
    ).head(10)

    fig = px.bar(
        top10,
        x="Wilayah",
        y="Prediksi_Timbulan_Sampah",
        color="Status",
        title="10 Wilayah Timbulan Sampah Tertinggi"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📊 Distribusi Status")

    status_count = df_filter["Status"].value_counts()

    fig2 = px.pie(
        values=status_count.values,
        names=status_count.index,
        title="Distribusi Status Wilayah"
    )

    st.plotly_chart(fig2, use_container_width=True)
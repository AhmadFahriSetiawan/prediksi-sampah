import streamlit as st
from streamlit_option_menu import option_menu

from views.dashboard import show_dashboard
from views.analytics import show_analytics
from views.map import show_map


# CONFIG
st.set_page_config(
    page_title="Prediksi Sampah Kabupaten Bogor",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# LOAD CSS
with open("assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )


# =========================
# NAVBAR
# =========================

col1, col2 = st.columns([1, 8])

with col1:
    st.image("assets/logo.png", width=80)

with col2:
    st.title("Prediksi Timbulan Sampah Kabupaten Bogor")

st.markdown("<hr>", unsafe_allow_html=True)


# =========================
# SIDEBAR
# =========================

with st.sidebar:



    selected = option_menu(
        menu_title=None,

        options=[
            "Dashboard",
            "Analytics",
            "Map"
        ],

        icons=[
            "speedometer2",
            "bar-chart-line",
            "geo-alt-fill"
        ],

        default_index=0,

        styles={

            "container": {
                "padding": "10px",
                "background-color": "transparent",
                "border-radius": "15px",
            },

            "icon": {
                "color": "#38BDF8",
                "font-size": "18px",
            },

            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "8px 0px",
                "padding": "14px",
                "border-radius": "12px",
                "color": "var(--text-color)",
                "--hover-color": "#1E293B",
            },

            "nav-link-selected": {
                "background-color": "#2563EB",
                "color": "white",
                "font-weight": "bold",
            },
        }
    )

    st.markdown("---")

    # STATUS BOX
        # KATEGORI BOX
    st.markdown(
        """
        <div class="status-box aman">
            🟢 Rendah
        </div>

        <div class="status-box rawan">
            🟠 Sedang
        </div>

        <div class="status-box overload">
            🔴 Tinggi
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.caption("Sistem Prediksi Timbulan Sampah")
    st.caption("Kabupaten Bogor")


# =========================
# ROUTING
# =========================

if selected == "Dashboard":
    show_dashboard()

elif selected == "Analytics":
    show_analytics()

elif selected == "Map":
    show_map()
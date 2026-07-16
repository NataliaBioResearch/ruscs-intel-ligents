import streamlit as st

from ns_dashboard.dashboard_acoustic import acoustic_dashboard
from ns_dashboard.dashboard_ml import ml_dashboard
from ns_dashboard.dashboard_meteo import meteo_dashboard
from ns_dashboard.dashboard_sensors import sensors_dashboard

st.set_page_config(page_title="Rusc Dashboard", layout="wide")

st.title("🐝 Dashboard del Sistema del Rusc")

tab1, tab2, tab3, tab4 = st.tabs([
    "🔊 Acústica (CRNN)",
    "📊 Model ML (XGBoost)",
    "🌦️ Meteorologia",
    "📡 Sensors del Rusc"
])

with tab1:
    acoustic_dashboard()

with tab2:
    ml_dashboard()

with tab3:
    meteo_dashboard()

with tab4:
    sensors_dashboard()

elif menu == "Model ML (XGBoost)":
    ml_dashboard()

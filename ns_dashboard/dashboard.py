import streamlit as st
from ns_dashboard.dashboard_acoustic import acoustic_dashboard
from ns_dashboard.dashboard_ml import ml_dashboard

st.set_page_config(page_title="Rusc Dashboard", layout="wide")

st.title("🐝 Dashboard del Sistema del Rusc")

menu = st.sidebar.selectbox(
    "Selecciona un mòdul",
    ["Acústica (CRNN)", "Model ML (XGBoost)"]
)

if menu == "Acústica (CRNN)":
    acoustic_dashboard()

elif menu == "Model ML (XGBoost)":
    ml_dashboard()

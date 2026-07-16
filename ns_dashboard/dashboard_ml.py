import streamlit as st
import pandas as pd
import xgboost as xgb
import seaborn as sns
import matplotlib.pyplot as plt

from ns_dashboard.plots_ml import plot_xgb_feature_importance

st.title("Dashboard ML — Model d'Enjambrament XGBoost")

# Carregar CSV
csv_file = st.file_uploader("Carrega un dataset tabular (.csv)", type=["csv"])

if csv_file is not None:
    df = pd.read_csv(csv_file)
    st.subheader("Dataset carregat")
    st.dataframe(df)

    # Carregar model XGB
    model_path = st.text_input("Ruta del model XGBoost", "models/swarm_xgb.json")

    if st.button("Carregar model"):
        booster = xgb.Booster()
        booster.load_model(model_path)
        st.success("Model carregat correctament.")

        st.subheader("Importància de features")
        plot_xgb_feature_importance(model_path)

        # Prediccions
        st.subheader("Prediccions del model")
        feature_cols = ["weight", "weight_trend", "sound_trend",
                        "acoustic_swarm_prob", "temp_in", "temp_out",
                        "humidity", "correlation_score"]

        if all(col in df.columns for col in feature_cols):
            dmatrix = xgb.DMatrix(df[feature_cols])
            preds = booster.predict(dmatrix)
            df["swarm_probability"] = preds
            st.dataframe(df[["swarm_probability"]])
        else:
            st.warning("El dataset no conté totes les features necessàries.")

        # Correlacions
        st.subheader("Mapa de correlacions")
        plt.figure(figsize=(10, 6))
        sns.heatmap(df.corr(), annot=True, cmap="viridis")
        st.pyplot(plt)


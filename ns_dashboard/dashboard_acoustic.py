import streamlit as st
import numpy as np

from ns_acoustic.crnn_inference import crnn_predict
from ns_acoustic.features import compute_mel_spectrogram
from ns_dashboard.plots_ml import plot_probability_distribution

def load_pcm(path):
    """
    Carrega un fitxer PCM guardat com .npy
    """
    return np.load(path).astype("float32")

st.title("Dashboard Acústic — CRNN")

# Selecció de fitxer PCM
pcm_file = st.file_uploader("Carrega un fitxer PCM (.npy)", type=["npy"])

if pcm_file is not None:
    pcm = np.load(pcm_file).astype("float32")

    st.subheader("Espectrograma Mel")
    mel = compute_mel_spectrogram(pcm, sr=16000)

    st.image(mel, caption="Mel Spectrogram", use_column_width=True)

    st.subheader("Inferència CRNN")
    preds = crnn_predict(pcm)

    st.write("Probabilitats per classe:")
    st.json(preds)

    st.subheader("Distribució de probabilitats")
    plot_probability_distribution(preds)

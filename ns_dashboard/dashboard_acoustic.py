import streamlit as st
import numpy as np

from ns_acoustic.crnn_inference import crnn_predict
from ns_acoustic.features import compute_mel_spectrogram
from ns_dashboard.plots_ml import plot_probability_distribution
from ns_dashboard.plots_acoustic import plot_mel_spectrogram

def acoustic_dashboard():
    st.header("🔊 Mòdul Acústic — CRNN")

    pcm_file = st.file_uploader("Carrega un fitxer PCM (.npy)", type=["npy"])

    if pcm_file is not None:
        pcm = np.load(pcm_file).astype("float32")

        # Espectrograma Mel
        mel = compute_mel_spectrogram(pcm, sr=16000)
        st.subheader("Espectrograma Mel")
        plot_mel_spectrogram(mel)

        # Inferència CRNN
        preds = crnn_predict(pcm)
        st.subheader("Probabilitats CRNN")
        st.json(preds)

        # Distribució de probabilitats
        st.subheader("Distribució de probabilitats")
        plot_probability_distribution(preds)


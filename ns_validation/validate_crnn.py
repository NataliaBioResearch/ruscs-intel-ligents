import numpy as np
from ns_acoustic.crnn_inference import crnn_predict
from ns_dashboard.plots_ml import plot_probability_distribution

def load_pcm(path):
    """
    Carrega un fitxer PCM guardat com .npy
    """
    return np.load(path).astype("float32")

def main():
    # Ruta a un sample real
    pcm_path = "data/audio_processed/pcm/2026-07-15T07-51-00Z.npy"
    pcm = load_pcm(pcm_path)

    # Inferència CRNN
    preds = crnn_predict(pcm)

    # Plot de probabilitats
    plot_probability_distribution(preds)

if __name__ == "__main__":
    main()


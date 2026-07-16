import matplotlib.pyplot as plt
import numpy as np
import librosa
import librosa.display
import seaborn as sns

def plot_mel_spectrogram(mel, sr=16000):
    """
    Mostra un espectrograma Mel.
    Args:
        mel: matriu Mel (n_mels x frames)
        sr: sample rate
    """
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(mel, sr=sr, x_axis="time", y_axis="mel", cmap="inferno")
    plt.colorbar(format="%+2.0f dB")
    plt.title("Espectrograma Mel")
    plt.tight_layout()
    plt.show()


def plot_stft_spectrogram(pcm, sr=16000):
    """
    Mostra un espectrograma STFT.
    """
    D = np.abs(librosa.stft(pcm))
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(librosa.amplitude_to_db(D, ref=np.max),
                             sr=sr, x_axis="time", y_axis="log", cmap="magma")
    plt.colorbar(format="%+2.0f dB")
    plt.title("Espectrograma STFT")
    plt.tight_layout()
    plt.show()


def plot_frequency_power(pcm, sr=16000):
    """
    Mostra la potència per freqüència (FFT).
    """
    fft = np.abs(np.fft.rfft(pcm))
    freqs = np.fft.rfftfreq(len(pcm), 1/sr)

    plt.figure(figsize=(10, 4))
    plt.plot(freqs, fft, color="purple")
    plt.title("Potència per freqüència (FFT)")
    plt.xlabel("Freqüència (Hz)")
    plt.ylabel("Amplitud")
    plt.xlim(0, 1500)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_energy_bands(pcm, sr=16000):
    """
    Mostra bandes energètiques Low/Mid/High.
    """
    fft = np.abs(np.fft.rfft(pcm))
    freqs = np.fft.rfftfreq(len(pcm), 1/sr)

    bands = {
        "Low (50–200 Hz)": fft[(freqs >= 50) & (freqs <= 200)].mean(),
        "Mid (200–600 Hz)": fft[(freqs >= 200) & (freqs <= 600)].mean(),
        "High (600–1200 Hz)": fft[(freqs >= 600) & (freqs <= 1200)].mean(),
    }

    plt.figure(figsize=(6, 4))
    plt.bar(bands.keys(), bands.values(), color=["#4CAF50", "#FFC107", "#F44336"])
    plt.title("Bandes energètiques")
    plt.ylabel("Energia mitjana")
    plt.tight_layout()
    plt.show()


def plot_acoustic_heatmap(matrix):
    """
    Mostra un heatmap acústic temporal.
    Args:
        matrix: matriu 2D (temps x features)
    """
    plt.figure(figsize=(10, 5))
    sns.heatmap(matrix, cmap="magma")
    plt.title("Heatmap acústic temporal")
    plt.tight_layout()
    plt.show()


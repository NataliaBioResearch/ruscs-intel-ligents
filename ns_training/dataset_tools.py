import numpy as np
from ns_acoustic.features import compute_mel_spectrogram
from ns_training.augmentation import augment_audio

def load_training_sample(pcm, sr=16000, augment=True):
    """
    Carrega un sample per entrenament CRNN.
    Aplica augmentació si augment=True.
    Retorna l'espectrograma Mel.
    """
    if augment:
        pcm = augment_audio(pcm, sr)

    mel = compute_mel_spectrogram(pcm, sr)
    mel = mel.astype("float32")
    mel = mel / (mel.max() + 1e-8)
    mel = np.expand_dims(mel, axis=(0, -1))  # (1, H, W, 1)

    return mel

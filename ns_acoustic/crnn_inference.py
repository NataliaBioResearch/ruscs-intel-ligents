import os
import numpy as np
from .crnn_model import load_crnn_model
from .features import compute_mel_spectrogram

# Carreguem el model un cop
MODEL = load_crnn_model()

def load_classes():
    """
    Carrega les classes del model CRNN des de models/classes.txt.
    Retorna:
        list[str]: llista de classes en l'ordre del model.
    """
    classes_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "models",
        "classes.txt"
    )

    if not os.path.exists(classes_path):
        raise FileNotFoundError(f"Fitxer de classes no trobat: {classes_path}")

    with open(classes_path, "r") as f:
        classes = [c.strip() for c in f.readlines()]

    return classes


CLASSES = load_classes()


def crnn_predict(audio_pcm, sr=16000):
    """
    Fa inferència CRNN sobre un senyal PCM.

    Args:
        audio_pcm (np.ndarray): senyal d'àudio en float32.
        sr (int): taxa de mostreig.

    Retorna:
        dict: probabilitats per cada classe.
    """

    # 1. Generar espectrograma
    mel = compute_mel_spectrogram(audio_pcm, sr)

    # 2. Normalitzar i adaptar dimensions
    mel = mel.astype("float32")
    mel = mel / (mel.max() + 1e-8)
    mel = np.expand_dims(mel, axis=(0, -1))  # (1, H, W, 1)

    # 3. Inferència
    preds = MODEL.predict(mel)[0]

    # 4. Mapar probabilitats a classes
    return {cls: float(pred) for cls, pred in zip(CLASSES, preds)}

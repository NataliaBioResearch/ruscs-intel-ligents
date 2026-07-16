import numpy as np
from .crnn_model import load_crnn_model
from .features import compute_mel_spectrogram

# Carreguem el model un cop
MODEL = load_crnn_model()

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

    # 4. Carregar classes
    classes_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "models",
        "classes.txt"
    )
    with open(classes_path, "r") as f:
        classes = [c.strip() for c in f.readlines()]

    return {cls: float(pred) for cls, pred in zip(classes, preds)}

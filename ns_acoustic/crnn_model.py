import os
from tensorflow.keras.models import load_model

MODEL_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "models",
    "crnn_real.h5"
)

def load_crnn_model():
    """
    Carrega el model CRNN real entrenat.
    Retorna:
        model (keras.Model): model carregat llest per inferència.
    """
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model no trobat: {MODEL_PATH}")

    model = load_model(MODEL_PATH)
    return model

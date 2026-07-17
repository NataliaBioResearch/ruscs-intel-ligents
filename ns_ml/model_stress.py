import os
import pickle
import numpy as np

MODEL_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "models",
    "stress_model.pkl"
)

def load_stress_model():
    """
    Carrega el model d'estrès tèrmic entrenat (pickle).
    """
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model no trobat: {MODEL_PATH}")

    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    return model


MODEL = load_stress_model()

def predict_stress(temp_interna, temp_externa, humitat, tend_temp, tend_hum):
    """
    Predicció d'estrès tèrmic basada en telemetria i tendències.

    Retorna:
        float: probabilitat d'estrès tèrmic (0–1)
    """

    features = np.array([
        temp_interna,
        temp_externa,
        humitat,
        tend_temp,
        tend_hum
    ]).reshape(1, -1)

    prob = MODEL.predict_proba(features)[0][1]
    return float(prob)

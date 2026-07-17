import os
import xgboost as xgb
import numpy as np

MODEL_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "models",
    "swarm_xgb.json"
)

def load_swarm_model():
    """
    Carrega el model XGBoost d'enjambrament.
    """
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model no trobat: {MODEL_PATH}")

    booster = xgb.Booster()
    booster.load_model(MODEL_PATH)
    return booster


MODEL = load_swarm_model()

def predict_swarm(features):
    """
    Predicció d'enjambrament basada en features del rusc.

    Args:
        features (dict): Diccionari amb:
            - weight
            - weight_trend
            - sound_trend
            - acoustic_swarm_prob
            - temp_interna
            - temp_externa
            - humidity
            - correlation_score

    Returns:
        float: probabilitat d'enjambrament (0–1)
    """

    x = np.array([
        features["weight"],
        features["weight_trend"],
        features["sound_trend"],
        features["acoustic_swarm_prob"],
        features["temp_interna"],
        features["temp_externa"],
        features["humidity"],
        features["correlation_score"]
    ]).reshape(1, -1)

    dmatrix = xgb.DMatrix(x)
    prob = MODEL.predict(dmatrix)[0]
    return float(prob)

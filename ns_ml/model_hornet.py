import xgboost as xgb
import numpy as np

class HornetModel:
    """
    Model ML del rusc (Hornet).
    Carrega el model XGBoost i fa prediccions sobre features del rusc.
    """

    def __init__(self, model_path):
        self.model = xgb.Booster()
        self.model.load_model(model_path)

    def predict(self, features):
        """
        Rep un diccionari de features i retorna prediccions estructurades.

        Args:
            features (dict): Features del rusc (acústica, sensors, meteo).

        Returns:
            dict: Probabilitats de cada classe.
        """

        # Convertir a vector ordenat
        ordered = np.array([
            features["heat_index"],
            features["comfort_index"],
            features["wind_risk_score"],
            features["rain_risk_score"],
            features["acoustic_activity"],
            features["sensor_activity"],
            features["temp_ext"],
            features["humidity"]
        ]).reshape(1, -1)

        dmatrix = xgb.DMatrix(ordered)
        preds = self.model.predict(dmatrix)[0]

        return {
            "prob_swarm": float(preds[0]),
            "prob_stress": float(preds[1]),
            "prob_low_activity": float(preds[2]),
            "prob_noise_anomaly": float(preds[3])
        }

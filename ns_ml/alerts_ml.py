def ml_alerts(pred):
    """
    Genera alertes basades en prediccions ML (XGBoost o CRNN).

    Args:
        pred (dict): Diccionari amb resultats ML:
            - prob_swarm
            - prob_stress
            - prob_low_activity
            - prob_noise_anomaly

    Returns:
        list: Llista d'alertes detectades.
    """

    alerts = []

    # Enjambrazó (swarm)
    if pred["prob_swarm"] > 0.75:
        alerts.append({
            "type": "swarm_risk",
            "severity": "high",
            "message": "Alta probabilitat d'enjambrazó segons model ML."
        })

    # Estrès tèrmic o ambiental
    if pred["prob_stress"] > 0.70:
        alerts.append({
            "type": "stress_risk",
            "severity": "medium",
            "message": "Probable estrès ambiental detectat pel model ML."
        })

    # Activitat baixa
    if pred["prob_low_activity"] > 0.65:
        alerts.append({
            "type": "low_activity",
            "severity": "medium",
            "message": "Activitat baixa detectada pel model ML."
        })

    # Anomalies acústiques
    if pred["prob_noise_anomaly"] > 0.80:
        alerts.append({
            "type": "acoustic_anomaly",
            "severity": "high",
            "message": "Anomalia acústica detectada pel model CRNN."
        })

    return alerts

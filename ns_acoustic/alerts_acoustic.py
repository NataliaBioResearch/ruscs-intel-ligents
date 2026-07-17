def acoustic_alerts(ac):
    """
    Genera alertes acústiques basades en deteccions del pipeline acústic.

    Args:
        ac (dict): Diccionari amb resultats acústics:
            - event_calls
            - event_clicks
            - event_whistles
            - anomaly_score
            - crnn_prob_swarm
            - crnn_prob_distress
            - rms
            - spectral_flux

    Returns:
        list: Llista d'alertes detectades.
    """

    alerts = []

    # Esdeveniments acústics
    if ac["event_calls"] > 10:
        alerts.append({
            "type": "acoustic_calls",
            "severity": "medium",
            "message": "Increment de 'calls' detectat — possible agitació."
        })

    if ac["event_clicks"] > 15:
        alerts.append({
            "type": "acoustic_clicks",
            "severity": "medium",
            "message": "Patró de 'clicks' elevat — possible comunicació d'alerta."
        })

    if ac["event_whistles"] > 3:
        alerts.append({
            "type": "acoustic_whistles",
            "severity": "high",
            "message": "Xiulets detectats — patró acústic associat a pre-enjambrazó."
        })

    # Model CRNN
    if ac["crnn_prob_swarm"] > 0.75:
        alerts.append({
            "type": "crnn_swarm",
            "severity": "high",
            "message": "Alta probabilitat d'enjambrazó segons model CRNN."
        })

    if ac["crnn_prob_distress"] > 0.70:
        alerts.append({
            "type": "crnn_distress",
            "severity": "medium",
            "message": "Probable estrès acústic detectat pel model CRNN."
        })

    # Anomalies acústiques
    if ac["anomaly_score"] > 0.8:
        alerts.append({
            "type": "acoustic_anomaly",
            "severity": "high",
            "message": "Anomalia acústica detectada — patró no habitual."
        })

    # Soroll RMS
    if ac["rms"] > 0.6:
        alerts.append({
            "type": "high_noise",
            "severity": "medium",
            "message": "Nivell de soroll elevat — possible agitació interna."
        })

    # Flux espectral
    if ac["spectral_flux"] > 0.5:
        alerts.append({
            "type": "spectral_change",
            "severity": "medium",
            "message": "Canvi espectral sobtat — activitat acústica irregular."
        })

    return alerts

def meteo_alerts(m):
    """
    Genera alertes meteorològiques basades en valors de temperatura, humitat, vent i pluja.

    Args:
        m (dict): Diccionari amb dades meteorològiques:
            - temp_ext
            - humidity
            - wind
            - rain

    Returns:
        list: Llista d'alertes detectades.
    """

    alerts = []

    # Temperatura
    if m["temp_ext"] > 35:
        alerts.append({
            "type": "heat",
            "severity": "high",
            "message": "Calor extrema — risc d'estrès tèrmic i pre-enxam."
        })

    if m["temp_ext"] < 5:
        alerts.append({
            "type": "cold",
            "severity": "medium",
            "message": "Fred intens — risc d'inactivitat i consum elevat."
        })

    # Humitat
    if m["humidity"] > 90:
        alerts.append({
            "type": "humidity_high",
            "severity": "medium",
            "message": "Humitat molt alta — risc de fongs."
        })

    if m["humidity"] < 20:
        alerts.append({
            "type": "humidity_low",
            "severity": "medium",
            "message": "Humitat molt baixa — risc de deshidratació."
        })

    # Vent
    if m["wind"] > 40:
        alerts.append({
            "type": "wind",
            "severity": "high",
            "message": "Vent fort — risc de danys estructurals i agitació."
        })

    # Pluja
    if m["rain"] > 5:
        alerts.append({
            "type": "rain",
            "severity": "medium",
            "message": "Pluja intensa — reducció d'activitat i humitat interna."
        })

    return alerts


import numpy as np

def compute_slope(values):
    """
    Calcula la tendència (slope) d'una sèrie temporal curta.
    """
    if len(values) < 2:
        return 0.0
    x = np.arange(len(values))
    slope = np.polyfit(x, values, 1)[0]
    return float(slope)


def compute_general_features(sensor, acoustic, meteo):
    """
    Genera features generals del rusc combinant sensors, acústica i meteo.

    Args:
        sensor (dict): Dades del rusc (pes, temp_interna, humitat, etc.)
        acoustic (dict): Dades acústiques processades
        meteo (dict): Dades meteorològiques externes

    Returns:
        dict: Features generals per models ML
    """

    weight = sensor["weight"]
    weight_trend = compute_slope(sensor["weight_history"])
    sound_trend = compute_slope(acoustic["rms_history"])

    return {
        # Sensors
        "weight": weight,
        "weight_trend": weight_trend,
        "temp_interna": sensor["temp_interna"],
        "humidity": sensor["humidity"],

        # Acústica
        "acoustic_activity": acoustic["rms"],
        "sound_trend": sound_trend,
        "acoustic_swarm_prob": acoustic["crnn_prob_swarm"],

        # Meteo
        "temp_externa": meteo["temp_ext"],
        "comfort_index": meteo["comfort_index"],
        "heat_index": meteo["heat_index"],

        # Features compostes
        "correlation_score": sensor["corr_score"],
        "stress_indicator": sensor["temp_interna"] - meteo["temp_ext"]
    }


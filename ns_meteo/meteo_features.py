import numpy as np

def compute_heat_index(temp, humidity):
    """
    Índex de calor segons fórmula NOAA.
    """
    return (
        -8.78469475556 +
        1.61139411 * temp +
        2.33854883889 * humidity +
        -0.14611605 * temp * humidity +
        -0.012308094 * temp**2 +
        -0.0164248277778 * humidity**2 +
        0.002211732 * temp**2 * humidity +
        0.00072546 * temp * humidity**2 +
        -0.000003582 * temp**2 * humidity**2
    )


def compute_wind_risk(wind):
    """
    Risc de vent segons llindars.
    """
    if wind > 60:
        return "extreme"
    elif wind > 40:
        return "high"
    elif wind > 25:
        return "medium"
    return "low"


def compute_rain_risk(rain):
    """
    Risc de pluja segons intensitat.
    """
    if rain > 10:
        return "high"
    elif rain > 5:
        return "medium"
    return "low"


def compute_meteo_features(m):
    """
    Genera features meteorològiques a partir d’un diccionari de mesures.
    """
    temp = m["temp_ext"]
    humidity = m["humidity"]
    wind = m["wind"]
    rain = m["rain"]

    return {
        "heat_index": compute_heat_index(temp, humidity),
        "wind_risk": compute_wind_risk(wind),
        "rain_risk": compute_rain_risk(rain),
        "comfort_index": temp - (0.55 * (1 - humidity/100) * (temp - 14.5)),
        "is_anomaly_temp": temp > 35 or temp < 5,
        "is_anomaly_humidity": humidity > 90 or humidity < 20,
        "is_anomaly_wind": wind > 40,
        "is_anomaly_rain": rain > 5
    }


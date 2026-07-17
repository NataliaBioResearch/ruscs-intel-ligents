import requests

def fetch_meteo(lat, lon):
    """
    Obtén dades meteorològiques externes (Open-Meteo) i les normalitza.

    Args:
        lat (float): Latitud del rusc.
        lon (float): Longitud del rusc.

    Returns:
        dict: Dades meteorològiques normalitzades.
    """

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}&hourly=temperature_2m,relativehumidity_2m,"
        f"windspeed_10m,precipitation"
    )

    r = requests.get(url)
    data = r.json()

    # Agafem l'última hora disponible
    temp = data["hourly"]["temperature_2m"][-1]
    humidity = data["hourly"]["relativehumidity_2m"][-1]
    wind = data["hourly"]["windspeed_10m"][-1]
    rain = data["hourly"]["precipitation"][-1]

    return {
        "temp_ext": temp,
        "humidity": humidity,
        "wind": wind,
        "rain": rain
    }

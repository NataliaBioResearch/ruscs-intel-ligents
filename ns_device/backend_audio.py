import numpy as np
from ns_acoustic.pipeline import run_acoustic_pipeline
from ns_acoustic.alerts_acoustic import acoustic_alerts
from ns_monitoring.influx_writer import write_measurement

def process_audio_block(pcm, rusc_id="R1", meteo=None, write_influx=False):
    """
    Processa un bloc d'àudio PCM i retorna resultats acústics estructurats.

    Args:
        pcm (np.ndarray): Àudio PCM mono 16 kHz.
        rusc_id (str): Identificador del rusc.
        meteo (dict): Dades meteorològiques externes.
        write_influx (bool): Escriure resultats a InfluxDB.

    Returns:
        dict: Resultats acústics (features, alertes, probabilitats CRNN).
    """

    # Normalització
    audio = pcm.astype(float) / 32768.0

    # Pipeline acústic complet
    result = run_acoustic_pipeline(
        audio=audio,
        rusc_id=rusc_id,
        meteo=meteo
    )

    # Alertes acústiques
    alerts = acoustic_alerts(result)

    output = {
        "rusc_id": rusc_id,
        "features": result,
        "alerts": alerts
    }

    # Opcional: escriure a InfluxDB
    if write_influx:
        write_measurement(
            bucket="acoustic",
            token="YOUR_TOKEN",
            org="YOUR_ORG",
            url="http://localhost:8086",
            measurement="acoustic_events",
            fields={
                "rms": result["rms"],
                "spectral_flux": result["spectral_flux"],
                "crnn_prob_swarm": result["crnn_prob_swarm"],
                "crnn_prob_distress": result["crnn_prob_distress"]
            },
            tags={"rusc": rusc_id}
        )

    return output


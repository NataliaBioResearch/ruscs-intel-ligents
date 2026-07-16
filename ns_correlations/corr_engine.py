import pandas as pd
from ns_monitoring.influx_reader import read_measurements
from ns_monitoring.alerts_corr import compute_correlations, detect_correlation_alerts

def run_correlation_engine(bucket, token, org, url, measurement, variables=None, threshold=0.75):
    """
    Executa el motor de correlacions del rusc.

    Args:
        bucket (str): Bucket d'InfluxDB.
        token (str): Token d'accés.
        org (str): Organització d'InfluxDB.
        url (str): URL del servidor.
        measurement (str): Measurement a consultar.
        variables (list): Variables a correlacionar.
        threshold (float): Llindar per alertes.

    Returns:
        dict: Resultats amb matriu de correlacions i alertes detectades.
    """

    # 1) Llegir dades
    rows = read_measurements(bucket, measurement, token, org, url)
    df = pd.DataFrame(rows)

    # 2) Filtrar variables si cal
    if variables:
        df = df[variables]

    # 3) Calcular correlacions
    corr_matrix = compute_correlations(df)

    # 4) Detectar alertes
    alerts = detect_correlation_alerts(corr_matrix, threshold)

    return {
        "correlations": corr_matrix,
        "alerts": alerts
    }

import pandas as pd

def compute_correlations(df, variables=None):
    """
    Calcula correlacions entre variables del rusc.

    Args:
        df (pd.DataFrame): Dataset amb mesures del rusc.
        variables (list): Llista de columnes a correlacionar. Si és None, usa totes.

    Returns:
        pd.DataFrame: Matriu de correlacions.
    """

    if variables is not None:
        df = df[variables]

    corr_matrix = df.corr()

    return corr_matrix


def detect_correlation_alerts(corr_matrix, threshold=0.75):
    """
    Detecta correlacions fortes que poden indicar alertes.

    Args:
        corr_matrix (pd.DataFrame): Matriu de correlacions.
        threshold (float): Valor mínim per considerar una correlació com a alerta.

    Returns:
        list: Llista d'alertes detectades.
    """

    alerts = []

    for var1 in corr_matrix.columns:
        for var2 in corr_matrix.columns:
            if var1 != var2:
                value = corr_matrix.loc[var1, var2]
                if abs(value) >= threshold:
                    alerts.append({
                        "var1": var1,
                        "var2": var2,
                        "correlation": float(value),
                        "severity": "high" if abs(value) > 0.85 else "medium",
                        "message": f"Correlació forta entre {var1} i {var2}: {value:.2f}"
                    })

    return alerts

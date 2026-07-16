from .crnn_inference import crnn_predict
from .alerts_acoustic import generate_acoustic_alerts
from .features import compute_acoustic_features

def run_acoustic_pipeline(audio_pcm, rusc_id, meteo=None):
    """
    Pipeline complet:
        PCM → espectrograma → CRNN → alertes → features
    """

    # Inferència CRNN
    probs = crnn_predict(audio_pcm)

    # Features acústiques
    feats = compute_acoustic_features(audio_pcm)

    # Alertes
    alerts = generate_acoustic_alerts(probs, feats, meteo)

    return {
        "rusc_id": rusc_id,
        "probs": probs,
        "features": feats,
        "alerts": alerts
    }

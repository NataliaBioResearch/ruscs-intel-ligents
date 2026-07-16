import numpy as np
import random
import librosa

def add_noise(audio, noise_level=0.02):
    """
    Afegeix soroll blanc al senyal.
    """
    noise = np.random.randn(len(audio)) * noise_level
    return audio + noise


def random_gain(audio, min_gain=0.8, max_gain=1.2):
    """
    Aplica un guany aleatori al senyal.
    """
    gain = random.uniform(min_gain, max_gain)
    return audio * gain


def time_stretch(audio, rate_range=(0.9, 1.1)):
    """
    Estira o comprimeix el senyal temporalment.
    """
    rate = random.uniform(*rate_range)
    return librosa.effects.time_stretch(audio, rate)


def pitch_shift(audio, sr=16000, semitone_range=(-2, 2)):
    """
    Aplica pitch shifting en semitons.
    """
    semitones = random.uniform(*semitone_range)
    return librosa.effects.pitch_shift(audio, sr, semitones)


def augment_audio(audio, sr=16000):
    """
    Aplica una combinació d’augmentacions aleatòries.
    Retorna:
        np.ndarray: senyal augmentat.
    """

    # Triem augmentacions aleatòries
    if random.random() < 0.5:
        audio = add_noise(audio)

    if random.random() < 0.5:
        audio = random_gain(audio)

    if random.random() < 0.3:
        audio = time_stretch(audio)

    if random.random() < 0.3:
        audio = pitch_shift(audio, sr)

    return audio.astype(np.float32)

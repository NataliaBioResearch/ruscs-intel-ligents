import os
import numpy as np
from ns_training.dataset_tools import load_training_sample
from ns_acoustic.crnn_model import load_crnn_model

def train_step(model, pcm, label):
    """
    Executa un pas d'entrenament amb un sol sample PCM.
    """
    mel = load_training_sample(pcm, augment=True)
    model.train_on_batch(mel, label)


def train_loop(model, dataset, epochs=10):
    """
    Bucle d'entrenament complet per al model CRNN.

    Args:
        model: model CRNN carregat.
        dataset: iterable de (pcm, label)
        epochs: nombre d'èpoques
    """
    for epoch in range(epochs):
        print(f"Epoch {epoch+1}/{epochs}")

        for pcm, label in dataset:
            train_step(model, pcm, label)

        print("Epoch completada.")


def main():
    """
    Punt d'entrada per entrenar el model CRNN.
    """
    model = load_crnn_model()

    # Exemple: dataset carregat des de data/audio_processed/
    # dataset = load_dataset()   # Aquí hi va el teu loader real

    # Placeholder per demostrar estructura:
    dataset = []  # Substitueix amb el teu dataset real

    train_loop(model, dataset, epochs=10)

    # Guardar el model entrenat
    model.save("models/crnn_real_trained.h5")
if __name__ == "__main__":
    main()

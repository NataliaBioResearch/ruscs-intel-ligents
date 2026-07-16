import os
import numpy as np
from ns_training.dataset_tools import load_training_sample
from ns_acoustic.crnn_model import load_crnn_model

def train_step(model, pcm, label):
    mel = load_training_sample(pcm, augment=True)
    model.train_on_batch(mel, label)

def train_loop(model, dataset, epochs=10):
    for epoch in range(epochs):
        print(f"Epoch {epoch+1}/{epochs}")
        for pcm, label in dataset:
            train_step(model, pcm, label)
        print("Epoch completada.")

def main():
    model = load_crnn_model()

    dataset = []  # Substitueix amb el teu loader real

    train_loop(model, dataset, epochs=10)

    model.save("models/crnn_real_trained.h5")

if __name__ == "__main__":
    main()

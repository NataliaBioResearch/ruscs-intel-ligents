import matplotlib.pyplot as plt
import numpy as np
import xgboost as xgb

def plot_crnn_training(history):
    """
    Mostra les corbes d'entrenament del CRNN.
    Args:
        history: objecte Keras History
    """
    plt.figure(figsize=(10, 5))
    plt.plot(history.history["loss"], label="Loss")
    if "val_loss" in history.history:
        plt.plot(history.history["val_loss"], label="Val Loss")

    plt.title("CRNN Training Loss")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_crnn_accuracy(history):
    """
    Mostra les corbes d'accuracy del CRNN.
    """
    if "accuracy" not in history.history:
        print("No hi ha accuracy al model.")
        return

    plt.figure(figsize=(10, 5))
    plt.plot(history.history["accuracy"], label="Accuracy")
    if "val_accuracy" in history.history:
        plt.plot(history.history["val_accuracy"], label="Val Accuracy")

    plt.title("CRNN Training Accuracy")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_xgb_feature_importance(model_path):
    """
    Mostra la importància de features del model XGBoost.
    Args:
        model_path: ruta al model swarm_xgb.json
    """
    booster = xgb.Booster()
    booster.load_model(model_path)

    importance = booster.get_score(importance_type="gain")
    features = list(importance.keys())
    values = list(importance.values())

    plt.figure(figsize=(10, 6))
    plt.barh(features, values)
    plt.title("XGBoost Feature Importance (Gain)")
    plt.xlabel("Gain")
    plt.grid(True)
    plt.show()


def plot_probability_distribution(preds_dict):
    """
    Mostra la distribució de probabilitats d'un model acústic.
    Args:
        preds_dict: dict {classe: probabilitat}
    """
    classes = list(preds_dict.keys())
    values = list(preds_dict.values())

    plt.figure(figsize=(10, 5))
    plt.bar(classes, values)
    plt.title("Distribució de probabilitats CRNN")
    plt.ylabel("Probabilitat")
    plt.grid(True)
    plt.show()

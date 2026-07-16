import matplotlib.pyplot as plt
import numpy as np
import xgboost as xgb

def plot_xgb_feature_importance(model_path):
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
    classes = list(preds_dict.keys())
    values = list(preds_dict.values())

    plt.figure(figsize=(10, 5))
    plt.bar(classes, values)
    plt.title("Distribució de probabilitats CRNN")
    plt.ylabel("Probabilitat")
    plt.grid(True)
    plt.show()

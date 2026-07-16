import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_temperature(df):
    """
    Gràfic de temperatura externa.
    Requereix columnes: timestamp, temp_c
    """
    plt.figure(figsize=(10, 4))
    plt.plot(df["timestamp"], df["temp_c"], color="red")
    plt.title("Temperatura externa")
    plt.xlabel("Temps")
    plt.ylabel("°C")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_humidity(df):
    """
    Gràfic d'humitat externa.
    Requereix columnes: timestamp, humidity_pct
    """
    plt.figure(figsize=(10, 4))
    plt.plot(df["timestamp"], df["humidity_pct"], color="blue")
    plt.title("Humitat externa")
    plt.xlabel("Temps")
    plt.ylabel("%")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_wind(df):
    """
    Gràfic de velocitat del vent.
    Requereix columnes: timestamp, wind_ms
    """
    plt.figure(figsize=(10, 4))
    plt.plot(df["timestamp"], df["wind_ms"], color="green")
    plt.title("Velocitat del vent")
    plt.xlabel("Temps")
    plt.ylabel("m/s")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_rain(df):
    """
    Gràfic de pluja acumulada.
    Requereix columnes: timestamp, rain_mm
    """
    plt.figure(figsize=(10, 4))
    plt.plot(df["timestamp"], df["rain_mm"], color="purple")
    plt.title("Pluja (mm)")
    plt.xlabel("Temps")
    plt.ylabel("mm")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_pressure(df):
    """
    Gràfic de pressió atmosfèrica.
    Requereix columnes: timestamp, pressure_hpa
    """
    plt.figure(figsize=(10, 4))
    plt.plot(df["timestamp"], df["pressure_hpa"], color="orange")
    plt.title("Pressió atmosfèrica")
    plt.xlabel("Temps")
    plt.ylabel("hPa")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_meteo_correlations(df):
    """
    Heatmap de correlacions meteorològiques.
    """
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlacions meteorològiques")
    plt.tight_layout()
    plt.show()

import xgboost as xgb
import pandas as pd

def train_swarm_xgb(data_csv, model_out):
    df = pd.read_csv(data_csv)

    X = df[["weight", "weight_trend", "sound_trend",
            "acoustic_swarm_prob", "temp_in", "temp_out",
            "humidity", "correlation_score"]]

    y = df["label_swarm"]

    dtrain = xgb.DMatrix(X, label=y)

    params = {
        "objective": "binary:logistic",
        "eval_metric": "logloss",
        "max_depth": 5,
        "eta": 0.1
    }

    model = xgb.train(params, dtrain, num_boost_round=300)
    model.save_model(model_out)

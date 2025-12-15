import joblib
import pandas as pd

MODEL_DIR = "models"

def load_model():
    rf = joblib.load(f"{MODEL_DIR}/main_model.joblib")
    scaler = joblib.load(f"{MODEL_DIR}/main_scaler.joblib")
    le = joblib.load(f"{MODEL_DIR}/label_encoder.joblib")
    return rf, scaler, le

def prepare(df, features):
    for c in features:
        if c not in df.columns:
            df[c] = 0
    return df[features].fillna(0)

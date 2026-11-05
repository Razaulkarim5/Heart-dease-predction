from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI

from app.schemas import HeartInput, PredictionOut

MODEL_PATH = Path(__file__).resolve().parent.parent / "model" / "heart_model.joblib"
FEATURES = list(HeartInput.model_fields.keys())

app = FastAPI(title="Heart Disease Prediction API", version="1.0.0")
model = joblib.load(MODEL_PATH)  # loaded once at startup


@app.get("/")
def root():
    return {"message": "Heart Disease API. See /docs for Swagger UI."}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/info")
def info():
    return {
        "model_type": type(model.steps[-1][1]).__name__,
        "pipeline_steps": [name for name, _ in model.steps],
        "n_features": len(FEATURES),
        "features": FEATURES,
    }


@app.post("/predict", response_model=PredictionOut)
def predict(payload: HeartInput):
    X = pd.DataFrame([payload.model_dump()])[FEATURES]
    proba = float(model.predict_proba(X)[0][1])
    return PredictionOut(heart_disease=proba >= 0.5, probability=round(proba, 4))

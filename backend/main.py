from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("model/bot_model.pkl")

EXPECTED_FEATURE_KEYS = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10']

class InputData(BaseModel):
    data: dict

def extract_features(data: dict) -> dict:
    # TODO: Replace with your actual feature extraction logic
    # Make sure all expected keys are present!
    return {
        'f1': 1.0,
        'f2': 2.0,
        'f3': 3.0,
        'f4': 4.0,
        'f5': 5.0,
        'f6': 6.0,
        'f7': 7.0,
        'f8': 8.0,
        'f9': 9.0,
        'f10': 10.0
    }

def features_dict_to_vector(features: dict):
    # Use EXPECTED_FEATURE_KEYS to maintain order and fill missing with 0.0
    return [float(features.get(k, 0.0)) for k in EXPECTED_FEATURE_KEYS]

@app.post("/analyze")
async def analyze(input_data: InputData):
    features_dict = extract_features(input_data.data)
    feature_vector = features_dict_to_vector(features_dict)

    expected_len = model.n_features_in_

    if len(feature_vector) != expected_len:
        return {
            "error": f"Feature vector length is {len(feature_vector)} but model expects {expected_len}."
        }

    try:
        features_array = np.array(feature_vector, dtype=float).reshape(1, -1)
    except Exception as e:
        return {"error": f"Invalid feature vector: {e}"}

    try:
        proba = model.predict_proba(features_array)[0]
    except Exception as e:
        return {"error": f"Model prediction failed: {e}"}

    prediction = int(proba[1] > 0.7) if len(proba) > 1 else 0
    confidence = max(proba)

    return {
        "is_bot": "maybe" if confidence < 0.7 else bool(prediction),
        "confidence": confidence,
    }

@app.get("/")
async def root():
    return {"message": "UIDAI Passive Bot Detection API running"}

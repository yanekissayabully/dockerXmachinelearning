import joblib
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="ML API dlya Iris",
    description="API dlya predskazaniya klassa iris na osnove priznakov",
    version="1.0.0"
)

try:
    model = joblib.load('model.joblib')
except Exception as e:
    print(f"oshibka: {e}")
    model = None

class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float 
    petal_length: float 
    petal_width: float  
    
    class Config:
        json_schema_extra = {
            "example": {
                "sepal_length": 5.1,
                "sepal_width": 3.5,
                "petal_length": 1.4,
                "petal_width": 0.2
            }
        }

IRIS_CLASSES = {
    0: "setosa",
    1: "versicolor",
    2: "virginica"
}

@app.get("/")
def root():
    return {"message": "ML API is running", "status": "active"}

@app.post("/predict")
def predict(features: IrisFeatures):
    if model is None:
        raise HTTPException(status_code=500, detail="fail")
    
    input_data = np.array([[
        features.sepal_length,
        features.sepal_width,
        features.petal_length,
        features.petal_width
    ]])

    prediction = model.predict(input_data)[0]
    prediction_proba = model.predict_proba(input_data)[0]
    
    return {
        "prediction": int(prediction),
        "class_name": IRIS_CLASSES[prediction],
        "probabilities": {
            "setosa": round(float(prediction_proba[0]), 4),
            "versicolor": round(float(prediction_proba[1]), 4),
            "virginica": round(float(prediction_proba[2]), 4)
        }
    }

@app.get("/health")
def health():
    return {"status": "healthy", "model_loaded": model is not None}
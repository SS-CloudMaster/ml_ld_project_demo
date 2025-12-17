from fastapi import FastAPI
#Lightweight API framework
model=joblib.load("models/model_v1.joblib")
#Load once at startup (performance).
@app.post("/predict")
#Stateless inference endpoint.
#FastAPI gives async support, validation, and OpenAPI docs for free
import fastapi
import pandas as pd

from challenge.model_loader import load_trained_model 
from challenge.schemas.flight_data import FlightRequest
from fastapi import HTTPException


app = fastapi.FastAPI()

# Load the trained model
model = load_trained_model()

@app.get("/health", status_code=200)
async def get_health() -> dict:
    return {"status": "OK"}

@app.post("/predict", status_code=200)
async def post_predict(request: FlightRequest) -> dict:
    input_data = pd.DataFrame([flight.dict() for flight in request.flights])
    try:
        input_features = model.preprocess(data=input_data, is_training=False)
    except KeyError as e:
        raise HTTPException(status_code=400, detail=f"Invalid input column: {str(e)}")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Input validation error: {str(e)}")

    predictions = model.predict(input_features)

    return {"predict": predictions}

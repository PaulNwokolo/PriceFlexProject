
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib 
import numpy as np

app = FastAPI()

# Load models
demand_model = joblib.load("C:/Users/PAUL/Desktop/PriceFlex/data/model/demand_model.pkl")
pricing_model = joblib.load("C:/Users/PAUL/Desktop/PriceFlex/data/model/pricing_model.pkl")

# loading preprocesser
import pickle
with open("C:/Users/PAUL/Desktop/PriceFlex/data/preprocessed/preprocessor.pkl", 'rb') as f:
    preprocessor = pickle.load(f)
    

# Building the class
class PricingRequest(BaseModel):
        competitor_price = float
        day_of_week: int
        hour_of_day: int
    
    
@app.post('/recommend_price')
def recommend_price(data: PricingRequest):
    try:
        features = np.array([[data.competitor_price, data.day_of_week, data.hour_of_day]])
        features_preprocessed = preprocessor.transform(features)
        predicted_demand = demand_model.predict(features_preprocessed)[0]
        recommend_price = pricing_model.predict(features_preprocessed)[0]
        return {'recommend_price': recommend_price, 'predicted_demand': predicted_demand}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    


# ⚡ FastAPI - Food Delivery Time Prediction

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

import pandas as pd
import joblib


# 🚀 Create FastAPI App
app = FastAPI(
    title="Food Delivery Time Prediction API",
    description="ML API for predicting food delivery time",
    version="1.0"
)


# 🤖 Load ML Model + Scaler
model = joblib.load("food_delivery_model.pkl")
scaler = joblib.load("food_delivery_scaler.pkl")


# 🎨 Static Files
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


# 🛡️ Input Validation
class DeliveryInput(BaseModel):

    Delivery_person_Age: float = Field(..., ge=18, le=70)

    Delivery_person_Ratings: float = Field(
        ...,
        ge=1,
        le=5
    )

    Road_traffic_density: str

    Vehicle_condition: float = Field(
        ...,
        ge=0,
        le=5
    )

    multiple_deliveries: float = Field(
        ...,
        ge=0,
        le=5
    )

    order_day: float = Field(
        ...,
        ge=1,
        le=31
    )

    order_month: float = Field(
        ...,
        ge=1,
        le=12
    )

    order_dayofweek: float = Field(
        ...,
        ge=0,
        le=6
    )

    is_weekend: int = Field(
        ...,
        ge=0,
        le=1
    )

    order_hour: float = Field(
        ...,
        ge=0,
        le=23
    )

    order_minute: float = Field(
        ...,
        ge=0,
        le=59
    )

    pickup_delay_min: float = Field(
        ...,
        ge=0
    )

    distance_km: float = Field(
        ...,
        ge=0
    )

    Weatherconditions: str

    Type_of_order: str

    Type_of_vehicle: str

    Festival: str

    City: str


# 🏠 Website Home
@app.get("/")
def home():

    return FileResponse(
        "templates/index.html"
    )


# ❤️ Health Check
@app.get("/health")
def health_check():

    return {
        "status": "healthy",
        "model": "Food Delivery Random Forest"
    }


# 🔮 Prediction API
@app.post("/predict")
def predict(data: DeliveryInput):

    # 📦 Convert input into dictionary
    input_data = data.model_dump()


    # 🚦 Traffic Encoding
    traffic_map = {

        "Low": 0,

        "Medium": 1,

        "High": 2,

        "Jam": 3

    }


    input_data["Road_traffic_density"] = traffic_map[
        input_data["Road_traffic_density"]
    ]


    # 📊 Create DataFrame
    df = pd.DataFrame(
        [input_data]
    )


    # 🔤 One-Hot Encoding
    df = pd.get_dummies(

        df,

        columns=[

            "Weatherconditions",

            "Type_of_order",

            "Type_of_vehicle",

            "Festival",

            "City"

        ],

        dtype=int

    )


    # 📌 Model Training Features
    feature_columns = [

        "Delivery_person_Age",

        "Delivery_person_Ratings",

        "Road_traffic_density",

        "Vehicle_condition",

        "multiple_deliveries",

        "order_day",

        "order_month",

        "order_dayofweek",

        "is_weekend",

        "order_hour",

        "order_minute",

        "pickup_delay_min",

        "distance_km",


        # 🌦️ Weather
        "Weatherconditions_Fog",

        "Weatherconditions_Sandstorms",

        "Weatherconditions_Stormy",

        "Weatherconditions_Sunny",

        "Weatherconditions_Windy",


        # 🍔 Order
        "Type_of_order_Drinks",

        "Type_of_order_Meal",

        "Type_of_order_Snack",


        # 🛵 Vehicle
        "Type_of_vehicle_electric_scooter",

        "Type_of_vehicle_motorcycle",

        "Type_of_vehicle_scooter",


        # 🎉 Festival
        "Festival_Yes",


        # 🏙️ City
        "City_Semi-Urban",

        "City_Urban"

    ]


    # 🔄 Make columns exactly same as training
    df = df.reindex(

        columns=feature_columns,

        fill_value=0

    )


    # 📏 Feature Scaling
    scaled_data = scaler.transform(df)


    # 🤖 ML Prediction
    prediction = model.predict(
        scaled_data
    )


    # ⏱️ Final Prediction
    predicted_time = round(
        float(prediction[0]),
        2
    )


    # 📤 Response
    return {

        "predicted_delivery_time":
            predicted_time,

        "unit":
            "minutes"

    }
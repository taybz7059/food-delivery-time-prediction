# 🍔 Food Delivery Time Prediction

<p align="center">

<a href="https://food-delivery-time-prediction-bfsg.onrender.com/">
<img src="https://img.shields.io/badge/🌐%20Live%20Demo-Visit%20Website-success?style=for-the-badge">
</a>

<a href="https://github.com/taybz7059/food-delivery-time-prediction">
<img src="https://img.shields.io/badge/🐙%20GitHub-Source%20Code-black?style=for-the-badge">
</a>

</p>

<p align="center">
  <b>Machine Learning Web Application for Food Delivery Time Prediction</b>
</p>

## 📌 Project Overview

Food Delivery Time Prediction is a Machine Learning project that predicts the estimated delivery time of a food order in minutes.

The project uses delivery-related information such as delivery partner details, traffic conditions, weather, vehicle information, order type, distance, and pickup delay to predict the delivery time.

The trained Machine Learning model is deployed as a web application using FastAPI and Render.

---

---

## 🖥️ Project Screenshots

### 🏠 Home Page

![Food Delivery Prediction Website](screenshots/home.png)

### 📊 Prediction Result

![Prediction Result](screenshots/prediction.png)

---
## 🎯 Objective

The main objective of this project is to build a Machine Learning model that can accurately predict food delivery time and provide predictions through a user-friendly web application.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- FastAPI
- HTML
- CSS
- JavaScript
- Git
- GitHub
- Git LFS
- Render

---

## 📊 Dataset

The dataset contains more than 45,000 food delivery records.

### Important Features

- Delivery Person Age
- Delivery Person Rating
- Weather Conditions
- Road Traffic Density
- Vehicle Condition
- Multiple Deliveries
- Order Date & Time
- Pickup Delay
- Distance
- Type of Order
- Type of Vehicle
- Festival
- City

### Target Variable

`Time_taken(min)`

---

## 🔄 Machine Learning Workflow

The project follows an end-to-end Machine Learning workflow:

1. Data Loading
2. Data Cleaning
3. Missing Value Handling
4. Feature Engineering
5. Exploratory Data Analysis
6. Encoding Categorical Features
7. Feature Scaling
8. Train-Test Split
9. Model Training
10. Model Comparison
11. Hyperparameter Tuning
12. Model Evaluation
13. Model Saving
14. FastAPI Development
15. Web Deployment

---

## 🤖 Machine Learning Models

The following regression models were tested:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor

### Model Performance

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | 4.93 | 6.21 | 0.57 |
| Decision Tree | 4.14 | 5.43 | 0.67 |
| Random Forest | 3.17 | 3.98 | 0.82 |
| XGBoost | 3.27 | 4.12 | 0.81 |
| Tuned Random Forest | **3.15** | **3.96** | **0.825** |

### 🏆 Final Model

**Random Forest Regressor**

After hyperparameter tuning, the Random Forest model achieved approximately:

- **MAE:** 3.15 minutes
- **RMSE:** 3.96 minutes
- **R²:** 0.825

This means the model's average absolute prediction error is approximately 3.15 minutes.

---

## 🌐 Live Demo

👉 **[Try the Live Website](https://food-delivery-time-prediction-bfsg.onrender.com/)**

---

## 📁 Project Structure

```text
Food_Delivery_ML/
│
├── app.py
├── requirements.txt
├── food_delivery_model.pkl
├── food_delivery_scaler.pkl
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js

# Karachi House Price Prediction ML App

This project is a machine learning application that predicts house prices in Karachi based on user inputs such as location, number of bedrooms, bathrooms, square footage, and more. The model is built using a Random Forest Regressor and is deployed using Streamlit.

### Live Demo

Check out the live app [here](https://karachi-house-price-prediction.streamlit.app)!

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [How to Use](#how-to-use)
- [Steps Performed](#steps-performed)
- [Model Training](#model-training)
- [Technologies Used](#technologies-used)

## Overview

The **Karachi House Price Prediction App** allows users to input key details of a property, including location, number of rooms, and square footage, and instantly receive a predicted house price. This tool aims to provide an estimate based on historical data, making it easier for users to make informed decisions about real estate in Karachi.

## Features

- **Location Selection**: Choose from various popular locations in Karachi.
- **House Details Input**: Enter the number of bedrooms, bathrooms, and the size of the house in square yards.
- **Prediction**: Get an instant price estimate based on the Random Forest Regressor model.
- **Purpose and Property Type**: Choose the purpose of the property (For Sale/For Rent) and the type (House, Flat, etc.).
- **Interactive User Interface**: A modern and responsive interface built with Streamlit.

## How to Use

1. Navigate to the app using the live link or run it locally.
2. Input the required property details:
   - Select the **location** of the house.
   - Input the number of **bedrooms**, **bathrooms**, and **square yards**.
   - Select the **property purpose** (For Sale/For Rent).
   - Choose the **property type** (House, Flat, etc.).
3. Click on the **"Predict House Price"** button to get an estimate.
4. The predicted price will be displayed in the app.

## Steps Performed

1. **Data Preprocessing**:
   - Handled missing and duplicate values.
   - Remove outliers and abnormal data points.
   
2. **Feature Engineering**:
   - Converted and scaled continous features e.g prices, sq_feets, sq_yards.
   - Applied one-hot and ordinal encoding to categorical variables for better model interpretation.

3. **Model Building**:
   - Selected Random Forest Regressor as the best predictive model among Linear Regression models and XGBoost Regressor.
   - Split the data into training and test sets.
   - Trained the model using the training dataset.

4. **Hyperparameter Tuning**:
   - Performed Grid Search with K-Fold Cross-Validation to optimize model parameters.
   - Tuned key hyperparameters such as the number of trees, maximum depth etc.

5. **Model Evaluation**:
   - Evaluated the model using metrics such as R² score, Root Mean Squared Error (RMSE), Mean Absolute Error (MAE).
   - Selected the best-performing model for deployment.

6. **Application Development**:
   - Built a Streamlit app with an interactive UI to accept user inputs.
   - Integrated the trained Random Forest model to generate predictions based on user inputs.

7. **Deployment**:
   - Deployed the app on Streamlit, making it accessible through the web.

## Model Training

The Random Forest model was trained on historical house price data, with the following features:
- Location
- Number of bedrooms
- Number of bathrooms
- Size of the house (square yards)
- Property type and purpose

For hyperparameter tuning and model evaluation, a **Grid Search** with **K-Fold Cross-Validation** was applied to ensure optimal performance.

## Technologies Used

- **Python**: Backend programming language.
- **Streamlit**: For building the web interface and deploying the app.
- **scikit-learn**: For training the machine learning model (Random Forest Regressor).
- **Pandas & NumPy**: For data manipulation and preprocessing.
- **Matplotlib & Seaborn**: For data visualizations.
- **Git**: For version control.
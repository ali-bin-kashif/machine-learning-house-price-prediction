import streamlit as st
import pickle
import json
import numpy as np

# Load the trained model
with open('./artifacts/model.pkl', 'rb') as file:
    model = pickle.load(file)

# Load columns metadata (for locations, etc.)
with open('./artifacts/columns.json', 'r') as file:
    columns = json.load(file)

banner_image = './artifacts/karachi.jpg'

# Property type encoding
property_type_encoding = {'House': 1, 'Flat': 2, 'Lower Portion': 3, 'Upper Portion': 4}

# Function to make predictions
def predict_price(location, rooms, bathrooms, sq_yards, purpose, property_type):

    # print(location, rooms, bathrooms, sq_yards, purpose, property_type)
    # Create an array with zeros for all columns in the model
    input_array = np.zeros(len(columns['columns']))
    
    # Set the input features
    loc_index = columns['columns'].index(location)
    input_array[loc_index] = 1  # One-hot encoding for location
    
    # Set numerical inputs
    input_array[columns['columns'].index('bedrooms')] = rooms
    input_array[columns['columns'].index('baths')] = bathrooms
    input_array[columns['columns'].index('sq_yards')] = sq_yards
    
    # Encode the purpose ('For Sale': 1, 'For Rent': 2)
    input_array[columns['columns'].index('purpose')] = 1 if purpose == 'For Rent' else 2
    
    # Encode property type
    input_array[columns['columns'].index('property_type')] = property_type_encoding[property_type]

    print(input_array)
    
    # Reshape to 2D array for model prediction
    prediction = model.predict([input_array])
    
    return prediction[0]  # Return the predicted price

# # App layout and design
# st.title("Karachi House Price Prediction")
# st.markdown("""
#     ### Welcome to the Karachi House Price Prediction App!
#     Provide the details of your house, and get an instant price prediction based on historical data.
# """)

# # Dropdown for location
# locations = columns['columns'][6:]  # Extract location columns
# location = st.selectbox('Select Location:', tuple(locations))

# # Input fields for number of bedrooms, bathrooms, and square yards
# rooms = st.number_input('Enter the number of bedrooms', format='%d', step=1, min_value=1, max_value=15)
# bathrooms = st.number_input('Enter the number of bathrooms', format='%d', step=1, min_value=1, max_value=15)
# sq_yards = st.number_input('Enter the square yards of the house', format='%d', step=1, min_value=1)

# # Dropdown for purpose of house
# purpose = st.selectbox('Select the purpose of the property:', ('For Sale', 'For Rent'))

# # Dropdown for property type
# property_type = st.selectbox('Select Property Type:', ('House', 'Flat', 'Lower Portion', 'Upper Portion'))

# # Button to make prediction
# if st.button('Predict House Price'):
#     predicted_price = predict_price(location, rooms, bathrooms, sq_yards, purpose, property_type)

#     if predicted_price < 1:
#         predicted_price = predicted_price * 100000
#         st.subheader(f"Predicted Price: PKR {predicted_price:,.0f}")
#     else:
#         # Display the prediction result
#         st.subheader(f"Predicted Price: PKR {predicted_price:,.2f} Lakhs")

from PIL import Image

# Custom CSS for modern design
st.markdown(
    """
    <style>
    body {
        background-color: #f7f9fc;
    }

    .main-title {
        font-size: 46px;
        font-weight: 600;
        color: #2c3e50;
        text-align: center;
        margin-top: -50px;
    }

    .sub-title {
        font-size: 20px;
        color: #34495e;
        text-align: center;
        margin-bottom: 40px;
    }

    .stButton button {
        background-color: #1abc9c;
        color: white;
        padding: 12px 24px;
        border-radius: 8px;
        font-size: 18px;
        font-weight: 600;
        border: none;
        transition: background-color 0.3s ease;
    }

    .stButton button:hover {
        background-color: #16a085;
        color: white;
    }

    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
        color: #95a5a6;
        font-size: 14px;
        padding: 10px;
    }

    .footer a {
        color: #2980b9;
        text-decoration: none;
    }
    </style>
    """, unsafe_allow_html=True
)
st.__name__ = "Karachi House Price Prediction"

# Main Title
st.markdown("<h1 class='main-title'>Karachi House Price Prediction📈</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='sub-title'>Get instant price predictions based on your house requirements, Happy Living!</h3>", unsafe_allow_html=True)

# Optional Banner or Header Image (Replace 'banner_image.jpg' with your own image path)
image = Image.open(banner_image)
st.image(image, use_column_width=True)

# Property Details Section
st.markdown("<h4 style='text-align: center;'>Enter House or Property Details</h4>", unsafe_allow_html=True)

# Using columns for a clean layout
col1, col2, col3 = st.columns(3)

with col1:
    locations = columns['columns'][6:]  # Example locations
    location = st.selectbox('Select Location:', tuple(locations))

with col2:
    rooms = st.number_input('Enter the number of bedrooms', format='%d', step=1, min_value=1, max_value=15)

with col3:
    bathrooms = st.number_input('Enter the number of bathrooms', format='%d', step=1, min_value=1, max_value=15)

# Square yards input
sq_yards = st.number_input('Enter the square yards of the house', format='%d', step=1, min_value=40, max_value=5000)

# Using columns for the purpose and property type
col4, col5 = st.columns(2)

with col4:
    purpose = st.selectbox('Select the purpose of the property:', ('For Sale', 'For Rent'))

with col5:
    property_type = st.selectbox('Select Property Type:', ('House', 'Flat', 'Lower Portion', 'Upper Portion'))

# Predict Button
st.markdown("<br>", unsafe_allow_html=True)  # Adding space
if st.button('Predict House Price'):

    predicted_price = predict_price(location, rooms, bathrooms, sq_yards, purpose, property_type)

    # Adjust price display
    if predicted_price < 1:
        predicted_price = predicted_price * 100000
        st.success(f"Predicted Price: PKR {predicted_price:,.0f}")
    else:
        st.success(f"Predicted Price: PKR {predicted_price:,.2f} Lakhs")

# Footer Section
st.markdown(
    """
    <div class='footer'>
        Made by Ali | <a href='https://ali-bin-kashif-portfolio.vercel.app'>Visit Website</a> | © 2024
    </div>
    """, unsafe_allow_html=True
)

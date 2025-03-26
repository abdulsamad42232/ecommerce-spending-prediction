import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("model/trained_model.pkl")

# Streamlit UI
st.title("E-Commerce Yearly Amount Spent Prediction")

# Input fields with relevant units
session_length = st.number_input("Average Session Length (hours)", min_value=0.0, format="%.2f")
time_on_app = st.number_input("Time on App (minutes)", min_value=0.0, format="%.2f")
time_on_website = st.number_input("Time on Website (minutes)", min_value=0.0, format="%.2f")
membership_length = st.number_input("Length of Membership (years)", min_value=0.0, format="%.2f")

# Predict button
if st.button("Predict"):
    # Convert minutes to hours for consistency (if required by the model)
    time_on_app_hours = time_on_app 
    time_on_website_hours = time_on_website

    # Prepare input features
    input_data = np.array([[session_length, time_on_app_hours, time_on_website_hours, membership_length]])

    # Make prediction
    prediction = model.predict(input_data)[0]
    
    st.success(f"Predicted Yearly Amount Spent: ${prediction:.2f}")

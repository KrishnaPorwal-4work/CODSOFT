import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load(r"C:\Users\hp\Desktop\ML_Basic_Models\SALES_PREDICTION\sales_model.pkl")

st.title("📊 Sales Prediction App")

st.write("Enter advertising budget to predict sales")

# User inputs
tv = st.number_input("TV Advertising Budget", min_value=0.0)
radio = st.number_input("Radio Advertising Budget", min_value=0.0)

# Predict button
if st.button("Predict Sales"):
    input_data = np.array([[tv, radio]])
    prediction = model.predict(input_data)
    
    st.success(f"Predicted Sales: {prediction[0]:.2f}")
import streamlit as st
import numpy as np
import pickle

# Load model
with open(r"C:\Users\hp\Desktop\ML_Basic_Models\IRIS_FLOWER_CLASSIFICATION\Iris_Flower.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Iris Flower Prediction")

# Inputs
sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0)
sepal_width = st.slider("Sepal Width (cm)", 1.5, 5.0)
petal_length = st.slider("Petal Length (cm)", 1.0, 8.0)
petal_width = st.slider("Petal Width (cm)", 0.0, 3.0)

# Prediction
if st.button("Predict"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction  = model.predict(input_data)

    species = ["Setosa", "Versicolor", "Virginica"]

    st.success(f"Predicted Iris Species: {species[prediction[0]]}")
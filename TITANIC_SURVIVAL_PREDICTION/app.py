import streamlit as st
import pandas as pd
import pickle

with open(r"C:\Users\hp\Desktop\ML_Basic_Models\TITANIC_SURVIVAL_PREDICTION\titanic_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🚢 Titanic Survival Prediction")

pclass = st.selectbox("Passenger Class", [1,2,3])
sex = st.selectbox("Sex", ["Male", "Female"])
age = st.slider("Age", 1, 80, 25)
fare = st.slider("Fare", 0.0, 500.0, 50.0)
embarked = st.selectbox("Embarked", ["S","C","Q"])
family = st.slider("Family Size", 1, 10, 1)

# Encoding
sex = 1 if sex=="Male" else 0
emb_q = 1 if embarked=="Q" else 0
emb_s = 1 if embarked=="S" else 0
is_alone = 1 if family==1 else 0

input_df = pd.DataFrame([[pclass, sex, age, fare, emb_q, emb_s, family, is_alone]],
columns=['Pclass','Sex','Age','Fare','Embarked_Q','Embarked_S','FamilySize','IsAlone'])

if st.button("Predict"):
    pred = model.predict(input_df)
    if pred[0] == 1:
        st.success("Survived ✅")
    else:
        st.error("Did Not Survive ❌")
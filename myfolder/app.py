import streamlit as st
import pandas as pd
import pickle
import json

# Load model and food mapping
with open('vitamin_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('food_mapping.json', 'r') as f:
    food_mapping = json.load(f)

st.title("Athlete Vitamin D Deficiency Prediction")
st.write("Enter details to predict Vitamin D deficiency and get food recommendations.")

# User input
age = st.slider("Age", 18, 80, 25)
sex = st.selectbox("Sex", ["Male", "Female"])
activity_level = st.selectbox("Activity Level", ["High", "Moderate", "Low"])
fatigue = st.selectbox("Fatigue", ["Yes", "No"])
muscle_pain = st.selectbox("Muscle Pain", ["Yes", "No"])
vegan_diet = st.selectbox("Vegan Diet", ["Yes", "No"])
sunlight_exposure = st.slider("Sunlight Exposure (hours/week)", 0, 20, 5)

# Convert inputs
input_data = pd.DataFrame({
    'age': [age],
    'sex': [1 if sex == "Male" else 0],
    'activity_level': [3 if activity_level == "High" else 2 if activity_level == "Moderate" else 1],
    'fatigue': [1 if fatigue == "Yes" else 0],
    'muscle_pain': [1 if muscle_pain == "Yes" else 0],
    'vegan_diet': [1 if vegan_diet == "Yes" else 0],
    'sunlight_exposure': [sunlight_exposure]
})

# Predict
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.write("**Prediction**: Likely Vitamin D deficiency")
        st.write("**Recommended Foods**:")
        for food in food_mapping['vitamin_d']:
            st.write(f"- {food}")
    else:
        st.write("**Prediction**: No Vitamin D deficiency")

import shutil
shutil.move('/content/app.py', '/content/drive/MyDrive/app.py')



import streamlit as st
import pandas as pd
import numpy as np
import pickle

# with open("pipe.pkl", "rb") as f:
#     model = pickle.load(f)
model = pickle.load(open("pipe.pkl","rb+"))

st.title("Medical Cost Prediction")

# age = st.number_input("Age")
# sex = st.selectbox("Sex", ["Female", "Male"])
# bmi = st.number_input("BMI")
# children = st.number_input("Children", step=1)
# smoker = st.selectbox("Smoker", ["No", "Yes"])
# region = st.selectbox("Region",
#                       ["northeast", "northwest", "southeast", "southwest"])

# User Inputs

age = st.number_input(
    "Age",
    value=30,
    min_value=18,
    max_value=100,
    step=1
)

sex = st.selectbox(
    "sex",
    ["Female", "Male"]
)

bmi = st.number_input(
    "BMI",
    value=25.0,
    min_value=10.0,
    max_value=60.0,
    step=0.1
)

children = st.number_input(
    "Children",
    value=0,
    min_value=0,
    max_value=10,
    step=1
)

smoker = st.selectbox(
    "Smoker",
    ["No", "Yes"]
)

region = st.selectbox(
    "Region",
    ["northeast", "northwest", "southeast", "southwest"]
)

sex = 1 
if sex == "Male":
    sex = 1
else:
    sex = 0
  



smoker = 1 
if smoker == "Yes":
    smoker = 1
else:
    smoker = 0
    

region_dict = {
    "northeast": 0,
    "northwest": 1,
    "southeast": 2,
    "southwest": 3
}

region = region_dict[region]

if st.button("Predict"):
    data = pd.DataFrame([[age, sex, bmi, children, smoker, region]],
                        columns=['age','sex','bmi','children','smoker','region'])

    result = model.predict(data)

    st.success(f"Predicted Medical Charges: ₹{result[0]:.2f}")
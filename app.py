import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open('pipe.pkl', 'rb'))

st.title("Medical Cost Prediction")

age = st.number_input("Age")
sex = st.selectbox("Sex", ["Female", "Male"])
bmi = st.number_input("BMI")
children = st.number_input("Children", step=1)
smoker = st.selectbox("Smoker", ["No", "Yes"])
region = st.selectbox("Region",
                      ["northeast", "northwest", "southeast", "southwest"])

sex = 1 if sex == "Male" else 0
smoker = 1 if smoker == "Yes" else 0

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
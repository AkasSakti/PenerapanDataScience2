# app.py
import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the trained model and scaler
model = joblib.load('model/random_forest_model.joblib')
scaler = joblib.load('model/scaler_model.joblib')

# Title
st.title('Student Attrition Prediction App')

# User Inputs
st.header('Input Student Information')

course = st.selectbox('Course', [
    'Biofuel Production Technologies',
    'Animation and Multimedia Design',
    'Social Service (evening attendance)',
    'Agronomy',
    'Communication Design',
    'Veterinary Nursing',
    'Informatics Engineering',
    'Equinculture',
    'Management',
    'Social Service',
    'Tourism',
    'Nursing',
    'Oral Hygiene',
    'Advertising and Marketing Management',
    'Journalism and Communication',
    'Basic Education',
    'Management (evening attendance)'
])

gender = st.selectbox('Gender', ['Male', 'Female'])
daytime = st.selectbox('Daytime/evening attendance', ['Daytime', 'Evening'])
age = st.number_input('Age at Enrollment', min_value=16, max_value=60, value=20)

admission_grade = st.slider('Admission Grade', 0.0, 20.0, 10.0)
special_needs = st.selectbox('Educational Special Needs', [0, 1])
debtor = st.selectbox('Debtor', [0, 1])
tuition_up_to_date = st.selectbox('Tuition Fees Up to Date', [0, 1])
scholarship = st.selectbox('Scholarship Holder', [0, 1])

sem1_grade = st.slider('Curricular Units 1st Sem Grade', 0.0, 20.0, 10.0)
sem2_grade = st.slider('Curricular Units 2nd Sem Grade', 0.0, 20.0, 10.0)

# Mapping categorical features
course_map = {
    'Biofuel Production Technologies': 0,
    'Animation and Multimedia Design': 1,
    'Social Service (evening attendance)': 2,
    'Agronomy': 3,
    'Communication Design': 4,
    'Veterinary Nursing': 5,
    'Informatics Engineering': 6,
    'Equinculture': 7,
    'Management': 8,
    'Social Service': 9,
    'Tourism': 10,
    'Nursing': 11,
    'Oral Hygiene': 12,
    'Advertising and Marketing Management': 13,
    'Journalism and Communication': 14,
    'Basic Education': 15,
    'Management (evening attendance)': 16
}
gender_map = {'Male': 0, 'Female': 1}
daytime_map = {'Daytime': 0, 'Evening': 1}

# Feature Vector
features = np.array([[
    course_map[course],
    gender_map[gender],
    daytime_map[daytime],
    admission_grade,
    special_needs,
    debtor,
    tuition_up_to_date,
    scholarship,
    age,
    sem1_grade,
    sem2_grade
]])

# Scaling the features
features_scaled = scaler.transform(features)

# Predict
if st.button('Predict'):
    prediction = model.predict(features_scaled)
    result = 'Dropout' if prediction[0] == 0 else 'Not Dropout'
    st.success(f'Student Status Prediction: {result}')

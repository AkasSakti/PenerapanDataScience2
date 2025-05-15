""# app.py
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

# Pilihan input dari user
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

# One-Hot Encoding (Reconstruction)
courses = [
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
]

daytimes = ['Daytime', 'Evening']
genders = ['Male', 'Female']

# Buat dummy dataframe
input_data = pd.DataFrame(0, index=[0], columns=[f'Course_{c}' for c in courses] + 
                          [f'Daytime_evening_attendance_{d}' for d in daytimes] + 
                          [f'Gender_{g}' for g in genders])

# Set nilai 1 untuk pilihan yang dipilih
input_data[f'Course_{course}'] = 1
input_data[f'Daytime_evening_attendance_{daytime}'] = 1
input_data[f'Gender_{gender}'] = 1

# Masukkan fitur numerik
input_data['Admission_grade'] = admission_grade
input_data['Educational_special_needs'] = special_needs
input_data['Debtor'] = debtor
input_data['Tuition_fees_up_to_date'] = tuition_up_to_date
input_data['Scholarship_holder'] = scholarship
input_data['Age_at_enrollment'] = age
input_data['Curricular_units_1st_sem_grade'] = sem1_grade
input_data['Curricular_units_2nd_sem_grade'] = sem2_grade

# Scaling the features
features_scaled = scaler.transform(input_data)

# Predict
if st.button('Predict'):
    prediction = model.predict(features_scaled)
    result = 'Dropout' if prediction[0] == 0 else 'Not Dropout'
    st.success(f'Student Status Prediction: {result}')
""

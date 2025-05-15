import streamlit as st
import joblib
import pandas as pd

# Load model, scaler, dan kolom terbaru dari hasil training di GitHub
model = joblib.load('model/random_forest_model.joblib')
scaler = joblib.load('model/scaler_model.joblib')
columns = joblib.load('model/columns.joblib')  # pastikan ini kolom dataset hasil training

st.title('Student Attrition Prediction App')
st.header('Input Student Information')

# Input user
course = st.text_input('Course (e.g., 171, 8014, 9003, etc.)', '171')
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

# Buat DataFrame kosong sesuai kolom hasil training
input_data = pd.DataFrame(0, index=[0], columns=columns)

# Isi nilai 1 untuk fitur kategori sesuai input user jika kolom ada
course_col = f'Course_{course}'
if course_col in input_data.columns:
    input_data[course_col] = 1

gender_col = f'Gender_{gender}'
if gender_col in input_data.columns:
    input_data[gender_col] = 1

daytime_col = f'Daytime_evening_attendance_{daytime}'
if daytime_col in input_data.columns:
    input_data[daytime_col] = 1

# Isi fitur numerik
for col, val in {
    'Admission_grade': admission_grade,
    'Educational_special_needs': special_needs,
    'Debtor': debtor,
    'Tuition_fees_up_to_date': tuition_up_to_date,
    'Scholarship_holder': scholarship,
    'Age_at_enrollment': age,
    'Curricular_units_1st_sem_grade': sem1_grade,
    'Curricular_units_2nd_sem_grade': sem2_grade,
}.items():
    if col in input_data.columns:
        input_data[col] = val

# Scale input data pakai scaler hasil training
features_scaled = scaler.transform(input_data)

# Predict saat tombol ditekan
if st.button('Predict'):
    prediction = model.predict(features_scaled)
    result = 'Dropout' if prediction[0] == 0 else 'Not Dropout'
    st.success(f'Student Status Prediction: {result}')

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from joblib import load

st.title('🎓 Student Status Prediction App')
st.write('Aplikasi prediksi status mahasiswa (Dropout, Graduate, Enrolled) menggunakan Random Forest')

# === [1] Load Pretrained Model ===
model_path = 'model/rf_model.joblib'
try:
    model = load(model_path)
    st.success(f'Model berhasil dimuat dari: {model_path}')
except Exception as e:
    st.error(f'Gagal memuat model: {e}')
    st.stop()

# === [2] Input Data untuk Prediksi ===
st.subheader('Input Data Mahasiswa untuk Prediksi')
features = {
    'Marital_status': st.selectbox('Marital Status', [0, 1, 2]),
    'Application_mode': st.number_input('Application Mode', min_value=0, max_value=20, value=0),
    'Course': st.number_input('Course', min_value=0, max_value=50, value=0),
    'Daytime_evening_attendance': st.selectbox('Daytime/Evening Attendance', [0, 1]),
    'Previous_qualification': st.number_input('Previous Qualification', min_value=0, max_value=10, value=0),
    'Previous_qualification_grade': st.number_input('Previous Qualification Grade', min_value=0.0, max_value=20.0, value=0.0),
    'Nacionality': st.number_input('Nacionality', min_value=0, max_value=100, value=0),
    'Mothers_qualification': st.number_input('Mothers Qualification', min_value=0, max_value=10, value=0),
    'Fathers_qualification': st.number_input('Fathers Qualification', min_value=0, max_value=10, value=0),
    'Mothers_occupation': st.number_input('Mothers Occupation', min_value=0, max_value=10, value=0),
    'Fathers_occupation': st.number_input('Fathers Occupation', min_value=0, max_value=10, value=0),
    'Displaced': st.selectbox('Displaced', [0, 1]),
    'Educational_special_needs': st.selectbox('Educational Special Needs', [0, 1]),
    'Debtor': st.selectbox('Debtor', [0, 1]),
    'Tuition_fees_up_to_date': st.selectbox('Tuition Fees Up to Date', [0, 1]),
    'Gender': st.selectbox('Gender', [0, 1]),
    'Scholarship_holder': st.selectbox('Scholarship Holder', [0, 1]),
    'International': st.selectbox('International', [0, 1])
}

# Konversi ke DataFrame
input_df = pd.DataFrame([features])

# === [3] Scaling Data ===
scaler = StandardScaler()
input_scaled = scaler.fit_transform(input_df)

# === [4] Prediksi ===
if st.button('Prediksi Status'):
    pred = model.predict(input_scaled)
    mapping = {0: 'Graduate', 1: 'Dropout', 2: 'Enrolled'}
    st.write(f'### Prediksi Status Mahasiswa: **{mapping[pred[0]]}**')

import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

# === [1] Title & Description ===
st.title('🎓 Student Status Prediction App')
st.write('Aplikasi prediksi status mahasiswa (Dropout, Graduate, Enrolled) menggunakan Random Forest')

# === [2] Load Model dan Scaler ===
model_path = 'model/rf_model.joblib'
scaler_path = 'model/scaler.joblib'

try:
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    st.success('Model dan Scaler berhasil dimuat!')
except Exception as e:
    st.error(f'Gagal memuat model atau scaler: {e}')
    st.stop()

# === [3] Input Data Mahasiswa ===
st.subheader('Input Data Mahasiswa')
features = {
    'Marital_status': st.selectbox('Marital Status', [0, 1, 2]),
    'Application_mode': st.number_input('Application Mode', min_value=0, max_value=20, value=0),
    'Application_order': st.number_input('Application Order', min_value=0, max_value=20, value=0),
    'Course': st.number_input('Course', min_value=0, max_value=10000, value=0),
    'Daytime_evening_attendance': st.selectbox('Daytime/Evening Attendance', [0, 1]),
    'Previous_qualification': st.number_input('Previous Qualification', min_value=0, max_value=10, value=0),
    'Previous_qualification_grade': st.number_input('Previous Qualification Grade', min_value=0.0, max_value=20.0, value=0.0),
    'Nacionality': st.number_input('Nacionality', min_value=0, max_value=300, value=0),
    'Mothers_qualification': st.number_input('Mothers Qualification', min_value=0, max_value=10, value=0),
    'Fathers_qualification': st.number_input('Fathers Qualification', min_value=0, max_value=10, value=0),
    'Mothers_occupation': st.number_input('Mothers Occupation', min_value=0, max_value=10, value=0),
    'Fathers_occupation': st.number_input('Fathers Occupation', min_value=0, max_value=10, value=0),
    'Admission_grade': st.number_input('Admission Grade', min_value=0.0, max_value=20.0, value=0.0),
    'Displaced': st.selectbox('Displaced', [0, 1]),
    'Educational_special_needs': st.selectbox('Educational Special Needs', [0, 1]),
    'Debtor': st.selectbox('Debtor', [0, 1]),
    'Tuition_fees_up_to_date': st.selectbox('Tuition Fees Up to Date', [0, 1]),
    'Gender': st.selectbox('Gender', [0, 1]),
    'Scholarship_holder': st.selectbox('Scholarship Holder', [0, 1]),
    'Age_at_enrollment': st.number_input('Age at Enrollment', min_value=0, max_value=100, value=18),
    'International': st.selectbox('International', [0, 1])
}

# Konversi ke DataFrame
input_df = pd.DataFrame([features])

# === [4] Scaling Data ===
try:
    input_scaled = scaler.transform(input_df)
except Exception as e:
    st.error(f'Error saat melakukan scaling data: {e}')
    st.stop()

# === [5] Prediksi ===
if st.button('Prediksi Status'):
    try:
        pred = model.predict(input_scaled)
        mapping = {0: 'Graduate', 1: 'Dropout', 2: 'Enrolled'}
        st.success(f'### Prediksi Status Mahasiswa: **{mapping[pred[0]]}**')
    except Exception as e:
        st.error(f'Gagal melakukan prediksi: {e}')

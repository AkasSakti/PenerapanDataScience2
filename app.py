import streamlit as st
import pandas as pd
from joblib import load

# Load data dan model
data = pd.read_csv("dataset/data_cleaned.csv")
model = load("model/random_forest_model.joblib")  # Contoh nama file model, sesuaikan dengan milikmu

category_mapping = {
    33: 'Biofuel Production Technologies',
    171: 'Animation and Multimedia Design',
    8014: 'Social Service (evening attendance)',
    9003: 'Agronomy',
    9070: 'Communication Design',
    9085: 'Veterinary Nursing',
    9119: 'Informatics Engineering',
    9130: 'Equinculture',
    9147: 'Management',
    9238: 'Social Service',
    9254: 'Tourism',
    9500: 'Nursing',
    9556: 'Oral Hygiene',
    9670: 'Advertising and Marketing Management',
    9773: 'Journalism and Communication',
    9853: 'Basic Education',
    9991: 'Management (evening attendance)'
}

data['Course_Label'] = data['Course'].replace(category_mapping)

if st.sidebar.selectbox("Choose a page", ["Dashboard", "Prediction"]) == "Prediction":
    st.title("Student Dropout Prediction")

    # Input user (contoh input, sesuaikan dengan fitur model)
    selected_course = st.selectbox('Select course', ['None'] + list(data['Course_Label'].unique()))
    selected_gender = st.selectbox('Select gender', ['None', 'Male', 'Female'])
    selected_attendance = st.selectbox('Select attendance time', ['None', 'Daytime', 'Evening'])
    selected_grade_1st = st.number_input('Enter 1st Semester Grade', min_value=0.0, max_value=100.0, value=75.0)
    selected_grade_2nd = st.number_input('Enter 2nd Semester Grade', min_value=0.0, max_value=100.0, value=75.0)

    # Convert inputs ke bentuk model input (contoh)
    course_code = None
    if selected_course != 'None':
        # mapping balik dari nama ke kode
        inv_map = {v: k for k, v in category_mapping.items()}
        course_code = inv_map.get(selected_course, 0)
    else:
        course_code = 0

    gender_code = 1 if selected_gender == 'Male' else 0 if selected_gender == 'Female' else -1
    attendance_code = 1 if selected_attendance == 'Daytime' else 0 if selected_attendance == 'Evening' else -1

    # Prepare fitur untuk prediksi (pastikan urutan fitur sesuai model)
    input_features = pd.DataFrame([{
        'Course': course_code,
        'Gender': gender_code,
        'Daytime_evening_attendance': attendance_code,
        'Curricular_units_1st_sem_grade': selected_grade_1st,
        'Curricular_units_2nd_sem_grade': selected_grade_2nd
    }])

    if st.button("Predict Dropout Status"):
        prediction = model.predict(input_features)[0]
        status_map = {0: "Dropout", 1: "Enrolled", 2: "Graduated"}
        st.success(f"Predicted status: {status_map.get(prediction, 'Unknown')}")

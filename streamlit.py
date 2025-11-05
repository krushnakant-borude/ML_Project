import streamlit as st
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

st.title("Student Exam Performance Indicator")
st.header("Student Exam Performance Prediction")

# Input widgets replacing your HTML form fields
gender = st.selectbox('Gender', ['male', 'female'], index=0)
ethnicity = st.selectbox('Race or Ethnicity', ['group A', 'group B', 'group C', 'group D', 'group E'], index=0)
parental_education = st.selectbox('Parental Level of Education', [
    "associate's degree", "bachelor's degree", "high school",
    "master's degree", "some college", "some high school"], index=0)
lunch = st.selectbox('Lunch Type', ['free/reduced', 'standard'], index=0)
test_prep = st.selectbox('Test Preparation Course', ['none', 'completed'], index=0)
writing_score = st.number_input('Writing Score out of 100', min_value=0.0, max_value=100.0, value=50.0)
reading_score = st.number_input('Reading Score out of 100', min_value=0.0, max_value=100.0, value=50.0)

# When user clicks Predict button
if st.button('Predict your Maths Score'):
    # Instantiate input data structure
    data = CustomData(
        gender=gender,
        race_ethnicity=ethnicity,
        parental_level_of_education=parental_education,
        lunch=lunch,
        test_preparation_course=test_prep,
        reading_score=reading_score,
        writing_score=writing_score
    )
    pred_df = data.get_data_as_data_frame()

    # Run prediction pipeline
    predict_pipeline = PredictPipeline()
    result = predict_pipeline.predict(pred_df)

    # Show result
    st.success(f'The prediction is: {result[0]}')

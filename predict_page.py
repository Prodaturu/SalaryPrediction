import streamlit as st

from config import COUNTRIES, EDUCATION_LEVELS
from salary_model import predict_salary


def show_predict_page():
    st.title("Software Developer Salary Prediction")
    st.write("### Information about you to predict the salary")

    country = st.selectbox("Country", COUNTRIES)
    education = st.selectbox("Educational Level", EDUCATION_LEVELS)
    experience = st.slider("Years of Experience", 0, 50, 3)

    ok = st.button("Calculate Salary")
    if ok:
        salary = predict_salary(country, education, experience)
        st.subheader(f"The estimated salary is ${salary:,.2f}")

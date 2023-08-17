import streamlit as st
import numpy as np
import pickle

def load_model():
    with open('saved_steps.pkl','rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data['model']
le_country = data['le_country']
le_education = data['le_education']

def show_predict_page():  # sourcery skip: use-named-expression
    st.title('software developer salary prediction')
    st.write('''### Information about you to predict the salary''')

    countries = {
        'United States of America',
        'United Kingdom of Great Britain and Northern Ireland',
        'Australia',
        'India',
        'Netherlands',
        'Germany',
        'Sweden',
        'France',
        'Spain',
        'Brazil',
        'Italy',
        'Canada',
        'Switzerland',
        'Poland'
    }

    education = {
        'Less than Bachelors',
        'Bachelors degree',
        'Masters degree',
        'Post graduate'
    }

    country = st.selectbox('Country',countries)
    education = st.selectbox('Educational Level',education)
    experience = st.slider('Years of Experience', 0, 50, 3)
    
    ok = st.button('Calculate Salary')
    if ok:
        X = np.array([[country, education, experience]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])
        X = X.astype(float)
        salary = regressor.predict(X)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")
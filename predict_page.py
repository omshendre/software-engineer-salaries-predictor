import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('model_saved.pkl', 'rb') as file:
        data = pickle.load(file)
    return data
data = load_model()
regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

def show_predict_page():
    st.title("Software Developer Salary Prediction")

    st.write("""### We need some information to predict the salary""")

    countries = (
        "United States of America",
        "India",
        "United Kingdom of Great Britain and Northern Ireland",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherlands",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
    )

    education_levels = (
        "Less than a Bachelores",
        "Bachelors",
        "Masters",
        "Post grad",
    )
    country = st.selectbox("Country", countries)
    education = st.selectbox("Education Level", education_levels)
    experience = st.slider("Years of Experience", 0, 50, 3)
    year  = st.selectbox("Year", [2021, 2022])
    
    ok = st.button("Calculate Salary")
    if ok:
        X = np.array([[country, education, experience, year]])
        X[:, 0] = le_country.transform(X[:, 0])

        # Check if label encoder has been loaded and fitted
        if le_education is not None:
            X[:, 1] = le_education.transform(X[:, 1])
        else:
            st.error("Label encoder not found or not fitted!")

        X = X.astype(float)
        salary = regressor.predict(X)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")

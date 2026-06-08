import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page


def main():
    st.set_page_config(page_title="Salary Prediction")
    page = st.sidebar.selectbox("Predict / Explore", ("Predict", "Explore"))

    if page == "Explore":
        show_explore_page()
    else:
        show_predict_page()


if __name__ == "__main__":
    main()

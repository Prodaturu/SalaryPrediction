import streamlit as st
import plotly.express as px

from salary_data import load_survey_data


@st.cache_data
def get_data():
    return load_survey_data()


def show_explore_page():
    st.title("Explore Software Engineer Salaries")
    st.write("### Stack Overflow Developer Survey")

    df = get_data()

    data = df["Country"].value_counts().reset_index()
    data.columns = ["Country", "count"]
    fig = px.pie(
        data_frame=data,
        names="Country",
        values="count",
        title="Number of data points from different countries",
    )
    st.plotly_chart(fig)

    st.write("### Mean salary v Country")
    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write("#### Mean salary based on Experience")
    data = df.groupby(["Experience"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def shorten_Categories(categories, cutoff):
    # sourcery skip: assign-if-exp, dict-comprehension, inline-immediately-returned-variable
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'other'
    return categorical_map

def experience_cleaner(value):
    if value == "More than 50 years":
        return 50
    elif value == "Less than 1 year":
        return 0.5
    return float(value)

def education_cleaner(education_level):
    if "Bachelor’s degree" in education_level:
        return 'Bachelors degree'
    if "Master’s degree" in education_level:
        return 'Masters degree'
    if "Professional degree" in education_level:
        return 'Post graduate'
    return 'Less than Bachelors'

@st.cache_data
def load_data():
    df = pd.read_csv('Datasets/survey_results_public.csv')
    df = df[['Country', 'EdLevel', 'YearsCodePro', 'Employment', 'ConvertedCompYearly']]
    df = df.rename({
        'EdLevel' : 'Education',
        'ConvertedCompYearly':'Salary',
        'YearsCodePro' : 'Experience'
        }, axis=1)
    df = df[df['Salary'].notnull()]
    df = df.dropna()
    df = df[df['Employment'] == 'Employed, full-time']
    df = df.drop('Employment', axis = 1)
    
    country_map = shorten_Categories(df.Country.value_counts(), 400)
    df['Country'] = df['Country'].map(country_map)
    df = df[df['Salary'] <= 600000] 
    df = df[df['Salary'] >= 10000]
    df = df[df['Country'] != 'Other']
    
    df['Experience'] = df['Experience'].apply(experience_cleaner)
    df['Education'] = df['Education'].apply(education_cleaner)
    return df

df = load_data()

def show_explore_page():
    st.title('Explore Software Engineer Salaries')
    st.write(
        '''
        ### StackOverflow Developer's Survey 2022
        ''')
    data = df['Country'].value_counts()

    fig1, ax1 = plt.subplots(figsize=(12, 6)) # Set the figure size
    wedges, texts, autotexts = ax1.pie(data, autopct="%1.1f%%",pctdistance=0.9, shadow=True, startangle=180)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Add a legend with labels
    ax1.legend(wedges, data.index, title="Countries", loc="center left", bbox_to_anchor=(1.05, 0.5), fontsize=8)

    plt.setp(autotexts, size=8, weight="bold")
    plt.tight_layout()

    st.write("""
            #### Number of Data from different countries
            """)
    st.pyplot(fig1)

    st.write("""
            ### Mean salary v Country
            """
            )

    data = df.groupby(['Country'])['Salary'].mean().sort_values(ascending = True)
    st.bar_chart(data)
    
    st.write(
    """
        #### Mean salary based on Experience
    """
    )

    data = df.groupby(['Experience'])['Salary'].mean().sort_values(ascending = True)
    st.line_chart(data)


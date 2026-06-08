import pandas as pd

from config import DATASET_PATH


SURVEY_COLUMNS = [
    "Country",
    "EdLevel",
    "YearsCodePro",
    "Employment",
    "ConvertedCompYearly",
]


def shorten_categories(categories, cutoff):
    return {
        category: category if count >= cutoff else "Other"
        for category, count in categories.items()
    }


def clean_experience(value):
    if value == "More than 50 years":
        return 50.0
    if value == "Less than 1 year":
        return 0.5
    return float(value)


def clean_education(education_level):
    if "Bachelor’s degree" in education_level:
        return "Bachelors degree"
    if "Master’s degree" in education_level:
        return "Masters degree"
    if "Professional degree" in education_level:
        return "Post graduate"
    return "Less than Bachelors"


def load_survey_data(dataset_path=DATASET_PATH):
    df = pd.read_csv(dataset_path)
    df = df[SURVEY_COLUMNS]
    df = df.rename(
        {
            "EdLevel": "Education",
            "ConvertedCompYearly": "Salary",
            "YearsCodePro": "Experience",
        },
        axis=1,
    )

    df = df[df["Salary"].notnull()]
    df = df.dropna()
    df = df[df["Employment"] == "Employed, full-time"]
    df = df.drop("Employment", axis=1)

    country_map = shorten_categories(df["Country"].value_counts(), 400)
    df["Country"] = df["Country"].map(country_map)
    df = df[(df["Salary"] <= 600000) & (df["Salary"] >= 10000)]
    df = df[df["Country"] != "Other"]

    df["Experience"] = df["Experience"].apply(clean_experience)
    df["Education"] = df["Education"].apply(clean_education)
    return df

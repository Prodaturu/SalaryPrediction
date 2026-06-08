from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATASET_PATH = BASE_DIR / "Datasets" / "survey_results_public.csv"
MODEL_PATH = BASE_DIR / "saved_steps.pkl"

COUNTRIES = (
    "United States of America",
    "United Kingdom of Great Britain and Northern Ireland",
    "Australia",
    "India",
    "Netherlands",
    "Germany",
    "Sweden",
    "France",
    "Spain",
    "Brazil",
    "Italy",
    "Canada",
    "Switzerland",
    "Poland",
)

EDUCATION_LEVELS = (
    "Less than Bachelors",
    "Bachelors degree",
    "Masters degree",
    "Post graduate",
)

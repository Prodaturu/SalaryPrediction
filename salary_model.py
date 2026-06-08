from functools import lru_cache
import pickle

import numpy as np

from config import MODEL_PATH


@lru_cache(maxsize=1)
def load_saved_steps():
    with MODEL_PATH.open("rb") as file:
        return pickle.load(file)


def predict_salary(country, education, experience):
    saved_steps = load_saved_steps()
    regressor = saved_steps["model"]
    country_encoder = saved_steps["le_country"]
    education_encoder = saved_steps["le_education"]

    features = np.array([[country, education, experience]])
    features[:, 0] = country_encoder.transform(features[:, 0])
    features[:, 1] = education_encoder.transform(features[:, 1])
    features = features.astype(float)

    return regressor.predict(features)[0]

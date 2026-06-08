import pandas as pd

from config import BASE_DIR, DATASET_PATH


ORIGINAL_DATASET_PATH = BASE_DIR / "Datasets" / "original_dataset.csv"
REQUIRED_COLUMNS = [
    "Age",
    "Country",
    "Employment",
    "EdLevel",
    "YearsCodePro",
    "Industry",
    "ConvertedCompYearly",
]


def compress_dataset(
    original_dataset_path=ORIGINAL_DATASET_PATH,
    output_dataset_path=DATASET_PATH,
):
    df = pd.read_csv(original_dataset_path)
    df = df[REQUIRED_COLUMNS]
    df.to_csv(output_dataset_path, index=False)


if __name__ == "__main__":
    compress_dataset()

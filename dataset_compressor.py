import pandas as pd

# Reading the original dataset
original_dataset_path = 'Datasets/original_dataset.csv'
df = pd.read_csv(original_dataset_path)

# Selecting the required columns
required_columns = ['Age', 'Country', 'Employment', 'EdLevel', 'YearsCodePro', 'Industry', 'ConvertedCompYearly']
df = df[required_columns]

# Saving the new dataset
new_dataset_path = 'Datasets/survey_results_public.csv'
df.to_csv(new_dataset_path, index=False)
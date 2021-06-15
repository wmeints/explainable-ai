import os
from pathlib import Path
import pandas as pd


root_folder = Path(os.path.dirname(os.path.dirname(__file__)))
output_folder = root_folder / 'data' / 'processed'
input_file = root_folder / 'data' / 'raw' / 'uci_creditcard_defaulters.csv'
output_file = root_folder / 'data' / 'processed' / 'uci_creditcard_defaulters.csv'

gender_mapping = {
    1: 'male',
    2: 'female'
}

education_mapping = {
    1: 'graduate',
    2: 'university',
    3: 'highschool',
    4: 'other'
}

marital_status_mapping = {
    1: 'married',
    2: 'single',
    3: 'other'
}

df_defaulters = pd.read_csv(input_file, sep=';')

# Several columns are categorical, so we need to encode those.
# This first step takes care of translating numbers into category values.
df_defaulters['GENDER'] = df_defaulters['GENDER'].map(gender_mapping)
df_defaulters['EDUCATION'] = df_defaulters['EDUCATION'].map(education_mapping)
df_defaulters['MARRIAGE'] = df_defaulters['MARRIAGE'].map(marital_status_mapping)

categorical_columns = [
    'GENDER',
    'EDUCATION',
    'MARRIAGE'
]

df_output = df_defaulters

# This step turns them into one-hot encoded dummy values so we can use them in 
# the random forest classifier.
for column in categorical_columns:
    df_column = pd.get_dummies(df_defaulters[column], prefix=column)
    df_output = pd.concat([df_output, df_column], axis=1)
    df_output = df_output.drop([column], axis=1)

# We store the output in the output folder as a complete set.
# Use the split-data.py script to create a test and training set.
os.makedirs(output_folder,exist_ok=True)
df_output.to_csv(output_file, index=False)
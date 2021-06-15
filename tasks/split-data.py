import os
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split


root_folder = Path(os.path.dirname(os.path.dirname(__file__)))
input_file = root_folder / 'data' / 'processed' / 'uci_creditcard_defaulters.csv'
training_file = root_folder / 'data' / 'processed' / 'train.csv'
test_file = root_folder / 'data' / 'processed' / 'test.csv'

df_defaulters = pd.read_csv(input_file)
df_train, df_test = train_test_split(df_defaulters, test_size=0.1, stratify=df_defaulters[['LABEL']])

df_train.to_csv(training_file, index=False)
df_test.to_csv(test_file, index=False)

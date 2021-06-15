import os
from pathlib import Path
import joblib
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_validate


root_folder = Path(os.path.dirname(os.path.dirname(__file__)))
training_data = root_folder / 'data' / 'processed' / 'train.csv'
model_folder = root_folder / 'models'  
model_file = model_folder / 'classifier.bin'

df = pd.read_csv(training_data)
x = df.drop(['LABEL'], axis=1)
y = df['LABEL']

model = RandomForestClassifier()
results = cross_validate(model, x, y, cv=5, return_estimator=True)

os.makedirs(model_folder, exist_ok=True)

best_estimator = results['estimator'][np.argmax(results['test_score'])]
joblib.dump(best_estimator, model_file)

print(f"Done training. Stored model with score: {np.max(results['test_score'])}")
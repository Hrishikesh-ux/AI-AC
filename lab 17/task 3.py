import pandas as pd
import numpy as np

data = {
    'patient_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'age': [35, 45, 50, 62, 28, 70, 40, 55, 30, 68],
    'blood_pressure': [120, None, 135, 140, 115, 150, 125, None, 118, 145],
    'heart_rate': [72, 80, 75, 90, None, 85, 78, 92, 70, 88],
    'height_cm': [175, 180, 165, 170, 190, 160, 178, 172, 185, 168],
    'gender': ['M', 'Male', 'F', 'Female', 'm', 'male', 'F', 'Male', 'female', 'M'],
    'diagnosis': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A']
}
df = pd.DataFrame(data)

print("--- Original DataFrame (First 5 Rows) ---")
print(df.head())
print("\nOriginal Missing Values:")
print(df.isnull().sum())
print("-" * 50)

df_cleaned = df.copy()

numeric_cols = ['blood_pressure', 'heart_rate']
for col in numeric_cols:
    col_mean = df_cleaned[col].mean()
    df_cleaned[col].fillna(col_mean, inplace=True)

df_cleaned['height_m'] = df_cleaned['height_cm'] / 100
df_cleaned.drop('height_cm', axis=1, inplace=True)

gender_mapping = {
    'M': 'Male',
    'm': 'Male',
    'Male': 'Male',
    'F': 'Female',
    'f': 'Female',
    'Female': 'Female',
    'male': 'Male',
    'female': 'Female'
}
df_cleaned['gender'] = df_cleaned['gender'].replace(gender_mapping)

df_cleaned.drop('patient_id', axis=1, inplace=True)

print("-" * 50)
print("--- Cleaned Healthcare Patient Records ---")
print(df_cleaned)
print("\nFinal Missing Values Check:")
print(df_cleaned.isnull().sum())
print("\nStandardized Gender Categories:")
print(df_cleaned['gender'].value_counts())
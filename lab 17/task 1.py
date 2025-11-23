import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {
    'employee_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy'],
    'salary': [60000.0, 75000.0, None, 90000.0, 55000.0, 110000.0, 65000.0, None, 80000.0, 70000.0],
    'department': ['HR', 'Sales', 'IT', 'human resources', 'HR', 'IT', 'Marketing', 'sales', 'IT', 'HR'],
    'job_role': ['Manager', 'Associate', 'Analyst', 'Director', 'Associate', 'Manager', 'Analyst', 'Associate', 'Analyst', 'Director'],
    'joining_date': ['2020-01-15', '15/05/2021', '2022/10/01', 'N/A', '2023-03-20', '2019-11-01', '2022-07-25', '2021-09-01', '2020/05/10', '2023-01-01']
}
df = pd.DataFrame(data)

print("--- Original DataFrame (First 5 Rows) ---")
print(df.head())
print("\nOriginal Data Types:")
print(df.dtypes)
print("-" * 50)

df_cleaned = df.copy()

df_cleaned['joining_date'] = pd.to_datetime(
    df_cleaned['joining_date'],
    errors='coerce',
    dayfirst=True
)

median_salary = df_cleaned['salary'].median()
df_cleaned['salary'].fillna(median_salary, inplace=True)

mode_joining_date = df_cleaned['joining_date'].mode()[0]
df_cleaned['joining_date'].fillna(mode_joining_date, inplace=True)

mode_department = df_cleaned['department'].mode()[0]
df_cleaned['department'].fillna(mode_department, inplace=True)

df_cleaned['department'] = df_cleaned['department'].str.lower().str.strip()

department_map = {
    'hr': 'HR',
    'human resources': 'HR',
    'sales': 'Sales',
    'it': 'IT',
    'marketing': 'Marketing'
}

df_cleaned['department'] = df_cleaned['department'].replace(department_map)

le = LabelEncoder()

df_cleaned['department_encoded'] = le.fit_transform(df_cleaned['department'])

df_cleaned['job_role_encoded'] = le.fit_transform(df_cleaned['job_role'])

print("-" * 50)
print("--- Cleaned DataFrame ---")
print(df_cleaned)
print("\nCleaned Data Types:")
print(df_cleaned.dtypes)
print("\nMissing Value Check:")
print(df_cleaned[['salary', 'department', 'joining_date']].isnull().sum())
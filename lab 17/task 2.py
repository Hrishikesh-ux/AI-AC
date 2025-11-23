import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np

data = {
    'transaction_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'product_name': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'transaction_date': ['01-01-2023', '2023/01/15', '2023/02/05', '03/10/2023', '4/1/2023', '2023-04-25', '2023-05-10', '05/25/2023', '06-05-2023', '06-20-2023'],
    'transaction_amount': [150.50, 75.25, -20.00, 100.00, 0.00, 300.75, 50.00, 125.00, 250.99, 175.50]
}
df = pd.DataFrame(data)

print("--- Original DataFrame (First 5 Rows) ---")
print(df.head())
print("-" * 50)

df_preprocessed = df.copy()

print("Step A: Converting transaction_date to datetime...")
df_preprocessed['transaction_date'] = pd.to_datetime(
    df_preprocessed['transaction_date'],
    errors='coerce',
    dayfirst=True
)

print("Step B: Creating 'Month-Year' column...")
df_preprocessed['Month-Year'] = df_preprocessed['transaction_date'].dt.to_period('M').astype(str)

print("Step C: Removing invalid transaction amounts (<= 0)...")
initial_rows = len(df_preprocessed)
df_preprocessed = df_preprocessed[df_preprocessed['transaction_amount'] > 0].reset_index(drop=True)
rows_removed = initial_rows - len(df_preprocessed)
print(f"Removed {rows_removed} rows with transaction_amount <= 0.")

print("Step D: Normalizing 'transaction_amount' using Min-Max Scaling...")
scaler = MinMaxScaler()

amount_to_scale = df_preprocessed[['transaction_amount']]

df_preprocessed['transaction_amount_normalized'] = scaler.fit_transform(amount_to_scale)

print("-" * 50)
print("--- Preprocessed DataFrame ---")
print(df_preprocessed)
print("\nFinal Data Types:")
print(df_preprocessed.dtypes)
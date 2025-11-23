import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
import numpy as np

# --- 1. Generate Sample Data ---
data = {
    'date': pd.to_datetime(['2025-10-01', '2025-10-02', '2025-10-03', '2025-10-04', '2025-10-05', '2025-10-06', '2025-10-07', '2025-10-08', '2025-10-09', '2025-10-10']),
    'stock_price': [100.5, 102.1, None, 105.0, 104.5, 106.2, 107.0, 108.5, None, 110.0],
    'volume': [100000, 110000, 105000, None, 120000, 130000, 125000, 140000, 135000, 150000],
    'sector': ['Tech', 'Finance', 'Tech', 'Energy', 'Tech', 'Finance', 'Tech', 'Energy', 'Finance', 'Tech'],
    'company_name': ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'B', 'A']
}
df_financial = pd.DataFrame(data).set_index('date').sort_index()

# --- 2. Data Preprocessing and Feature Engineering ---

df_fe = df_financial.copy()

# A. Handle missing values (Impute with Mean)
df_fe['stock_price'].fillna(df_fe['stock_price'].mean(), inplace=True)
df_fe['volume'].fillna(df_fe['volume'].mean(), inplace=True)

# B. Create new features: Moving Averages (7-day, 30-day)
df_fe['MA_7d'] = df_fe['stock_price'].rolling(window=7).mean()
df_fe['MA_30d'] = df_fe['stock_price'].rolling(window=30).mean()

# Fill NaN values created by rolling window with the series mean
df_fe['MA_7d'].fillna(df_fe['MA_7d'].mean(), inplace=True)
df_fe['MA_30d'].fillna(df_fe['MA_30d'].mean(), inplace=True)

# C. Normalize continuous variables (stock_price, volume, MAs) using StandardScaler
scaler = StandardScaler()
continuous_cols = ['stock_price', 'volume', 'MA_7d', 'MA_30d']
df_fe[continuous_cols] = scaler.fit_transform(df_fe[continuous_cols])

# D. Encode categorical columns (sector, company_name)
le_sector = LabelEncoder()
le_company = LabelEncoder()

df_fe['sector_encoded'] = le_sector.fit_transform(df_fe['sector'])
df_fe['company_encoded'] = le_company.fit_transform(df_fe['company_name'])

df_fe.drop(columns=['sector', 'company_name'], inplace=True)

# --- 3. Display Output and Assertions ---
print("\n" + "=" * 50)
print("--- Task 5: Financial Dataset Feature Engineering ---")
print("\nProcessed Data:")
print(df_fe)

# Assert Test Cases
assert not df_fe[['stock_price', 'volume']].isnull().any().any()
assert 'MA_7d' in df_fe.columns
assert len(df_fe.columns) == 6
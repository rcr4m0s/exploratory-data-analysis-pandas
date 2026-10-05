import numpy as np
import pandas as pd

data = {
    'User': ['Alex', 'Bob', 'Charlie', 'David'],
    'Age': [25, np.nan, 30, 22],
    'Score': [85, 90, np.nan, 78],
}

df = pd.DataFrame(data)

print('=== ORIGINAL DATAFRAME ===')
print(df)

print('\n=== MISSING VALUES COUNT ===')
print(df.isna().sum())

df['Age'] = df['Age'].fillna(df['Age'].mean())

print('\n=== AFTER FILLING AGE ===')
print(df)

clean_df = df.dropna()

print('\n=== FINAL CLEAN DATAFRAME ===')
print(clean_df)
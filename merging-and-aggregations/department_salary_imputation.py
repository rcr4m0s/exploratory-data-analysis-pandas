import pandas as pd
import numpy as np

# Data 1: Employees
emp = pd.DataFrame({
    'EmpID': ['E1', 'E2', 'E3', 'E4'],
    'Name': ['Dan', 'Ella', 'Faye', 'Gino'],
    'DeptID': ['D1', 'D1', 'D2', 'D2']
})

salaries = pd.DataFrame({
    'EmpID': ['E1', 'E2', 'E3', 'E4'],
    'Salary': [50000.0, np.nan, 60000.0, 55000.0]
})

median_value = salaries['Salary'].median()
salaries['Salary'] = salaries['Salary'].fillna(median_value)

merge_df = pd.merge(emp, salaries, on='EmpID', how='inner')

ave = merge_df.groupby('DeptID')['Salary'].mean().reset_index()

print("--- CLEANED EMPLOYEE DATA ---")
print(merge_df)
print("\n--- AVERAGE SALARY PER DEPT")
print(ave)


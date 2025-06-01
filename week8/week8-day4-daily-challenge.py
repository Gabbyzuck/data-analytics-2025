import zipfile
import os

data_zip = '/Users/gabby/Downloads/Data Science Job Salaries.zip' 
extract_dir = 'Data Science Job Salaries'

os.makedirs(extract_dir, exist_ok=True)
with zipfile.ZipFile(data_zip, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

#print(f"Extracted {data_zip} to {extract_dir}")

import pandas as pd

salaries = pd.read_csv('Data Science Job Salaries/ds_salaries.csv')
#print(salaries.head())

#print(salaries.dtypes)

salaries = salaries.drop_duplicates()
#print(salaries.drop_duplicates().sum())

import pandas as pf
missing_data = salaries.isnull()
#print(missing_data.head())

grouped_data = salaries.groupby('experience_level')['salary_in_usd'].agg(['mean', 'median'])
#print(grouped_data)

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10, 6))
plt.bar(grouped_data.index, grouped_data['mean'], color='skyblue', label='Mean Salary')
plt.xlabel('Experience Level')
plt.ylabel('Average Salary in USD')
plt.title('Average Salary by Experience Level')
plt.show()
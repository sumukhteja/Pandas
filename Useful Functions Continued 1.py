#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

# Create sample DataFrames
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [3, 4, 5], 'C': [7, 8, 9]})

# Merge the DataFrames based on column 'A'
merged = df1.merge(df2, on='A')
print("Merged DataFrame:")
print(merged)

# Create a pivot table based on 'A' and 'B' columns
pivot_table = merged.pivot_table(index='A', columns='B', values='C')
print("\nPivot Table:")
print(pivot_table)

# Stack the columns into rows, creating a multi-level index
stacked = pivot_table.stack()
print("\nStacked DataFrame:")
print(stacked)

# Unstack the rows into columns, creating a multi-level column index
unstacked = stacked.unstack()
print("\nUnstacked DataFrame:")
print(unstacked)

# Identify duplicate rows in the DataFrame
duplicates = merged.duplicated()
print("\nDuplicate Rows:")
print(duplicates)

# Remove duplicate rows from the DataFrame
deduplicated = merged.drop_duplicates()
print("\nDataFrame after removing duplicates:")
print(deduplicated)

# Compute pairwise correlation of columns
correlation = merged.corr()
print("\nCorrelation Matrix:")
print(correlation)

# Resample time series data based on a monthly frequency
timeseries = pd.date_range(start='1/1/2022', periods=12, freq='M')
df = pd.DataFrame({'Date': timeseries, 'Value': range(1, 13)})
resampled = df.resample('Q', on='Date').sum()
print("\nResampled Time Series Data:")
print(resampled)

# Compute rolling window calculations on time series data
rolling_mean = df['Value'].rolling(window=3).mean()
print("\nRolling Mean:")
print(rolling_mean)

# Apply a function to each group and return a DataFrame with transformed values aligned with the original DataFrame
grouped = df.groupby(df['Date'].dt.year)['Value']
transformed = grouped.transform(lambda x: x - x.mean())
print("\nTransformed DataFrame:")
print(transformed)


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a 5x5 DataFrame
data = np.random.randint(1, 10, size=(5, 5))
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E'])

# Get the dimensions (number of rows and columns) of the DataFrame
dimensions = df.shape
print("Dimensions (rows, columns):", dimensions)

# Get the column names of the DataFrame
columns = df.columns
print("Column names:", columns)

# Apply a function to each element or row/column of the DataFrame
def square(x):
    return x ** 2

df_applied = df.apply(square)
print("Applied function:\n", df_applied)

# Merge two DataFrames based on common columns
df2 = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                    'F': ['a', 'b', 'c', 'd', 'e']})

merged_df = df.merge(df2, on='A')
print("Merged DataFrame:\n", merged_df)

# Remove specified rows or columns from the DataFrame
df_dropped = df.drop(columns=['C', 'D'])
print("DataFrame with columns 'C' and 'D' dropped:\n", df_dropped)

# Group the DataFrame and apply aggregation functions
aggregated_df = df.groupby('A').agg({'B': 'sum', 'C': 'mean'})
print("Aggregated DataFrame:\n", aggregated_df)

# Create a pivot table
pivot_table = df.pivot_table(index='A', columns='B', values='C', aggfunc='mean')
print("Pivot table:\n", pivot_table)

# Count the occurrences of unique values in a column
value_counts = df['A'].value_counts()
print("Value counts:\n", value_counts)

# Create a basic plot
df.plot(kind='bar', x='A', y='B')
plt.show()


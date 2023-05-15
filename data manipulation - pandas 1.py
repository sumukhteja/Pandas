#!/usr/bin/env python
# coding: utf-8

# In[14]:


Pandas is a popular data manipulation and analysis library in Python. It provides powerful tools for working with
structured data, such as spreadsheets or SQL tables. Here's a brief introduction to some of the essential concepts
and operations in pandas:

Installation:
To use pandas, you need to install it first. You can install it via pip, the package installer for Python, by running
the following command:
pip install pandas

Importing pandas:
Once installed, you can import pandas into your Python script or notebook using the following line:

import pandas as pd
Data Structures:
Pandas introduces two primary data structures: Series and DataFrame.

Series is a one-dimensional array-like object that can hold any data type. It consists of an array of data and
an associated array of labels called the index. You can create a Series object as follows:

data = [10, 20, 30, 40, 50]
series = pd.Series(data)
DataFrame is a two-dimensional labeled data structure with columns of potentially different types. It is similar to a
spreadsheet or a SQL table. You can create a DataFrame using various methods, such as reading from a file, converting
from a NumPy array, or manually creating one. Here's an example:

data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

Reading and Writing Data:
Pandas provides functions to read and write data from various file formats, including CSV, Excel, SQL databases, and more.
Here's an example of reading a CSV file into a DataFrame:
df = pd.read_csv('data.csv')

To write a DataFrame to a file, you can use the to_csv() method:
df.to_csv('output.csv', index=False)  # Set index=False to exclude row numbers


BASIC OPERATIONS:

Inspecting data:
df.head(n): Returns the first n rows of the DataFrame.
df.tail(n): Returns the last n rows of the DataFrame.
df.info(): Provides a summary of the DataFrame, including the data types and number of non-null values in each column.
df.describe(): Generates descriptive statistics for numerical columns.

Accessing and selecting data:
df[column]: Returns a Series representing the specified column.
df[[column1, column2]]: Returns a DataFrame with the selected columns.
df.loc[row_label, column_label]: Accesses a specific element in the DataFrame using labels.
df.iloc[row_index, column_index]: Accesses a specific element in the DataFrame using integer-based indexing.

Filtering data:
df[condition]: Returns a DataFrame containing rows that satisfy the given condition.

Manipulating data:
df.drop(columns=[column1, column2]): Removes specified columns from the DataFrame.
df.rename(columns={'old_name': 'new_name'}): Renames columns.
df.sort_values(by='column'): Sorts the DataFrame by the values in the specified column.
df.groupby('column').agg(func): Groups the DataFrame by a column and applies an aggregation function (e.g., sum, mean)
to each group.

Handling missing data:
df.isnull(): Returns a DataFrame of the same shape as the original, indicating whether each value is missing or not.
df.dropna(): Drops rows with missing values.
df.fillna(value): Fills missing values with a specified value or method (e.g., mean, median).
    
Modifying data:
df['new_column'] = values: Adds a new column to the DataFrame with specified values.
df['column'].apply(function): Applies a function to each element in a column.
df['column'].map(dictionary): Maps values in a column to new values based on a dictionary.

Aggregating data:
df.groupby('column').agg({'column2': func1, 'column3': func2}): Groups the DataFrame by a column and applies different 
aggregation functions to different columns.

Merging and joining data:
pd.concat([df1, df2]): Concatenates DataFrames vertically (row-wise).
pd.merge(df1, df2, on='common_column'): Merges two DataFrames based on a common column.

Data visualization:
Pandas integrates with other libraries, such as Matplotlib and Seaborn, to create visualizations from DataFrame data.

More functions:
df.shape: Get the dimensions (number of rows and columns) of the DataFrame.
df.columns: Get the column names of the DataFrame.
df.apply(): Apply a function to each element or row/column of the DataFrame.
df.merge(): Merge two DataFrames based on common columns.
df.drop(): Remove specified rows or columns from the DataFrame.
df.groupby().agg(): 
df.pivot_table():
df.value_counts(): 
df.plot(): Create basic plots (line, bar, scatter, etc.) using Matplotlib or a backend library like Seaborn.

Reshaping and Pivoting Data:
df.melt(): Unpivots a DataFrame from wide format to long format.
df.pivot(): Pivots a DataFrame from long format to wide format based on unique values in a column.

Handling Categorical Data:
df.get_dummies(): Converts categorical variables into dummy/indicator variables.
df.astype('category'): Converts a column to the category data type, which can be useful for memory optimization and performing categorical operations.

String Operations:
df.str.contains(): Checks if each string element in a column contains a specified substring.
df.str.extract(): Extracts matching patterns from string columns using regular expressions.
df.str.replace(): Replaces substrings in a string column with a specified value.

Time Series Analysis:
pd.to_datetime(): Converts a column to the datetime data type for time series analysis.
df.resample(): Resamples time series data based on a specified frequency (e.g., daily, monthly).
df.rolling(): Computes rolling window calculations on time series data (e.g., rolling mean, rolling sum).

Handling Duplicate Data:
df.duplicated(): Identifies duplicate rows in a DataFrame.
df.drop_duplicates(): Removes duplicate rows from a DataFrame.

Advanced Indexing and Selection:
df.set_index(): Sets one or more columns as the index of the DataFrame.
df.reset_index(): Resets the index of the DataFrame to the default integer index.
df.nlargest(): Returns the n largest values from a column in a DataFrame.
df.nsmallest(): Returns the n smallest values from a column in a DataFrame.
    
Useful Functions:
df.applymap(function): Applies a function element-wise to a DataFrame.
df.sample(n): Returns a random sample of n rows from the DataFrame.
df.dtypes: Returns the data types of each column in the DataFrame.
df.dropna(axis): Drops missing values along a specified axis (rows or columns).
df.pivot_table(): Creates a spreadsheet-style pivot table based on the DataFrame.
df.explode(column): Expands a column with lists or arrays into multiple rows.
df.at[row, column]: Accesses a scalar value in the DataFrame using label-based indexing.
df.iat[row, column]: Accesses a scalar value in the DataFrame using integer-based indexing.
df.memory_usage(): Returns the memory usage of each column in the DataFrame.
df.replace(to_replace, value): Replaces specified values in the DataFrame with a new value.
df.dropna(subset=[column]): Drops rows with missing values in a specific column.
df.round(decimals): Rounds the values in the DataFrame to the specified number of decimals.
df.to_excel(): Writes the DataFrame to an Excel file.
df.to_sql(): Writes the DataFrame to a SQL database.

import pandas as pd

# Create a sample DataFrame
data = {'Name': ['John', 'Alice', 'Bob', 'Charlie', 'Emma'],
        'Age': [25, 30, 35, 28, 32],
        'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney'],
        'Salary': [50000, 60000, 55000, 48000, 52000]}
df = pd.DataFrame(data)

# Display the first 3 rows of the DataFrame
print(df.head(3))

# Display the last 2 rows of the DataFrame
print(df.tail(2))

# Display the summary information of the DataFrame
print(df.info())

# Generate descriptive statistics for numerical columns
print(df.describe())


# Access a specific column and return it as a Series
name_series = df['Name']
print(name_series)

# Access specific columns and return them as a DataFrame
columns = ['Name', 'Age']
selected_columns = df[columns]
print(selected_columns)

# Access a specific element using labels with loc
element_loc = df.loc[2, 'City']
print(element_loc)

# Access a specific element using integer-based indexing with iloc
element_iloc = df.iloc[3, 2]
print(element_iloc)
# In[5]:


# Filter rows based on a condition
filtered_df = df[df['Age'] > 30]
print(filtered_df)


# In[6]:


# Remove specified columns from the DataFrame
df = df.drop(columns=['City', 'Salary'])
print(df)

# Rename columns in the DataFrame
df = df.rename(columns={'Name': 'Full Name', 'Age': 'Years'})
print(df)

# Sort the DataFrame by the values in the 'Years' column
df = df.sort_values(by='Years')
print(df)

# Group the DataFrame by the 'Years' column and calculate the mean age for each group
grouped_df = df.groupby('Years').agg({'Full Name': 'count', 'Years': 'mean'})
print(grouped_df)


# In[7]:


import pandas as pd
import numpy as np

# Create a sample DataFrame with missing values
data = {'Name': ['John', np.nan, 'Bob', 'Charlie', 'Emma'],
        'Age': [25, 30, np.nan, 28, 32],
        'City': ['New York', 'London', 'Paris', np.nan, 'Sydney'],
        'Salary': [50000, 60000, 55000, 48000, np.nan]}
df = pd.DataFrame(data)

# Check for missing values in the DataFrame
missing_values = df.isnull()
print(missing_values)

# Drop rows with missing values
df_dropped = df.dropna()
print(df_dropped)

# Fill missing values with a specified value or method
df_filled = df.fillna(value=0)  # Fill with a specific value, such as 0
print(df_filled)

mean_age = df['Age'].mean()
df_filled_mean = df.fillna(value={'Age': mean_age})  # Fill missing values in 'Age' column with mean
print(df_filled_mean)


# In[ ]:


# Add a new column to the DataFrame with specified values
new_column_values = [True, False, True, False, True]
df['Is_Employed'] = new_column_values
print(df)

# Apply a function to each element in a column
def multiply_by_two(x):
    return x * 2

df['Age_Doubled'] = df['Age'].apply(multiply_by_two)
print(df)

# Map values in a column to new values based on a dictionary
city_mapping = {'New York': 'USA', 'London': 'UK', 'Paris': 'France', 'Tokyo': 'Japan', 'Sydney': 'Australia'}
df['Country'] = df['City'].map(city_mapping)
print(df)


# In[8]:


# Group the DataFrame by the 'City' column and apply different aggregation functions to different columns
aggregated_df = df.groupby('City').agg({'Age': 'mean', 'Salary': 'sum'})
print(aggregated_df)


# In[10]:


import pandas as pd

# Create two sample DataFrames
data1 = {'Name': ['John', 'Alice', 'Bob'],
         'Age': [25, 30, 35],
         'City': ['New York', 'London', 'Paris']}
df1 = pd.DataFrame(data1)

data2 = {'Name': ['Charlie', 'Emma'],
         'Salary': [48000, 52000],
         'City': ['Tokyo', 'Sydney']}
df2 = pd.DataFrame(data2)

# Concatenate DataFrames vertically (row-wise)
concatenated_df = pd.concat([df1, df2])
print(concatenated_df)

# Merge DataFrames based on a common column
merged_df = pd.merge(df1, df2, on='City')
print(merged_df)


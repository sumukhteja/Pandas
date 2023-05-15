#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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


# In[1]:


import pandas as pd

# Create a sample DataFrame
data = {
    'ID': [1, 2, 3],
    'Name': ['John', 'Alice', 'Bob'],
    'Math': [80, 90, 75],
    'Science': [85, 92, 88],
    'English': [78, 80, 82]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

melted_df = df.melt(id_vars=['ID', 'Name'], var_name='Subject', value_name='Score')
print("\nUnpivoted DataFrame:")
print(melted_df)

pivoted_df = melted_df.pivot(index='ID', columns='Subject', values='Score')
print("\nPivoted DataFrame:")
print(pivoted_df)


# In[2]:


import pandas as pd

# Create a sample DataFrame
data = {'ID': [1, 2, 3, 4, 5],
        'Name': ['John', 'Alice', 'Bob', 'Jane', 'Mike'],
        'Grade': ['A', 'B', 'A', 'C', 'B']}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Convert 'Grade' column to categorical data type
df['Grade'] = df['Grade'].astype('category')

print("\nDataFrame with Categorical Data:")
print(df)

# Create dummy variables for 'Grade' column
dummy_df = pd.get_dummies(df['Grade'], prefix='Grade')

print("\nDataFrame with Dummy Variables:")
df = pd.concat([df, dummy_df], axis=1)
print(df)


# In[3]:


import pandas as pd

# Create a sample DataFrame
data = {'Name': ['John Doe', 'Alice Smith', 'Bob Johnson', 'Jane Williams'],
        'Email': ['john.doe@example.com', 'alice.smith@example.com', 'bob.johnson@example.com', 'jane.williams@example.com']}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Check if 'Name' column contains a specified substring
contains_smith = df['Name'].str.contains('Smith')

print("\nChecking if 'Name' column contains 'Smith':")
print(contains_smith)

# Extract first names from 'Name' column using regular expressions
first_names = df['Name'].str.extract(r'(\w+)')

print("\nExtracting first names from 'Name' column:")
print(first_names)

# Replace 'example.com' in 'Email' column with 'gmail.com'
replaced_emails = df['Email'].str.replace('example.com', 'gmail.com')

print("\nReplacing 'example.com' with 'gmail.com' in 'Email' column:")
print(replaced_emails)


# In[4]:


import pandas as pd

# Create a sample DataFrame with a datetime column
data = {'Date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04'],
        'Value': [10, 15, 20, 25]}
df = pd.DataFrame(data)

# Convert 'Date' column to datetime data type
df['Date'] = pd.to_datetime(df['Date'])

print("Original DataFrame:")
print(df)

# Resample the DataFrame to monthly frequency
df_resampled = df.resample('M', on='Date').sum()

print("\nResampled DataFrame (monthly frequency):")
print(df_resampled)

# Perform rolling mean calculation on 'Value' column with a window size of 2
rolling_mean = df['Value'].rolling(window=2).mean()

print("\nRolling mean calculation (window size = 2):")
print(rolling_mean)


# In[5]:


import pandas as pd

# Create a sample DataFrame with duplicate rows
data = {'Column1': ['A', 'B', 'A', 'C', 'B'],
        'Column2': [1, 2, 1, 3, 2]}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Identify duplicate rows in the DataFrame
duplicates = df.duplicated()

print("\nDuplicate rows:")
print(duplicates)

# Remove duplicate rows from the DataFrame
df_no_duplicates = df.drop_duplicates()

print("\nDataFrame after removing duplicates:")
print(df_no_duplicates)


# In[7]:


import pandas as pd

# Create a sample DataFrame
data = {'Column1': ['A', 'B', 'C', 'D'],
        'Column2': [10, 20, 30, 40]}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Set 'Column1' as the index of the DataFrame
df_set_index = df.set_index('Column1')

print("\nDataFrame with 'Column1' as index:")
print(df_set_index)

# Reset the index of the DataFrame
df_reset_index = df_set_index.reset_index()

print("\nDataFrame with reset index:")
print(df_reset_index)

# Get the 2 largest values from 'Column2'
df_largest = df.nlargest(2, 'Column2')

print("\n2 largest values from 'Column2':")
print(df_largest)

# Get the 2 smallest values from 'Column2'
df_smallest = df.nsmallest(2, 'Column2')

print("\n2 smallest values from 'Column2':")
print(df_smallest)


# In[11]:


import pandas as pd
import os
import sqlite3

# Sample DataFrame creation
data = {
    'Name': ['John', 'Emily', 'Michael', 'Jessica'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'London', 'Paris', 'Sydney']
}

df = pd.DataFrame(data)

# Writing DataFrame to an Excel file
df.to_excel('output.xlsx', index=False)

current_directory = os.getcwd()
excel_file_path = os.path.join(current_directory, 'output.xlsx')
print("Excel file saved at:", excel_file_path)


# Writing DataFrame to a SQL database (using SQLite in this example)
#conn = sqlite3.connect('sample.db')
#df.to_sql('sample_table', conn, index=False, if_exists='replace')
#conn.close()


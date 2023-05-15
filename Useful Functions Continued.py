#!/usr/bin/env python
# coding: utf-8

# In[ ]:


df.to_excel(): Writes the DataFrame to an Excel file.
df.to_sql(): Writes the DataFrame to a SQL database.
df.sample(n): Returns a random sample of n rows from the DataFrame.
df.explode(column): Expands a column with lists or arrays into multiple rows.
df.at[row, column]: Accesses a scalar value in the DataFrame using label-based indexing.
df.iat[row, column]: Accesses a scalar value in the DataFrame using integer-based indexing.
df.memory_usage(): Returns the memory usage of each column in the DataFrame.
df.replace(to_replace, value): Replaces specified values in the DataFrame with a new value.
df.dropna(subset=[column]): Drops rows with missing values in a specific column.
df.round(decimals): Rounds the values in the DataFrame to the specified number of decimals.
df.nunique(): Returns the number of unique values in each column of the DataFrame.
df.value_counts(): Returns the count of unique values in a column.
df.cumsum(): Computes the cumulative sum of values in each column.
df.cumprod(): Computes the cumulative product of values in each column.
df.cummax(): Computes the cumulative maximum value in each column.
df.cummin(): Computes the cumulative minimum value in each column.
df.melt(): Unpivots a DataFrame from wide format to long format.
df.pivot(): Pivots a DataFrame from long format to wide format based on unique values in a column.
df.iterrows(): Iterates over the rows of the DataFrame as (index, Series) pairs.
df.itertuples(): Iterates over the rows of the DataFrame as namedtuples.
df.style: Provides styling options to enhance the visual representation of the DataFrame.


# In[ ]:


import pandas as pd

# Sample DataFrame creation
data = {
    'Name': ['John', 'Emily', 'Michael', 'Jessica'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'London', 'Paris', 'Sydney']
}

df = pd.DataFrame(data)

# Writing DataFrame to an Excel file
output_path = 'output.xlsx'
df.to_excel(output_path, index=False)

# Print output path for Excel file
print("DataFrame has been written to the following Excel file:")
print(output_path)

# Writing DataFrame to a SQL database (Oracle in this example)
import cx_Oracle

dsn = cx_Oracle.makedsn('hostname', 'port', service_name='service_name')
conn = cx_Oracle.connect('username', 'password', dsn=dsn)

cursor = conn.cursor()
cursor.execute('CREATE TABLE sample_table (name VARCHAR2(50), age NUMBER, city VARCHAR2(50))')

for index, row in df.iterrows():
    cursor.execute('INSERT INTO sample_table VALUES (:1, :2, :3)',
                   (row['Name'], row['Age'], row['City']))

conn.commit()
conn.close()

# Print output path for Oracle database
print("Data has been written to the Oracle database.")


# In[6]:


import pandas as pd

# Sample DataFrame creation
data = {
    'Name': ['John', 'Emily', 'Michael', 'Jessica'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'London', 'Paris', 'Sydney']
}

df = pd.DataFrame(data)

# Returning a random sample of n rows from the DataFrame
n = 2
sample = df.sample(n)
print(f"Random sample of {n} rows:\n{sample}")

# Expanding a column with lists or arrays into multiple rows
data = {'Name': ['John', 'Emily', 'Michael'], 'Hobbies': [['Reading', 'Cooking'], ['Sports'], ['Painting', 'Music']]}
df_expanded = pd.DataFrame(data)
expanded = df_expanded.explode('Hobbies')
print("\nExpanded DataFrame:")
print(expanded)

# Accessing a scalar value in the DataFrame using label-based indexing
value = df.at[1, 'Age']
print(f"\nValue at row 1, column 'Age': {value}")

# Accessing a scalar value in the DataFrame using integer-based indexing
value = df.iat[2, 0]
print(f"\nValue at row 2, column 0: {value}")

# Returning the memory usage of each column in the DataFrame
memory_usage = df.memory_usage()
print("\nMemory usage of each column:")
print(memory_usage)

# Replacing specified values in the DataFrame with a new value
df_replaced = df.replace('John', 'Jonathan')
print("\nDataFrame with replaced values:")
print(df_replaced)

# Dropping rows with missing values in a specific column
column = 'City'
df_dropped = df.dropna(subset=[column])
print(f"\nDataFrame after dropping rows with missing values in column '{column}':")
print(df_dropped)

# Rounding the values in the DataFrame to the specified number of decimals
decimals = 1
df_rounded = df.round(decimals)
print(f"\nDataFrame with rounded values to {decimals} decimal places:")
print(df_rounded)

# Returning the number of unique values in each column of the DataFrame
n_unique = df.nunique()
print("\nNumber of unique values in each column:")
print(n_unique)

# Returning the count of unique values in a column
value_counts = df['City'].value_counts()
print("\nCount of unique values in the 'City' column:")
print(value_counts)

# Computing the cumulative sum of values in each column
cumulative_sum = df.cumsum()
print("\nCumulative sum of values in each column:")
print(cumulative_sum)

# Computing the cumulative product of values in each numeric column
numeric_columns = df.select_dtypes(include=[int, float]).columns
cumulative_product = df[numeric_columns].cumprod()
print("\nCumulative product of values in each numeric column:")
print(cumulative_product)

# Computing the cumulative maximum value in each column
cumulative_max = df.cummax()
print("\nCumulative maximum value in each column:")
print(cumulative_max)

# Computing the cumulative minimum value in each column
cumulative_min = df.cummin()
print("\nCumulative minimum value in each column:")
print(cumulative_min)


# Unpivoting the DataFrame from wide format to long format using melt()
melted = df.melt(id_vars='Name', value_vars=['Age', 'City'], var_name='Attribute', value_name='Value')
print("\nUnpivoted DataFrame using melt():")
print(melted)

# Pivoting the DataFrame from long format to wide format using pivot()
pivoted = melted.pivot(index='Name', columns='Attribute', values='Value')
print("\nPivoted DataFrame using pivot():")
print(pivoted)

# Iterating over the rows of the DataFrame using iterrows()
print("\nIterating over rows using iterrows():")
for index, row in df.iterrows():
    print(f"Index: {index}, Row: {row}")

# Iterating over the rows of the DataFrame as namedtuples using itertuples()
print("\nIterating over rows as namedtuples using itertuples():")
for row in df.itertuples():
    print(row)

# Styling the DataFrame using style
styled_df = df.style.highlight_max(axis=0).highlight_min(axis=0)

# Displaying the styled DataFrame
styled_df


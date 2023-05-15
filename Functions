Reading a CSV file into a DataFrame:
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

Useful Functions Continued:
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
df.merge(): Merges two DataFrames based on common columns or indexes.
df.pivot_table(): Creates a spreadsheet-style pivot table based on the DataFrame.
df.stack(): Pivots columns into rows, creating a multi-level index.
df.unstack(): Pivots rows into columns, creating a multi-level column index.
df.duplicated(): Identifies duplicate rows in a DataFrame.
df.drop_duplicates(): Removes duplicate rows from a DataFrame.
df.corr(): Computes pairwise correlation of columns, indicating the strength and direction of the relationship between variables.
df.resample(): Resamples time series data based on a specified frequency (e.g., daily, monthly).
df.rolling(): Computes rolling window calculations on time series data (e.g., rolling mean, rolling sum).
df.groupby().transform(): Applies a function to each group and returns a DataFrame with the transformed values aligned with the original DataFrame.

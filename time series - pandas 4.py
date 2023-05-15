#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import numpy as np

# Create a sample sales DataFrame
np.random.seed(0)
dates = pd.date_range('2023-01-01', periods=100, freq='D')
sales = np.random.randint(100, 1000, size=100)
df = pd.DataFrame({'Date': dates, 'Sales': sales})

#Handling Date/Time Components:
#Pandas provides convenient functions to extract date/time components from a DateTime column.
#For example, to extract the year, month, and day from the "Date" column, we can use the following code:
    
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
print(df[['Date', 'Year', 'Month', 'Day']])

#Resampling:
#Resampling involves changing the frequency of the time series data. For example, to resample the daily
#sales data to a monthly frequency, we can use the resample() function:
df_monthly = df.resample('M', on='Date').sum()

#Rolling Window Calculations:
#Rolling window calculations involve applying a function to a sliding window of a specified size over the
#time series data. For example, to calculate the rolling average of sales over a 7-day window, we can use
#the rolling() function:
df['Rolling_Average'] = df['Sales'].rolling(window=7).mean()

#Time-based Indexing:
#To make time-based analysis more convenient, we can set the "Date" column as the DataFrame's index using
#the set_index() function:
df = df.set_index('Date')


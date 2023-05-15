#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import yfinance as yf

# Define the stock symbol and the time range for data retrieval
stock_symbol = "AAPL"
start_date = "2022-01-01"
end_date = "2022-12-31"

# Fetch the stock data from Yahoo Finance
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Display the first few rows of the DataFrame (rounded to 2 decimal places)
print("First few rows of the stock data:\n", stock_data.head().round(2), "\n")

# Display the last few rows of the DataFrame (rounded to 2 decimal places)
print("Last few rows of the stock data:\n", stock_data.tail().round(2), "\n")

# Get a summary of the DataFrame, including data types and non-null values
print("Summary of the stock data:\n")
print(stock_data.info(), "\n")

# Generate descriptive statistics for numerical columns (rounded to 2 decimal places)
print("Descriptive statistics of the stock data:\n")
print(stock_data.describe().round(2), "\n")

# Access specific columns
print("Close price:\n", stock_data["Close"].round(2), "\n")
print("Open, High, Low, Close prices:\n", stock_data[["Open", "High", "Low", "Close"]].round(2), "\n")

# Access a specific element using labels
print("Close price on 2022-01-03:\n", stock_data.loc["2022-01-03", "Close"].round(2), "\n")

# Access a specific element using integer-based indexing
print("Close price on the first day:\n", stock_data.iloc[0, 3].round(2), "\n")

# Filter data based on a condition
filtered_data = stock_data[stock_data["Volume"] > 1000000]
print("Filtered stock data:\n", filtered_data.round(2), "\n")

# Add a new column
stock_data["DailyReturn"] = stock_data["Close"].pct_change().round(2)
print("Daily returns:\n", stock_data["DailyReturn"], "\n")

# Group data by a column and apply an aggregation function (e.g., mean)
grouped_data = stock_data.groupby(pd.Grouper(freq="M")).mean().round(2)
print("Monthly average:\n", grouped_data, "\n")


# In[7]:


import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Define the stock symbol and the time range for data retrieval
stock_symbol = "AAPL"
start_date = "2022-01-01"
end_date = "2022-12-31"

# Fetch the stock data from Yahoo Finance
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Plotting the closing prices
plt.figure(figsize=(12, 6))
plt.plot(stock_data.index, stock_data['Close'], color='b')
plt.title("Stock Closing Prices")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.grid(True)
plt.show()


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np

# Create a sample sales DataFrame
np.random.seed(0)
dates = pd.date_range('2023-01-01', periods=100, freq='D')
sales = np.random.randint(100, 1000, size=100)
df = pd.DataFrame({'Date': dates, 'Sales': sales})

summary = df.describe()
print(summary)

correlation = df.corr()
print(correlation)

df['Sales'].hist()
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()


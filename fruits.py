#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
import pandas as pd


# In[19]:


df = pd.read_csv("C:\\data sets\\fruits.csv")
print(df)

df1 = df
df2 = df
df3 =df


# In[20]:


df_Quantity = df1.groupby(['Category'], as_index = False)['Quantity'].sum()

df1.groupby(['Category'])['Quantity'].sum().plot.bar()


# In[21]:


df_Price = df2.groupby(['Category'])['Price'].sum()
df_Price

df2.groupby(['Category'])['Price'].sum().plot.bar()


# In[22]:


df_Mix = df3.groupby(['Category'])['Quantity', 'Price'].sum()
df_Mix
df3.groupby(['Category'])['Quantity', 'Price'].sum().plot.line()


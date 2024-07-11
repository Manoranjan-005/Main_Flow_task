#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
data=pd.read_csv("C:\\Users\\manor\\OneDrive\\Documents\\EXCEL TASK-2.csv")
print(type(data))


# In[5]:


data.info


# In[6]:


data.describe()


# In[8]:


data=data.drop_duplicates()
data


# In[9]:


data.isnull()


# In[12]:


data.isnull().sum()


# In[14]:


data.notnull()


# In[15]:


data.isnull().sum().sum()


# In[16]:


data2=data.fillna(value=0)
data2


# In[17]:


data3=data.fillna(method="pad")
data3


# In[18]:


# filling the null value with the next value 
data4=data.fillna(method='bfill')
data4


# In[19]:


import numpy as np
from scipy import stats


# In[20]:


#detect the outliers using IQR
data2.columns


# In[21]:


data2.drop(['NAME'],axis=1,inplace=True)
data2


# In[25]:


Q1=data2.quantile(0.25)
Q3=data2.quantile(0.75)
IQR=Q3-Q1
print(IQR)


# In[26]:


data2=data2[~((data2<(Q1-1.5*IQR))|(data2>(Q3+1.5*IQR))).any(axis=1)]
data2


# In[27]:


data2.describe()


# In[ ]:





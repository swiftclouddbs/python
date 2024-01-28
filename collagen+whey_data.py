#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas pd


# In[13]:


import pandas as pd


# In[18]:


data = pd.read_csv("/home/dba/health/Collagen+Whey.csv")
data.set_index('Amino').plot.bar(rot=45, title='Collagen vs. Whey', figsize=(15,10), fontsize=12)


# In[15]:





# In[11]:





# In[ ]:





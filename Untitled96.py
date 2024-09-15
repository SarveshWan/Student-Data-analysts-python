#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df=pd.read_csv("DATA.csv.zip")


# In[4]:


df


# In[5]:


df.info()


# In[7]:


df.dtypes


# In[8]:


df.head()


# In[ ]:


# Drop the unnamed: 0 column
df = df.drop(['Unnamed: 0'],axis=1)


# In[12]:


df.head()


# # Distribution of Gender

# In[21]:


plt.figure(figsize=(5,5))
ad=sns.countplot(data=df,x='Gender')
ad.bar_label(ad.containers[0])
plt.title("Countplot of Gender")
plt.show()


# In[22]:


# from the above chart we have to analysed that:
# the number of female in the data is more than the number of males


# # Relationship between parant education and score

# In[25]:


gb = df.groupby('ParentEduc').agg({'MathScore':'mean','ReadingScore':'mean','WritingScore':'mean'})


# In[26]:


gb


# In[30]:


plt.figure(figsize=(4,4))
sns.heatmap(gb,annot=True)
plt.show()


# In[31]:


# from the above chart we have analyszed that:
# the paranteducation is heavly matter for scoring


# # Relationship between Weekly study hours and score

# In[39]:


gb1=df.groupby("WklyStudyHours").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})


# In[40]:


gb1


# In[45]:


plt.figure(figsize=(5,5))
ad=sns.heatmap(gb1,annot=True)
plt.show()


# In[46]:


# from the obove table we are anlysis that:
# weeklystudyhour impact is niglegible to score


# # Relationship between parant marital status and score

# In[48]:


gb2=df.groupby('ParentMaritalStatus').agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})


# In[50]:


gb2


# In[56]:


plt.figure(figsize=(4,4))
sns.heatmap(gb2,annot=True)
plt.show()


# In[57]:


# from the obove table we are analyzed that:
# the parant marital status neglegible impact for scoring


# In[59]:


sns.boxplot(data=df, x='MathScore')
plt.show()


# In[60]:


sns.boxplot(data=df, x='ReadingScore')
plt.show()


# In[61]:


sns.boxplot(data=df, x='WritingScore')
plt.show()


# In[62]:


df['EthnicGroup'].unique()


# In[81]:


groupA = df.loc[(df['EthnicGroup'] == 'group A')].count()
groupB = df.loc[(df['EthnicGroup'] == 'group B')].count()
groupC = df.loc[(df['EthnicGroup'] == 'group C')].count()
groupD = df.loc[(df['EthnicGroup'] == 'group D')].count()
groupE = df.loc[(df['EthnicGroup'] == 'group E')].count()

l= ['group A', 'group B', 'group C', 'group D', 'group E']

mlist=[groupA['EthnicGroup'], groupB['EthnicGroup'], groupC['EthnicGroup'], groupD['EthnicGroup'], groupE['EthnicGroup']]

plt.pie(mlist, labels=l, autopct ='%1.2f%%')
plt.show()



# In[84]:


plt.figure(figsize=(5,5))
ad=sns.countplot(data=df, x='EthnicGroup')
ad.bar_label(ad.containers[0])
plt.show()


# In[ ]:





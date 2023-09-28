#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import libraries
import pandas as pd
from bs4 import BeautifulSoup
import requests


# In[2]:


# get url
url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
page = requests.get(url)
page


# In[3]:


# get the html code
soup = BeautifulSoup(page.text, 'html')
soup


# In[4]:


# find the table method 1
table_1 = soup.find_all('table')[1]


# In[5]:


# find the table method 2
soup.find('table', class_ = "wikitable sortable")


# In[6]:


table_1


# In[7]:


# find columns names
columns = table_1.find_all('th')


# In[8]:


columns


# In[9]:


columns_titles =[title.text.strip() for title in columns]


# In[10]:


columns_titles


# In[11]:


df = pd.DataFrame(columns = columns_titles)


# In[12]:


df


# In[13]:


columns_data = table_1.find_all('tr')


# In[14]:


for row in columns_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data
    


# In[15]:


df


# In[16]:


# Save the DataFrame to a CSV file
csv_filename = "D:\DOCS\Downloads\List of largest companies in the United States.csv"
df.to_csv(csv_filename, index=False)


# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests # you need this module to make an API call
import pandas as pd


# In[2]:


api_url = "http://api.open-notify.org/astros.json" # this url gives use the astronaut data


# In[3]:


response = requests.get(api_url) # Call the API using the get method and store the
                                # output of the API call in a variable called response.


# In[4]:


if response.ok:             # if all is well() no errors, no network timeouts)
    data = response.json()  # store the result in json format in a variable called data
                            # the variable data is of type dictionary.


# In[5]:


print(data)   # print the data just to check the output or for debugging


# In[6]:


print(data.get('number'))


# In[7]:


astronauts = data.get('people')
print("There are {} astronauts on ISS".format(len(astronauts)))
print("And their names are :")
for astronaut in astronauts:
    print(astronaut.get('name'))


# In[8]:


#Import required libraries
import requests


# In[21]:


baseurl = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/datasets/githubposting.json"


# In[22]:


def get_number_of_jobs(technology):
    number_of_jobs= 0
    response = requests.get(baseurl)
    if response.ok:             # if all is well() no errors, no network timeouts)
        data = response.json()
        tecnologias = data.get('technology')
        for item in tecnologias:
            if tecnologias.get(item).lower()==technology.lower():
                number_of_jobs += int(data.get('number of job posting').get(item))   
                
    return technology,number_of_jobs


# In[23]:


print(get_number_of_jobs('python'))


# In[24]:


#your code goes here
technologies = ['C','C%23','C%2B%2B','Java','JavaScript','Python','Scala','Oracle','SQL Server','MySQL Server','PostgreSQL','MongoDB']
technologies


# In[25]:


# your code goes here
get_ipython().system('pip3 install openpyxl')
from openpyxl import Workbook


# In[26]:


# your code goes here
wb=Workbook() 
ws=wb.active
ws


# In[27]:


#your code goes here
tech_list = list()
for language in technologies:
    jobs = get_number_of_jobs(language)
    tech_list.append(jobs)
    
ws.append(['Language', 'Job Postings'])
[ws.append(i) for i in tech_list]


# In[28]:


#your code goes here
wb.save("github-job-postings.xlsx")


# In[29]:


import pandas as pd
import os
print (os.path.abspath("github-job-postings.xlsx"))
filename="path/github-job-postings.xlsx"
df=pd.read_excel("github-job-postings.xlsx")
print(df)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import squarify
import folium


# ##  We will do some Exploratory Data Analysis on the Crime rate of the city in California, San Francisco.

# In[2]:


data = pd.read_csv('crime.csv')
# check the shape of the data
data.shape


# In[3]:


data.head()


# In[4]:


data.describe()


# In[5]:


data.isnull().sum()


# In[6]:


data['Category'] = data['Category'].astype(str)


# ## Data Visualization

# In[7]:


plt.rcParams['figure.figsize'] = (20, 9)
plt.style.use('dark_background')

sns.countplot(data=data, x='Category', palette='gnuplot')

plt.title('Major Crimes in San Francisco', fontweight='bold', fontsize=20)
plt.xticks(rotation=90)
plt.show()


# In[8]:


y = data['Category'].value_counts().head(25)
    
plt.rcParams['figure.figsize'] = (15, 15)
plt.style.use('fivethirtyeight')

color = plt.cm.magma(np.linspace(0, 1, 15))
squarify.plot(sizes = y.values, label = y.index, alpha=.8, color = color)
plt.title('Tree Map for Top 25 Crimes', fontsize = 20)

plt.axis('off')
plt.show()


# In[9]:


plt.rcParams['figure.figsize'] = (20, 9)
sns.set(style="darkgrid")

color = plt.cm.spring(np.linspace(0, 1, 15))
data['PdDistrict'].value_counts().plot.bar(color = color, figsize = (15, 10))

plt.title('District with Most Crime',fontsize = 30)

plt.xticks(rotation = 90)
plt.show()
plt.show()



# ## top 15 addresses in San Francisco In Crie

# In[10]:


plt.rcParams['figure.figsize'] = (20, 9)
plt.style.use('seaborn-v0_8-darkgrid')

color = plt.cm.ocean(np.linspace(0, 1, 15))
data['Address'].value_counts().head(15).plot.bar(color = color, figsize = (15, 10))

plt.title('Top 15 Regions in Crime',fontsize = 20)

plt.xticks(rotation = 90)
plt.show()


# ## Regions with days of crimes

# In[11]:


sns.set(style="darkgrid")


data['DayOfWeek'].value_counts().head(15).plot.pie(figsize = (15, 8), explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1))

plt.title('Crime count on each day',fontsize = 20)

plt.xticks(rotation = 90)
plt.show()


# ## Crimes In Each Month
# 
# 

# In[12]:


data['Date'] = pd.to_datetime(data['Date'])
data['Month'] = data['Date'].dt.month_name()

# Ordene os meses cronologicamente
order = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

plt.style.use('fivethirtyeight')
plt.rcParams['figure.figsize'] = (15, 8)

sns.countplot(data=data, x='Month', palette='autumn', order=order)
plt.title('Crimes in Each Month', fontsize=20)

plt.xlabel('Month', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.xticks(rotation=45)  # Ajuste a rotação dos rótulos do eixo x

plt.show()


# ## Checking the time at which crime occurs mostly

# In[13]:


import warnings
warnings.filterwarnings('ignore')

color = plt.cm.twilight(np.linspace(0, 5, 100))
data['Time'].value_counts().head(20).plot.bar(color = color, figsize = (15, 9))

plt.title('Distribution of crime over the day', fontsize = 20)
plt.show()


# ## District vs Category of Crime

# In[14]:


df = pd.crosstab(data['Category'], data['PdDistrict'])
color = plt.cm.Greys(np.linspace(0, 1, 10))

df.div(df.sum(1).astype(float), axis = 0).plot.bar(stacked = True, color = color, figsize = (18, 12))
plt.title('District vs Category of Crime', fontweight = 30, fontsize = 20)

plt.xticks(rotation = 90)
plt.show()


# ## Geographica Visualization

# In[15]:


t = data.PdDistrict.value_counts()

table = pd.DataFrame(data=t.values, index=t.index, columns=['Count'])
table = table.reindex(["CENTRAL", "NORTHERN", "PARK", "SOUTHERN", "MISSION", "TENDERLOIN", "RICHMOND", "TARAVAL", "INGLESIDE", "BAYVIEW"])

table = table.reset_index()
table.rename({'index': 'Neighborhood'}, axis='columns', inplace=True)

table


# In[16]:


gjson = r'https://cocl.us/sanfran_geojson'
sf_map = folium.Map(location = [37.77, -122.42], zoom_start = 12)


# ## Density of crime in San Francisco

# In[17]:


#generate map
sf_map.choropleth(
    geo_data=gjson,
    data=table,
    columns=['Neighborhood', 'Count'],
    key_on='feature.properties.DISTRICT',
    fill_color='YlOrRd', 
    fill_opacity=0.7, 
    line_opacity=0.2,
    legend_name='Crime Rate in San Francisco'
)

sf_map


# In[ ]:





# In[ ]:





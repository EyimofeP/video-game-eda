#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


games = pd.read_csv("Video Games Dataset.csv")


# In[3]:


games.head(10)


# Number of Rows and Columns

# In[4]:


games.info()
# 199 rows, 11 columns


# How many games have Wii as their platform

# In[5]:


len(games[games['Platform'] == "Wii"])


# Top 10 Publishers

# In[6]:


games["Publisher"].value_counts().head(10)


# Top Game Genres
# 
# 

# In[7]:


games["Genre"].value_counts().head(10)


# Top 20 Nintendo Games

# In[8]:


games[games["Publisher"] == "Nintendo"].head(20)


# Top 10 Genres in Nintendo

# In[9]:


games[games["Publisher"] == "Nintendo"]["Genre"].value_counts().head(10)


# Top Sports Games

# In[10]:


games[games["Genre"] == "Sports"]


# Top 10 Game Platforms

# In[11]:


games["Platform"].value_counts().head(10)


# Top 20 PS3 and PS4 Games

# In[12]:


games[(games["Platform"] == "PS3") | (games["Platform"] == "PS4") ].head(20)


# Top 10 Xbox Games

# In[13]:


games[games["Platform"] == "X360"].head(10)


# Higest Global Sales

# In[14]:


games["Global_Sales"].max()


# Lowest Global Sales

# In[15]:


games["Global_Sales"].min()


# Higest North American Sales

# In[16]:


games["NorthAmerica_Sales"].max()


# Lowest North American Sales

# In[17]:


games["NorthAmerica_Sales"].min()
# games[games["NorthAmerica_Sales"] == 0]


# Highest Other Sales

# In[18]:


games["Other_Sales"].max()
# games[games["Other_Sales"] == 8.46]


# Lowest Other Sales

# In[19]:


games["Other_Sales"].min()
# games[games["Other_Sales"] == 0]


# GTA Games

# In[20]:


def df_searcher(game_name, name):
    if game_name in name.lower():
        return True
    else:
        return False


# In[32]:


gta_games = games[games["Name"].apply(lambda x: df_searcher("grand", x))]
gta_games


# Sum of Global Sales of the GTA Franchise

# In[31]:


gta_games["Global_Sales"].sum()


# Average Number of Global Sales per Year

# In[77]:


year = games.groupby("Year").mean()["Global_Sales"]
year


# Year with Highest Sales

# In[90]:


year[year == year.max()]


# Year with Lowest Sales

# In[89]:


year[year == year.min()]


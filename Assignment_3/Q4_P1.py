
# coding: utf-8

# # Question 4 Part 1
# - Use ‘movies_awards’ data set
# - You are supposed to extract data from the awards column in this dataset and split it into several columns. An example is given below
# - The awards has details of wins, nominations in general and also wins and nominations in certain categories(e.g. Oscar, BAFTA etc.)
# - You are supposed to create a win and nominated column (these 2 columns contain total number of wins and nominations) and other columns that extract the number of wins and nominations for each category of award
# - If a movie has 2 Oscar nominations and 4 Oscar won, the columns Oscar_Awards_Won should have value 4 and Oscar_Awards_Nominated should have value 2. You should also have a total won and nominated column which aggregates all the awards (won or nominated)
# - Create two separate columns for each award category (won and nominated)
# - Write your output to a csv file

# In[1]:

import pandas as pd


# In[2]:

# maintain needed columns and drop NaNs
df = pd.read_csv('Data/movies_awards.csv')
col_list = ['imdbID', 'Awards']
df = df[col_list]
df = df.dropna()
df.head(4)


# In[3]:

import re    


# In[4]:

# get number of wins. name can be 'Oscar', 'Prime', etc.
def find_famous_wins(name, row):
    pattern = r'Won (\d+) '+name
    nums = re.findall(pattern, row)
    if len(nums)>0:
        return nums[0]
    else:
        return '0'


# In[5]:

# get number of Nominations. name can be 'Oscar', 'Prime', etc.
def find_famous_Noms(name, row):
    pattern = r'Nominated for (\d+) '+name
    nums = re.findall(pattern, row)
    if len(nums)>0:
        return nums[0]
    else:
        return '0'


# In[6]:

# get total of wins. total = other_wins + Oscar_wins + Prime_wins + ...
def find_all_wins(row):
    pattern = r'(\d+) win'
    famous_wins = int(row['Prime_Won'])+int(row['Oscar_Won'])+int(row['Golden_Globe_Won'])+int(row['BAFTA_Won'])
    nums = re.findall(pattern, row['Awards'])
    if len(nums)>0:
        return int(nums[0])+famous_wins
    else:
        return famous_wins


# In[7]:

# get total of nominations. total = other_nominations + Oscar_nominations + Prime_nominations + ...
def find_all_noms(row):
    pattern = r'(\d+) nomination'
    famous_noms = int(row['Prime_Nominated'])+int(row['Oscar_Nominated'])+int(row['Golden_Globe_Nominated'])+int(row['BAFTA_Nominated'])
    nums = re.findall(pattern, row['Awards'])
    if len(nums)>0:
        return int(nums[0])+famous_noms
    else:
        return famous_noms


# In[8]:

df['Prime_Won'] = df.apply(lambda row: find_famous_wins('Prime', row['Awards']), axis=1)
df.head(4)


# In[9]:

df['Oscar_Won'] = df.apply(lambda row: find_famous_wins('Oscar', row['Awards']), axis=1)
df.head(4)


# In[10]:

df['Golden_Globe_Won'] = df.apply(lambda row: find_famous_wins('Golden', row['Awards']), axis=1)
df.head(4)


# In[11]:

df['BAFTA_Won'] = df.apply(lambda row: find_famous_wins('BAFTA', row['Awards']), axis=1)
df.head(4)


# In[12]:

df['Prime_Nominated'] = df.apply(lambda row: find_famous_Noms('Prime', row['Awards']), axis=1)
df.head(4)


# In[13]:

df['Oscar_Nominated'] = df.apply(lambda row: find_famous_Noms('Oscar', row['Awards']), axis=1)
df.head(4)


# In[14]:

df['Golden_Globe_Nominated'] = df.apply(lambda row: find_famous_Noms('Golden', row['Awards']), axis=1)
df.head(4)


# In[15]:

df['BAFTA_Nominated'] = df.apply(lambda row: find_famous_Noms('BAFTA', row['Awards']), axis=1)
df.head(4)


# In[16]:

# After caculated Special wins and nominations, add those to total wins and nominations
df['Total_Wins'] = df.apply(find_all_wins, axis=1)


# In[17]:

df['Total_Nominations'] = df.apply(find_all_noms, axis=1)
df.head(4)


# In[18]:

# save to csv
df.to_csv('output_csv/q4p1_output.csv',index=False,header=True)
print(df.head(3))


# In[ ]:




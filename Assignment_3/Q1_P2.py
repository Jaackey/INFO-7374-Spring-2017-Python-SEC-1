
# coding: utf-8

# # Question 1 Part 2
# - Use ‘vehicle_collisions’ data set
# - For each borough, find out distribution of each collision scale. (One carinvolved? Two? Three? or more?) (From 2015 to present)
# - Display a few rows of the output use df.head()
# - Generate a csv output with five columns ('borough', 'one-vehicle', 'two- vehicles', 'three-vehicles', 'more-vehicles')

# In[30]:

import pandas as pd


# In[43]:

# drop unnecessary columns
raw_df = pd.read_csv('Data/vehicle_collisions.csv')
col_list = ['BOROUGH', 'VEHICLE 1 TYPE', 'VEHICLE 2 TYPE', 'VEHICLE 3 TYPE', 'VEHICLE 4 TYPE']
raw_df = raw_df[col_list]
raw_df.head(4)


# In[44]:

# count how many vehicle types not null for each row
raw_df['COUNT_VEHICLE'] = raw_df.count(axis=1) - 1
raw_df.head(4)


# In[45]:

# drop unnecessary columns
col_list = ['BOROUGH', 'COUNT_VEHICLE']
raw_df = raw_df[col_list]
raw_df.head(4)


# In[46]:

# remove zeros for vehicle count
raw_df = raw_df[raw_df['COUNT_VEHICLE'] != 0]
raw_df.head(4)


# In[47]:

# remove NaN borough
raw_df = raw_df[pd.notnull(raw_df['BOROUGH'])]
raw_df.head(4)


# In[48]:

# turn count to str and change numbers which >3 into '3+'
raw_df['COUNT_VEHICLE'] = raw_df['COUNT_VEHICLE'].apply(lambda x : str(x) if x < 4 else '3+')
raw_df.head(4)


# In[49]:

# group borough and count then calculate occurence of each count in each borough
df2 = raw_df.groupby(['BOROUGH', 'COUNT_VEHICLE'], as_index=False).size().reset_index()
df2.head(5)


# In[50]:

# use borough as index and count as columns to reshape dataframe
df3 = df2.pivot(index='BOROUGH', columns='COUNT_VEHICLE', values=0)
df3


# In[51]:

# change names of columns
df3.columns = ['ONE_VEHICLE_INVOLVED', 'TWO_VEHICLE_INVOLVED', 'THREE_VEHICLE_INVOLVED', 'MORE_VEHICLE_INVOLVED']
df3


# In[52]:

# reset indices
df4 = df3.reset_index()
df4


# In[53]:

# save to csv
df4.to_csv('output_csv/q1p2_output.csv',index=False,header=True)
print(df4.head(3))


# In[ ]:




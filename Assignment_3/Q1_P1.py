
# coding: utf-8

# # Question 1 Part 1
# - Use ‘vehicle_collisions’ data set
# - For each month in 2016, find out the percentage of collisions in Manhattan out of that year's total accidents in New York City
# - Display a few rows of the output use df.head()
# - Generate a csv output with four columns (‘Month’, ‘Manhattan’, ‘NYC’, ‘Percentage’)

# In[46]:

import pandas as pd


# In[47]:

# import csv file to Dataframe
# check how many rows are there for each district (not necessarily)
df = pd.read_csv('Data/vehicle_collisions.csv')
borough_count = df['BOROUGH'].value_counts()
borough_count


# In[48]:

# get rows of year 2016
df = df[df.apply(lambda x: x['DATE'].split('/')[2] == '16', axis=1)]
df.head(3)


# In[49]:

# count totals in each month in whole NYC
total_count = df['DATE'].apply(lambda x: x.split('/')[0]).value_counts()
total_count


# In[50]:

# count numbers in each month in Manhattan
df_man = df[df.apply(lambda x: x['BOROUGH'] == 'MANHATTAN', axis=1)]
man_count = df_man['DATE'].apply(lambda x: x.split('/')[0]).value_counts()
man_count


# In[51]:

# join two series to Dataframe
output_df = pd.concat([man_count, total_count], axis=1)
# name the columns
output_df.columns = ['MANHATTAN', 'NYC']
# change indices(months) to int
output_df.index = output_df.index.map(int)
# sort by index (from Jan to Dec)
output_df.sort_index(inplace=True)
output_df.head(3)


# In[66]:

# sum up and get total in the last row
output_df2 = output_df.append(output_df.sum(numeric_only=True), ignore_index=True)
# name the index column
output_df2.columns.name = 'MONTH'
output_df2.tail(2)
# row with index = 12 is the total of collisions in whole year


# In[67]:

# calculate percentage
output_df2['PERCENTAGE'] = output_df2['MANHATTAN']/output_df2['NYC']
# rename indices as months
output_df3 = output_df2.rename(index={0: 'Jan', 1: 'Feb', 2: 'Mar', 3: 'Apr', 4: 'May', 5: 'Jun', 6: 'Jul', 7: 'Aug', 8: 'Sep', 9: 'Oct', 10: 'Nov', 11: 'Dec', 12: 'Total'})
output_df3.tail(3)


# In[68]:

# save to csv
output_df3.to_csv('output_csv/q1p1_output.csv',index=True,header=True,index_label='MONTH')
print(output_df3.head(3))


# In[ ]:





# coding: utf-8

# # Question 2 Part 1
# - Use 'employee_compensation' data set
# - Find out the highest paid departments in each organization group by calculating mean of total compensation for every department
# - Output should contain the organization group and the departments in each organization group with the total compensation from highest to lowest value
# - Display a few rows of the output use df.head()
# - Generate a csv output

# In[1]:

import pandas as pd


# In[2]:

# drop unnecessary columns
raw_df = pd.read_csv('Data/employee_compensation.csv')
col_list = ['Organization Group', 'Department', 'Total Compensation']
raw_df = raw_df[col_list]
raw_df.head(4)


# In[5]:

# get average while maintaining organization group & Department
output_df = raw_df.groupby(['Organization Group','Department'],as_index=False).mean()
output_df.head(4)


# In[10]:

# for each Organization Group, sort the department in it by average total compensation
output_df = output_df.sort_values(['Organization Group','Total Compensation'], ascending = False)
output_df.head(4)


# In[11]:

# save to csv
output_df.to_csv('output_csv/q2p1_output.csv',index=False,header=True)
print(output_df.head(3))


# In[ ]:




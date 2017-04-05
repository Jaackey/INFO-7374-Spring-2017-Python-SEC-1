
# coding: utf-8

# # Question 2 Part 2
# - Use 'employee_compensation' data set
# - Data contains fiscal and calendar year information. Same employee details exist twice in the dataset. Filter data by calendar year and find average salary (you might have to find average for each of the columns for every employee. Eg. Average of Total Benefits, Average of total compensation etc.) for every employee
# - Now, find the people whose overtime salary is greater than 5% of salaries (salaries refers to ’Salaries' column)
# - For each ‘Job Family’ these people are associated with, calculate the percentage of total benefits with respect to total compensation (so for each job family you have to calculate average total benefits and average total compensation). Create a new column to hold the percentage value
# - Display the top 5 Job Families according to this percentage value using df.head()
# - Write the output (jobs and percentage value) to a csv

# In[1]:

import pandas as pd


# In[23]:

# filter calendar year and maintain useful columns
raw_df = pd.read_csv('Data/employee_compensation.csv')
raw_df = raw_df[raw_df['Year Type'] == 'Calendar']
col_list = ['Job Family', 'Employee Identifier' , 'Salaries', 'Overtime', 'Total Benefits', 'Total Compensation']
raw_df = raw_df[col_list]
raw_df.head(4)


# In[24]:

# get averages (Job Family & Employee Identifier should be maintained)
employee_mean = raw_df.groupby(['Job Family', 'Employee Identifier'], as_index=False).mean()
employee_mean.head(4)


# In[28]:

# get those rows where overtime > 5% of salaries
over_time = employee_mean[employee_mean['Overtime'] > employee_mean['Salaries']*0.05]
over_time.head(4)


# In[29]:

# drop unnecessary columns
col_list = ['Job Family', 'Total Benefits', 'Total Compensation']
cut_df = over_time[col_list]
cut_df.head(4)


# In[30]:

# drop unnecessary columns
job_family = cut_df.groupby(['Job Family'], as_index=False).mean()
job_family.head(4)


# In[33]:

# get average and sort in descending order
job_family['Percentage_Total_Benefit'] = job_family['Total Benefits'] / job_family['Total Compensation'] * 100
out_df = job_family.sort_values(by='Percentage_Total_Benefit', ascending=False)
out_df.head(5)


# In[34]:

# save to csv
out_df.to_csv('output_csv/q2p2_output.csv',index=False,header=True)
print(out_df.head(3))


# In[ ]:




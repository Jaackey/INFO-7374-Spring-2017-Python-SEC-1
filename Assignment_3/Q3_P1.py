
# coding: utf-8

# # Question 3 Part 1
# - Use ‘cricket_matches’ data set
# - Calculate the average score for each team which host the game and win the game
# - Remember that if a team hosts a game and wins the game, their score can be innings_1 runs or innings_2 runs. You have to check if the host team won the game, check which innings they played in (innings_1 or innings_2), and take the runs scored in that innings. The final answer is the average score of each team satisfying the above condition
# - Display a few rows of the output use df.head()
# - Generate a csv output

# In[1]:

import pandas as pd


# In[5]:

# maintain rows where hosts win
raw_df = pd.read_csv('Data/cricket_matches.csv')
raw_df = raw_df[raw_df['home'] == raw_df['winner']]
raw_df.head(2)


# In[19]:

# drop unnecessary columns
col_list = ['home', 'innings1' , 'innings2', 'innings1_runs', 'innings2_runs']
cut_df = raw_df[col_list]
cut_df.head(4)


# In[20]:

# decide which innings runs should we get
def choose_col(row):
    if row['home'] == row['innings1']:
        return row['innings1_runs']
    else:
        return row['innings2_runs']


# In[21]:

# drop NaNs and add Score column
# new_df.info()
cut_df['Score'] = cut_df.apply(choose_col, axis=1)
cut_df.head(4)


# In[22]:

# drop unnecessary columns
col_list = ['home', 'Score']
new_df= cut_df[col_list]
new_df.head(3)


# In[23]:

# get average scores of each team
out_df = new_df.groupby(['home'], as_index=False).mean()
out_df.head(4)


# In[24]:

out_df.to_csv('output_csv/q3p1_output.csv',index=False,header=True)


# In[ ]:




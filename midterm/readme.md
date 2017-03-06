
# Midterm Report

## Question 1

### Analysis 1

- find top 50 most used words in sent emails
- generate a CSV file listing the words and frequency

I first retreive emails in sent-boxes of all users using glob;
Then I get the words in emails in sent-boxes using .read().split() and counted the frequency with Counter;
At last I generate a CSV file listing the words and frequency.
The final output is in que_1/ana_1/sent_words.csv

From the Result we can find that words such as "agreement", "power", "Houston" and "energy" frequently occurs in emails.

### Analysis 2

- count times of email contact among all users in data set
- generate a CSV file showing the result

I first try to know who are in this data set;
Then, I retreive emails in sent-boxes of all users using glob, it will be unecessarily duplicate email counts if I retreive more boxes;
Here I locate the line starting with "From: " whose index is 2, and get the name of user by string slicing;
Next, I transfere this user set into a dictionary that relates an email address to an ID;
I create a matrix(list of lists) whose indices are ID of users;
We have 121 users in this data set, thus a 121*121 matrix will be created, each of whose element represents number of emails between two users;
Row indices are IDs of senders;
Column indices are IDs of receivers;
I then iterate through all sent-boxes, find the sender in line starting with "From: " and find the receiver(s) starting in line "To: ";
There may be multiple receivers, so create a list to store them;
The receivers end in line starting with "Subject: "
After getting sender and receivers in each email, I find the ID of those users and update the matrix;
At last generate two CSV files, one showing the users and their IDs, the other showing the IDs and number of emails between every one another;
The final outputs are in que_1/ana_3/email_id.csv and que_1/ana_3/email_count.csv

From the Result we can find email times between every one in the dataset. Some people contact a lot between each other which infers a strong relationship. Further conclusion will be obtained in next analysis.

### Analysis 3

- from CSV files generated in analysis 2, import as a matrix
- for every user, find the person to whom most emails are sent
- generate a CSV file listing who is the "most-emailed-friend" for every user and number of emails

I first read the CSV file generated in last analysis 2, and turn it into matrix using "for comprehension";
For each row in matrix, find the indices of maximum number in that row, then I have for each user who is the one he send most emails to;
Then from another CSV I get id and relating email address;
I only analyzed emails that are sent to users in this data set;
Not all users are listed in CSV file, because some of them usually send emails to people not in this data set;
We can see from 'que1/ana_3/most_email_friend.csv' CSV file that who are 'most-emailed-friends' of users in this data set.

From the Result we can find people such as phillip.love and cindy.stark can be very close, more those relationships can be found out in CSV file.

## Question 2

### Analysis 1

- with NYT archive API download all news in year 1993
- find name keywords of every article in this year
- try to find the most important person in this year
- generate a CSV file showing these important people

I first get the persons in keyword of those news using json.load() and add them to person_list;
Next count the frequency of those names and order them using Counter;
At last write those persons into CSV file in popularity-descending order.
The result is stored in que_2/ana_1/important_persons.csv

From the result we can find some interesting conclusion:
As Bill Clinton showed up 3863 times in keywords in year 1993, we have plenty of evidence to say he is the most important (or controversial) person in that year;
Just behind Bill Clinton, David Dinkins (106th Mayor of New York City, from 1990 to 1993) and Rudolph Giuliani (107th Mayor of New York City, from 1994 to 2001) are also reasonable to be popular on NYT news
Also many famous people in that age can be found in output

### Analysis 2

- find top 10 words that frequently occur in top 50 in lead paragraphs of 1993 and not in top 50 of 2016
- if there are not enough 10 words like this, show all words in top 50 of 1993 that not in top 50 of 2016
- the words are not supposed to be stop words or punctuation
- show the result in frequency-descending order in CSV file

News in 1993 and 2016 is downloaded using NYT archive API and is used in this analysis;
I first use a def to get the count of words in lead paragraph;
The words should not include any punctuations or figures and should not be stop words, which is hardly meaningful for our analysis;
Next prepare the paths to each data set;
Then use the def to get both counters which include the words and their frequency in those lead paragraphs;
Iterate collections and find most common words in 1993 which not in 2016;
At last store these words into CSV file in frequency-descending order;
The final output is in que_2/ana_2/disappear_words.csv

From the result we can find the words that usually used in 1993 but rarer in 2016 such as "yesterday", "federal", "officials", "national" and 18 more these words.

### Analysis 3

- Download articles with keyword "China" using NYT article-search API
- compare those in year 1980 with in 2010
- find out what articles usually focus on in either year and see if the focus about China had changed
- generate a CSV file to see what are the focus on either year

To prevent duplicate code, I create a def to locate subjects in keywords of articles in either year;
Prepare the variables including paths and counters;
Call the def and get the subjects;
Update both counters;
Write the two collections to CSV at the same time;
Iterate collections with index and get the tuples;
In each tuples, tuple[0] refers to the subject, tuple[1] refers to the frequency of that subject;

The result is interesting, as we can see from CSV file. In the year 1980, NYT focus very much on politics and government relating to China, which is only the 10th focus subject in 2010.
Just as the example above, we can jump to several further conclusions:
For China, what NYT cares the most in 1980 is China's politics and government while in 2010 is international trade and world market. The change of focus reflects how China developed in these 30 years.
Economic conditions and trends are always a main focus during these years.
In 2010, computers and the Internet, a keyword in top 3 focus showed up, which cannot be found in even top 50 of year 1980. Thus computers and the Internet is definitely a hot concern of China in recent years.



```python

```

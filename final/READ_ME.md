
# Final Exam Report

## Data Set

I used Yelp data set downloaded from https://www.kaggle.com/c/yelp-recruiting/data.
There are 4 JSON files in this data set, describing business, review, user and checkin.

Size of these data:
11,537 businesses
8,282 checkin sets
43,873 users
229,907 reviews

Below are brief examples of each json, including only used parameters, please find thourgh link above.

- Business
{
'business_id': (encrypted business id),
'full_address': (localized address),
'city': (city),
'state': (state),
'stars': (star rating, rounded to half-stars),
'review_count': review count,
'categories': [(localized category names)]
 ......
}

- review

{
'business_id': (encrypted business id),
'stars': (star rating),
'text': (review text),
'votes': {'useful': (count), 'funny': (count), 'cool': (count)}
 ......
}

- user

{
'review_count': (review count),
'average_stars': (floating point average, like 4.31),
 ......
}

- checkin

{
'business_id': (encrypted business id),
'checkin_info': {

'0-0': (number of checkins from 00:00 to 01:00 on all Sundays), 
'1-0': (number of checkins from 01:00 to 02:00 on all Sundays), 
... 
'14-4': (number of checkins from 14:00 to 15:00 on all Thursdays), 
... 
'23-6': (number of checkins from 23:00 to 00:00 on all Saturdays)

} # if there was no checkin for a hour-day block it will not be in the dict
}

## Analysis 1

### Questions

- On which day in a week do Yelp users hang out most?
- At what time in a day do they hang out most?

### Objectives

- For each day in a week, find number of business that have most check-ins on that day
- For each hour in a day, find number of business that have most check-ins in that hour

### Steps

- use checkin.json in data set, find day and hour with most check-ins for each business

For each line(object) in json file, find check_in_info (a list of dictionaries), pass it to a def already written to find max-check-in hour and max-check-in day by splitting time info, storing into DataFrame, groupby day or hour, and use argmax() method. The result of this step looks like this:

business_id	        max_day max_hour
KO9CpaSPOoqm0iCWm5scmg	3	12
oRqBAYtcBYZHXA7G8FlPaA	5	18
6cy2C9aBXUwkrh4bY1DApw	5	11

This dataframe is saved as 'ana_1/max_check_ins.csv'

- calculate occurence of each day and each hour, generate plot

for column 'max_day' and 'max_hour' use value_counts() then sort_index() to show from Sun. to Mon.
Below is the plot results:

![alt](https://github.com/Jaackey/INFO-7374-Spring-2017-Python-SEC-1/blob/master/final/analysis/ana_1/max_day_check_ins.png?raw=true)

![alt](https://github.com/Jaackey/INFO-7374-Spring-2017-Python-SEC-1/blob/master/final/analysis/ana_1/max_hour_check_ins.png?raw=true)

### Conclusions

- Friday being the first choice for people to hang out, many people also choose Thursday
- Few people choose Sat. and Sun. even if it's weekend
- Wed. is the worst, there are fewest people hanging out on Wed.
- From 10:00 people start hanging out and at around 12:00-13:00, number of people reaches highest point
- It seems that more people choose noon to hang out rather than evening, however, there are chances that people forget  to check in when hanging out in evening
- We can guess people in AZ have most activities outside from 10 A.M. to 8 P.M.

## Analysis 2

### Questions

- How many different catogries of Yelp businesses are there?
- Are most all Yelp businesses really restaurants?
- How many percents of all businesses does each catogory hold?

### Objectives

- Retrieve all Yelp catogories
- Rank the catogories and calculate the percentage for top 10 categories

### Steps

- use business.json in data set, find catogories property for each business

For each line(object) in json file, find categories (list of str), extend it to the list, change the list to set, and get the length. As a result, there are 508 different categories in this data set

- count the occurence, calculate percentage of each catogory and generate a pie plot showing percetages

Use Counter to count the occurence of each category add a colomn containing percentages for each row. Use format to give percision to floats, and the data frame finally looks like this:

category	count	percent
restaurants	9006.0	14.58%
shopping	3362.0	5.44%
food	    3232.0	5.23%

This data frame is saved as SCV file in 'ana_2/categories.csv'

Below is the plot results:


![alt](https://github.com/Jaackey/INFO-7374-Spring-2017-Python-SEC-1/blob/master/final/analysis/ana_2/categoties.png?raw=true)

### Conclusions

- There are 508 different categories among yelp businesses
- Only 14.58% of 61,782 businesses have the category "Restaurant"
- Top 10 popular categories such as bars and nightlife hold about 40% of all businesses, while the other 60% businesses own other categories

## Analysis 3

### Questions

- There are three type of votes to reviews on Yelp: funny, useful and cool, what might influence the votes other than the content of reviews?
- What length of reviews more likely to be considered useful? Longer or shorter? What about funny and cool?
- Reviews also come with stars giving to Yelp businesses. How many stars are more likely to be considered useful, funny or cool?

### Objectives

- For yelp reviews, find how number of words and stars influence votes made to that review

### Steps

- Use review.json in data set, find stars and number of each votes for each review

- Calculate number of words in review content, save it together with informaiton above to data frame

The data frame finally looks like this:

words	stars  funny  useful cool
889.0	5.0	   0.0	  5.0	 2.0
76.0	4.0	   0.0	  1.0	 0.0
419.0	5.0	   0.0	  2.0	 1.0

- First generate a plot showing relations between number of words and votes(funny, cool, useful and total)

Below is the plot results:

![alt](https://github.com/Jaackey/INFO-7374-Spring-2017-Python-SEC-1/blob/master/final/analysis/ana_3/stars_and_votes.png?raw=true)

- Then generate a plot of stars and votes

Below is the plot results:

![alt](https://github.com/Jaackey/INFO-7374-Spring-2017-Python-SEC-1/blob/master/final/analysis/ana_3/words_and_votes.png?raw=true)



### Conclusions

- Length and stars of reviews do have a little implicit influence on different votes
- First, stars. Five figures are nearly the same for 'total votes', but difference can be found in other three plots
- "Useful": both max quartile and max whisker in 4~5 stars are less than they are in other votes, that is to say, many 4~5 star reviews have only a limited number(less than 10) useful votes, while 0~4 star reviews have a better frequency that receive more than 10 useful votes.
- "funny": reviews with 2 stars or below have an apparent high chance to receive more "funny" votes
- "cool": low star-rated review are usually considered "not cool"
- Then, words. We can see that NOT "the longer review, the more votes".
- Reviews with around 800 words are most likely to gain more votes.
- Hardly can we tell how number of words influence different votes

## Analysis 4

### Questions

- The data set describes businesses in AZ, which street is the most profitable street in each city?
- Which streets can be a good place to find restaurants in each city in AZ?
- Which streets can be the most popular to drink and play in each city in AZ? 

### Objectives

- In each city in state AZ, find the most profitable streets
- In each city in state AZ, find the streets where can be a good place to find restaurants
- In each city in state AZ, find the most popular streets to drink and play

### Steps

- Use business.json in data set and get city and street information for each business

Use regex and string split to find street and city info in address

- Find street with most business in each city

Use groupby, sum and reset_index

- Find restaurants with catogory containing certain keywords

- In these restaurants, find those with more than 10 reviews and more than 4.0/5.0 average stars

- Rank the streets by number of those restaurants

First groupby('city', 'street') sum, reset_index, then group ('city'), max and reset_index

- Find business with catogory containing certain keywords with enough reviews and stars

Also do this to bars and nightlifes

- Generate CSV as result

CSV result is saved as 'ana4/profitable_streets_in_AZ.csv', 'ana4/restaurant_streets_in_AZ.csv' and 'ana4/nightlife_streets_in_AZ.csv'

### Conclusions

- St & Via Linda in Scottsdale can be the most profitable street in AZ
- There is a high chance to find a good restaurant at North Scottsdale Rd in Scottsdale
- W Northern Ave in Phoenix is a good place to find somewhere to drink and play

## Analysis 5

### Questions

- Some people only give review to unsatisfied restaurants and give low star-rate, is that true?
- How many average stars do people with different reviews have?
- How many stars, generally, do AZ people might think of their state?

### Objectives

- for yelp users find relation between their numbers of reviews given and average stars
- try to find weighted average rank of businesses in AZ
- further speculate habit of users writting reviews to business

### Steps

- use user.json in data set
- get review count and average stars for each user
- generate dataframe to record data
- calculate weighted average rank of businesses in AZ
- generate plots to analyze relation between their numbers of reviews given and average stars

Below is the plot results:

![alt](https://github.com/Jaackey/INFO-7374-Spring-2017-Python-SEC-1/blob/master/final/analysis/ana_5/reviews_and_average_stars.png?raw=true)

![alt](https://github.com/Jaackey/INFO-7374-Spring-2017-Python-SEC-1/blob/master/final/analysis/ana_5/users_in_review_range.png?raw=true)

![alt](https://github.com/Jaackey/INFO-7374-Spring-2017-Python-SEC-1/blob/master/final/analysis/ana_5/users_in_star_range.png?raw=true)

![alt](https://github.com/Jaackey/INFO-7374-Spring-2017-Python-SEC-1/blob/master/final/analysis/ana_5/users_stars_and_reviews.png?raw=true)

### Conclusions

- People might think their state owns 3.72 in general.
- The more reviews one person give, the average stars more likely to tend to around 3.7
- More than half people(people with no review not included) have given under 10 reviews
- There are the most people who give average stars between 3~4 than other range
- People who have given less than 3 reviews have a lower average stars than others
- Yes, it can be guessed that some people give few reviews and they only give low stars





```python

```

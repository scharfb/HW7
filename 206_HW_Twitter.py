import unittest
import tweepy
import requests
import json
from twitter_info import * 

## SI 206 - HW 7 (Bradley Scharf)
## COMMENT WITH:
## Your section day/time: Thursday 3:00PM
## Any names of people you worked with on this assignment:


## Write code that uses the tweepy library to search for tweets with three different phrases of the 
## user's choice (should use the Python input function), and prints out the Tweet text and the 
## created_at value (note that this will be in GMT time) of the first FIVE tweets with at least 
## 1 blank line in between each of them, e.g.


## You should cache all of the data from this exercise in a file, and submit the cache file 
## along with your assignment. 

## So, for example, if you submit your assignment files, and you have already searched for tweets 
## about "rock climbing", when we run your code, the code should use CACHED data, and should not 
## need to make any new request to the Twitter API.  But if, for instance, you have never 
## searched for "bicycles" before you submitted your final files, then if we enter "bicycles" 
## when we run your code, it _should_ make a request to the Twitter API.

## Because it is dependent on user input, there are no unit tests for this -- we will 
## run your assignments in a batch to grade them!

## We've provided some starter code below, like what is in the class tweepy examples.

##SAMPLE OUTPUT
## See: https://docs.google.com/a/umich.edu/document/d/1o8CWsdO2aRT7iUz9okiCHCVgU5x_FyZkabu2l9qwkf8/edit?usp=sharing



## **** For extra credit, create another file called twitter_info.py that 
## contains your consumer_key, consumer_secret, access_token, and access_token_secret, 
## import that file here.  Do NOT add and commit that file to a public GitHub repository.

## **** If you choose not to do that, we strongly advise using authentication information 
## for an 'extra' Twitter account you make just for this class, and not your personal 
## account, because it's not ideal to share your authentication information for a real 
## account that you use frequently.

## Get your secret values to authenticate to Twitter. You may replace each of these 
## with variables rather than filling in the empty strings if you choose to do the secure way 
## for EC points

## Set up your authentication to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# Set up library to grab stuff from twitter with your authentication, and 
# return it in a JSON-formatted way

api = tweepy.API(auth, parser=tweepy.parsers.JSONParser()) 

## Write the rest of your code here!

#### Recommended order of tasks: ####
## 1. Set up the caching pattern start -- the dictionary and the try/except 
## 		statement shown in class.

CACHE_FNAME = 'cache_twitter_queries.json' # String for your file. We want the JSON file type, bcause that way, we can easily get the information into a Python dictionary!

try:
	cache_file = open(CACHE_FNAME, 'r') # Try to read the data from the file
	cache_contents = cache_file.read()  # If it's there, get it into a string
	CACHE_DICTION = json.loads(cache_contents) # And then load it into a dictionary
	cache_file.close() # Close the file, we're good, we got the data in a dictionary.
except:
	CACHE_DICTION = {}

## 2. Write a function to get twitter data that works with the caching pattern, 
## 		so it either gets new data or caches data, depending upon what the input 
##		to search for is. 

def get_twitter_data(search_term):
# check if our search term is already in the cache
	if search_term in CACHE_DICTION:
		# return data from the cache
		print ("using cache")
		return CACHE_DICTION[search_term]
	else:
		# query twitter API for new data
		response = api.search(search_term, count = 5)
		CACHE_DICTION[search_term] = response
		print ("fetching")
		return response
		# save that to the cache 

## 3. Using a loop, invoke your function, save the return value in a variable, and explore the 
##		data you got back!

## 4. With what you learn from the data -- e.g. how exactly to find the 
##		text of each tweet in the big nested structure -- write code to print out 
## 		content from 5 tweets, as shown in the linked example.
def print_info(result):
	# result is a big dictionary
	# the key "statuses" is associated with a 
	# list of dictionaries, each dictionary contains info about one tweet
	tweet_list = result["statuses"]
	for tweet in tweet_list:
		# tweet is a dictionary
		# it has entries like "text" : "Text of the tweet"
		# and "created_at" : "date format thing" 
		print ("TEXT:", tweet["text"])
		print ("CREATED AT:", tweet["created_at"])
		print ("\n")
for i in range(0,3):
	term = input("Enter Tweet term: ")
	result = get_twitter_data(term)
	print_info(result)




file_string = json.dumps(CACHE_DICTION)
with(open(CACHE_FNAME, 'w')) as file:
	file.write(file_string)






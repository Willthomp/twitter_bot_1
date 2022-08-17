## Program to post new tweets 


#-------importing tweepy and csv
import tweepy 
import csv
import time
import os
from os import environ


#-------create variables to store api key and api secret key for your app in the api
api_key =  environ['api_key'] 
api_key_secret = environ['api_key_secret'] 


#-------authorize your api key & api secret key
auth = tweepy.OAuthHandler(api_key , api_key_secret)


#-------set access_token and access_token_secret
auth.set_access_token( environ['access_token'], environ['access_token_secret'])


#-------create the api instance
api = tweepy.API(auth)


#-------------------Reading the csv file :)---------------------------------

num_of_tweets = 6             #-------------------scheduled for 6 tweets a day

with open('tweets.csv', mode ='r')as file:
	csvFile = csv.reader(file)
	count = 0
	for tweets in csvFile:
		#post a tweet - [update_status]
		api.update_status(tweets[0])
		print(tweets[0])
		#check if the scheduled limit has been reached
		if (count+1)%num_of_tweets == 0 and (count+1) >= num_of_tweets:
			print("sleep for 24 hours")
			time.sleep(60)
		count+=1
		print("sleep for 1 minute")
		time.sleep(60)

#---------------------------------------------------------------------------


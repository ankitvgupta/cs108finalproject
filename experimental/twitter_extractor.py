#!/usr/bin/env python
# encoding: utf-8

import sys
import os.path
import tweepy #https://github.com/tweepy/tweepy
import csv
import json

def main(target_user, outfile):
	#Get Twitter API Credentials from File
	consumer_key, consumer_secret = extract_keys("../data/APIKeys.json")
	access_key = ""
	access_secret = ""

	#pass in the username of the account you want to download
	get_all_tweets(target_user, consumer_key, consumer_secret, access_key, access_secret, outfile)

# returns the consumer_secret and consumer_keys from JSON file with API keys.
def extract_keys(keys_file_name):
	with open(keys_file_name) as keys_file:    
	    data = json.load(keys_file)
	    return str(data['consumer_key']), str(data['consumer_secret'])

def get_all_tweets(screen_name, consumer_key, consumer_secret, access_key, access_secret, outfile):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	#authorize twitter, initialize tweepy
	print "\n *** Authorizing API Call ***"
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	print auth
	auth.set_access_token(access_key, access_secret)
	print auth
	api = tweepy.API(auth)
	print api
	print "*** SUCCESS ***\n" 
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	print "*** Downloading Tweets ***"
	while len(new_tweets) > 0:
		print "getting tweets before %s" % (oldest)
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,
									   count = 200,
									   max_id = oldest,
									   exclude_replies = True, #excludes all @ replies
									   include_rts = False) #excludes all native retweets
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print "...%s tweets downloaded so far" % (len(alltweets))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]

	#write the csv
	fpath = os.path.join("../data/", outfile)
	
	with open(fpath, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)

	print "\n*** Successfully downloaded all recent tweets from @%s" % screen_name
	
if __name__ == '__main__':
	
	#catch improper usage
	if len(sys.argv) != 2:
		print "Usage: twitter_extractor.py <target_user>"
		sys.exit(2)

	#call main
	main(sys.argv[1])
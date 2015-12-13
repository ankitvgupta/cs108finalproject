import os.path
import argparse
import twitter_extractor
import model_test

def run_tweet_generator(targets, k):
	raw_file = "_".join(targets) + ".csv"
	fpath = os.path.join("../data/", raw_file)
	if (os.path.isfile(fpath) == False):
		#Pull tweets from Twitter API and store data in outfile
		twitter_extractor.save_users_tweets_to_file(targets, raw_file)

	#Build and run Markov model
	model_test.generateTweetsFromFile(raw_file, k)


if __name__ == "__main__":
	#Define and parse command line arguments
	parser = argparse.ArgumentParser()
	#parser.add_argument('target', type=str, help='Twitter handle of target user (omit @)')
	parser.add_argument('-names', '--names', nargs='+', help="Handles", required=True)
	#parser.add_argument('-f', type=str, help='Name of file to store downloaded raw tweet data', required=True)
	parser.add_argument('-k', type=int, default=3, help='Size of KMer (default = 3)')
	args = parser.parse_args()
	print args
	raw_file = "_".join(args.names) + ".csv"
	print args.names
	run_tweet_generator(args.names, args.k)


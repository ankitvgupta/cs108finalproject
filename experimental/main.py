import os.path
import argparse
import twitter_extractor
import model_test

#Define and parse command line arguments
parser = argparse.ArgumentParser()
#parser.add_argument('target', type=str, help='Twitter handle of target user (omit @)')
parser.add_argument('-names', '--names', nargs='+', help="Handles", required=True)
parser.add_argument('-f', type=str, help='Name of file to store downloaded raw tweet data', required=True)
parser.add_argument('-k', type=int, default=3, help='Size of KMer (default = 3)')
args = parser.parse_args()
print args

print args.names

#Default to target twitter handle if no file name specified
#if (args.f == None):
#	args.f = args.target

targets = args.names 		  #Twitter handle
raw_file = "%s.csv" % args.f  #Raw data file
raw_file = args.f
k = args.k 					  #Size of KMer

#Check if data file for target already exists
fpath = os.path.join("../data/", raw_file)
if (os.path.isfile(fpath) == False):
	#Pull tweets from Twitter API and store data in outfile
	twitter_extractor.main(targets, raw_file)

#Build and run Markov model
model_test.main(raw_file, k)

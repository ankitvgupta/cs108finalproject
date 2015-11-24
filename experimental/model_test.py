import csv
import numpy as np
filename = "BarackObama_tweets.csv"

from model_generator import getAllKMers, buildModel, getStartingKMers


tweets = []

with open(filename, 'r') as tweetsfile:
	csvreader = csv.reader(tweetsfile, delimiter=',')
	for line in csvreader:
		tweets.append(line[-1])

K = 3
kmers = getAllKMers(K, tweets)
model = buildModel(kmers)

starting_kmers = getStartingKMers(K-1, tweets)
print starting_kmers
import sys
import csv
import numpy as np
from model_generator import getAllKMers, buildModel, getStartingKMers, getNextWord

def main(argv):

	#initialize array of tweets
	tweets = []

	#populate tweets array with contents of tweets file
	with open(argv[1], 'r') as tweetsfile:
		csvreader = csv.reader(tweetsfile, delimiter=',')
		for line in csvreader:
			tweets.append(line[-1])

	#DEFINE length of a single KMer
	K = 3

	#build Markov model
	kmers = getAllKMers(K, tweets)
	model = buildModel(kmers)
	starting_kmers = getStartingKMers(K-1, tweets)

	#begin loop to generate n novel tweets
	for i in range(100):

		#randomly pick a starting KMer
		sentence = starting_kmers[np.random.choice(range(len(starting_kmers)))]

		#generate rest of sentence using Markov chain
		for i in range(20):

			#select most recently-generated KMer
			current_phrase = tuple(sentence[-K + 1:])

			#get occurrence frequencies for most recent KMer
			frequencies = model[current_phrase]

			#generate the next word
			next_word = getNextWord(frequencies)

			#if no next word, end the sentence
			if next_word == None:
				break

			#append the next word to the sentence
			sentence.append(next_word)

		#flatten the sentence array into a string and print
		print " ".join(sentence)
	return

if __name__ == "__main__":
	main(sys.argv)
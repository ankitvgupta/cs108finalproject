import sys
import os.path
import csv
import numpy as np
from model_generator import getAllKMers, buildModel, getStartingKMers, getNextWord, getModelAndTweetsFromFile
from comparison import compareSentences

def generateSentenceFromStartingKmer(starting, K, numWords, model):
	sentence = starting
	#generate rest of sentence using Markov chain
	for j in range(numWords):
		#select most recently-generated KMer
		current_phrase = tuple(sentence[-K + 1:])

		#get occurrence frequencies for most recent KMer
		frequencies = model[current_phrase]

		#generate the next word
		next_word = getNextWord(frequencies)
		#print "Next:", next_word

		#if no next word, end the sentence
		if next_word == None:
			break

		#append the next word to the sentence
		sentence.append(next_word)

	#flatten the sentence array into a string and print
	return " ".join(sentence)

# Given two sentences as strings, matches their lengths.
def match_sentence_lengths(sentence1, sentence2):
	tokenized1 = sentence1.split(" ")
	tokenized2 = sentence2.split(" ")
	length_wanted = min(len(tokenized1), len(tokenized2))
	return " ".join(tokenized1[:length_wanted]), " ".join(tokenized2[:length_wanted])

def generateSentencesAndCheckErrors(infile, K):
	model, tweets = getModelAndTweetsFromFile(infile, K)
	res = []
	for i in range(10):
		random_tweet = np.random.choice(tweets)
		tweet_start = random_tweet.split(" ")[:K-1]
		num_words_wanted = len(random_tweet.split(" ")) - (K-1)
		generated_sentence = generateSentenceFromStartingKmer(tweet_start, K, num_words_wanted, model)
		updated_tweet, updated_generated_sentence = match_sentence_lengths(random_tweet, generated_sentence)
		#print "Updates", updated_tweet, updated_generated_sentence
		result = compareSentences(updated_tweet, updated_generated_sentence)
		res.append(result)
		sys.stdout.flush()
	print res
	return res

def checkIfSentenceInDatabase(sentence, tweets):
    return sentence in tweets

def main(infile, K):

	#initialize array of tweets
	model, tweets = getModelAndTweetsFromFile(infile, K)


	# tweets = []

	# fpath = os.path.join("../data/", infile)
	
	# #populate tweets array with contents of tweets file
	# with open(fpath, 'r') as tweetsfile:
	# 	csvreader = csv.reader(tweetsfile, delimiter=',')
	# 	for line in csvreader:
	# 		tweets.append(line[-1])

	# #build Markov model
	# kmers = getAllKMers(K, tweets)
	# model = buildModel(kmers)
	starting_kmers = getStartingKMers(K-1, tweets)

	#begin loop to generate n novel tweets
	#
	i = 0
	while i < 100:

		#randomly pick a starting KMer
		sentence = starting_kmers[np.random.choice(range(len(starting_kmers)))]
		generated_tweet = generateSentenceFromStartingKmer(sentence,K, 20, model)
		# If the tweet was one of the originals, get another one.
		if checkIfSentenceInDatabase(generated_tweet, tweets):
			continue
		print generated_tweet
		i += 1
		#print generateSentenceFromStartingKmer(sentence,K, 20, model)

        #print tmp
        #print generated_sentence
        #print checkIfSentenceInDatabase(sentence, tweets)
		# #generate rest of sentence using Markov chain
		# for j in range(20):

		# 	#select most recently-generated KMer
		# 	current_phrase = tuple(sentence[-K + 1:])

		# 	#get occurrence frequencies for most recent KMer
		# 	frequencies = model[current_phrase]

		# 	#generate the next word
		# 	next_word = getNextWord(frequencies)

		# 	#if no next word, end the sentence
		# 	if next_word == None:
		# 		break

		# 	#append the next word to the sentence
		# 	sentence.append(next_word)

		# #flatten the sentence array into a string and print
		# print " ".join(sentence)
	return

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print "Usage: model_test.py <tweet_data.csv> K"
		sys.exit(2)

	infile = sys.argv[1]
	K = int(sys.argv[2])

	#main(infile, K)
	generateSentencesAndCheckErrors(infile, K)

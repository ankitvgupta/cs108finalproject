import csv
import numpy as np
filename = "BarackObama_tweets.csv"

from model_generator import getAllKMers, buildModel, getStartingKMers, getNextWord


tweets = []

with open(filename, 'r') as tweetsfile:
	csvreader = csv.reader(tweetsfile, delimiter=',')
	for line in csvreader:
		tweets.append(line[-1])

K = 2
kmers = getAllKMers(K, tweets)
model = buildModel(kmers)

starting_kmers = getStartingKMers(K-1, tweets)
number_starting_kmers = len(starting_kmers)
for i in range(100):
	sentence = starting_kmers[np.random.choice(range(len(starting_kmers)))]
	for i in range(20):
		current_phrase = tuple(sentence[-K + 1:])
		frequencies = model[current_phrase]
		next_word = getNextWord(frequencies)
		if next_word == None:
			break
		sentence.append(next_word)
		#print sentence
		#print frequencies
	print " ".join(sentence)




print buildModel([["hello", "my", "name"], ["hello", "my", "dog"], ["here", "i", "am"], ["hello", "my", "dog"]])
#(hello, my) -> (name: 1), (dog: 2)
#(here, i) -> (am, 1)

# given a dictionary of word -> frequency mappings, returns a word proporirtional to its freqeuncy


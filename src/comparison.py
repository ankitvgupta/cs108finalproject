import nltk
import numpy as np
from nltk.corpus import wordnet
import string

def is_ascii(input_string):
	try:
		input_string.decode('ascii')
		return True
	except:
		return False

# Compare two words
# Returns the similarity, and whether the word was valid
def compareWord(word1, word2):
	#print "Words", word1, word2
	if (not is_ascii(word1)) or (not is_ascii(word2)):
		return 0., 0.
	word1_map = wordnet.synsets(word1)
	
	word2_map = wordnet.synsets(word2)
	#print word1_map
	#print word2_map
	if len(word1_map) > 0 and len(word2_map) > 0:
		if word1_map[0].wup_similarity(word2_map[0]) == None:
			return 0., 0.
		return word1_map[0].wup_similarity(word2_map[0]), 1
	return 0., 0.

# Returns a similarity score by compsaring corresponding words in sentences.
# Based loosely on http://www.cs.duke.edu/courses/spring14/compsci290/assignments/lab02.html
def compareSentences(sentence1, sentence2):
	sentence1 = sentence1.lower().translate(None, string.punctuation)
	sentence2 = sentence2.lower().translate(None, string.punctuation)

	words1 = sentence1.split(" ")
	words2 = sentence2.split(" ")
	assert(len(words1) == len(words2))
	total = 0
	numValids = 0
	for word1, word2 in zip(words1, words2):
		sim, isValid = compareWord(word1, word2)
		total += sim
		numValids += isValid
	if numValids == 0:
		return None
	else:
		return float(total) / float(numValids)

#print compareSentences("I really dislike climate change.", "I hate climate change much.")

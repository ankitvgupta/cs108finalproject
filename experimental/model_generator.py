#!/usr/bin/env python
# encoding: utf-8

from collections import defaultdict
import csv
import numpy as np
import os

def getAllKMers(K, list_of_strings):
    for string in list_of_strings:
        #tokenize string
        lst = string.split()

        #iterate through list and grab KMers
        for x in range (len(lst) - K + 1):
            yield lst[x:x+K]
            
def getStartingKMers(K, list_of_strings):
    results = []
    for string in list_of_strings:
        lst = string.split()

        results.append(lst[:K])
    return results

def buildModel(list_kmers):
    model = defaultdict(lambda : defaultdict(int))
    for kmer in list_kmers:
        current_words = tuple(kmer[:-1])
        next_word = kmer[-1]
        model[current_words][next_word] += 1
    return model

# Given a dictionary of word -> freq mappings, samples a word proprortional to its frequency
def getNextWord(freq_dictionary):
    words = freq_dictionary.keys()
    frequencies = np.array(freq_dictionary.values())
    if len(words) == 0:
        return None

    probabilities = frequencies/float(np.sum(frequencies))
    word = np.random.choice(words, size=1, p=probabilities)
    return word[0]

def getModelAndTweetsFromFile(infile, K):
    #initialize array of tweets
    tweets = []

    fpath = os.path.join("../data/", infile)
    
    #populate tweets array with contents of tweets file
    with open(fpath, 'r') as tweetsfile:
        csvreader = csv.reader(tweetsfile, delimiter=',')
        for line in csvreader:
            tweets.append(line[-1])

    #build Markov model
    kmers = getAllKMers(K, tweets)
    model = buildModel(kmers)
    return model, tweets

    


        
        
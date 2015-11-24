#!/usr/bin/env python
# encoding: utf-8

from collections import defaultdict
import csv
import numpy as np
# Given a string, get's K-mers of length K
#" dsf asfd adf asdf adsf asdf adsf adsf asdf"
# https://wiki.python.org/moin/Generators

# returns a generator for the KMers from a string
def getKMers(K, string):
    
    #tokenize string
    lst = string.split()
    
    #iterate through list and grab KMers
    for x in range (len(lst) - K + 1):
        yield lst[x:x+K]

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


    


        
        
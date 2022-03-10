#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 20:41:16 2022

@author: eyob
"""
import re
import nltk
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


s = input("Enter a sentences: ")
# print(s)
pattern = '\s'
tokens = re.split(pattern, s) # use split function to perform tokenization
# for token in tokens:
#     print(token)
for index in range(len(tokens)):
    tokens[index] = tokens[index].lower()
for token in tokens:
    print(token)

bigrams ={}
unigrams = {}
prev_word = "START"


tokenns=[]
for token in tokens:
    token = tokens.append(tokens)
    bigram = prev_word.append + ' ' + token
  
#print(bigram)
if token in unigrams:
    unigrams[token] +=1
else:
    unigrams[token] =1
  
#print(unigrams[word])
if bigram in bigrams:
    bigrams[bigram] += 1
else:
    bigrams[bigram] = 1
    prev_word = token

print(bigrams)
print(unigrams)

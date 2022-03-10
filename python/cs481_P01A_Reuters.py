#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 19:21:49 2022

@author: eyob
"""

import nltk
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


nltk.download('reuters')
nltk.download('stopwords')
nltk.download('punkt')

### Part 1 & 2
corpus = nltk.corpus.brown
stopWordsCorpus = nltk.corpus.stopwords.words('english')
words = corpus.words()
words = [w for w in words if w.lower() not in stopWordsCorpus]
frequencyDistribution = nltk.FreqDist(word.lower() for word in words) # note lowercasing with lower()
frequenciesAndWords = dict()
for word in words:
    frequenciesAndWords[word] = frequencyDistribution[word]

frequenciesAndWords = list(frequenciesAndWords.items())
frequenciesAndWords.sort(key = lambda a: a[1])
frequenciesAndWords.reverse()
labels, frequencies = map(list, zip(*frequenciesAndWords))

# first 10 words with their frequencies:
for index in range(10):
    print(labels[index] , ' ', frequencies[index])

labels2 = labels[:1000]
frequencies2 = frequencies[:1000]
fig, ax = plt.subplots()
xs = range(len(labels))
labels2 = range(len(labels))


### Part 3
def format_fn(tick_val, tick_pos):
    if int(tick_val) in xs:
        return labels2[int(tick_val)]
    else:
        return ''
ax.xaxis.set_major_formatter(format_fn)
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.plot(xs, frequencies, 'g')
ax.set_title('Token log frequency counts in Reuters ranked')
ax.set_xscale('log')
ax.set_yscale('log')
plt.xlabel('log(Rank)')
plt.ylabel('log(Frequency count)')
plt.show()

######### Part 4

word=corpus.words()
data= " ".join(word)
data = data.lower()
technical = "navigation"
nontechnical = "amazing"
t=data.count(technical)
d1=t/len(data)
n=data.count(nontechnical)
d2=n/len(data)
print("Technical probability is", d1)
print("Non-technical probability is", d2)
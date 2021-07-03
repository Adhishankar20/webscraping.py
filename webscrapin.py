#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer
import nltk
import matplotlib.pyplot as plt
import seaborn as sns

url = input("Enter the URL: ")
r = requests.get(url)
# Extract HTML 
html = r.text

# Create a BeautifulSoup object from the HTML
soup = BeautifulSoup(html, "html5lib")

# Get the text
text = soup.get_text()

# Create tokenizer
tokenizer = RegexpTokenizer('\w+')

# Create tokens
tokens = tokenizer.tokenize(text)

# Initialize new list
words = []

# Loop through list

for word in tokens:
	words.append(word.lower())
	
# Get English stopwords and print some of them
sw = nltk.corpus.stopwords.words('english')

# Initialize new list
words_ns = []

for word in words:
	if word not in sw:
		words_ns.append(word)

# plotting
freqdist1 = nltk.FreqDist(words_ns)
freqdist1.plot(25)
freq2 = dict(freqdist1)

k = ['good','bad','thank','way']
#f = [freq2.get(i) for i in k]
f = { i: freq2[i] for i in k }
f

print ("{:<5} {:<1} {:<20} {:<1} {:<4}".format('S.no',"|", 'Words',"|",'Count'))
print('------------------------------------')
c = 0
for words, count in f.items():
    c += 1
    words, count = words, count
    print("{:<5} {:<1} {:<20} {:<1} {:<4}".format(c,"|", words,"|", count))



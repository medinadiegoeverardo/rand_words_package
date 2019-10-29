"""

1st function

random "sentence" generator (not coherent sentence)
(more like random combination of words)

select number of words and a range of letters from a list of dictionary downloaded from the web;
dictionary is in chronological order. there are rougly 25,500 words in dictionary

if you would like to use 10 words that start with L, to words that start with Z,
format would look something like this:

function(number_of_words=, from=, to=):
"""

import requests
import pandas as pd
import numpy as np

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = requests.get(word_site)
WORDS = response.content.splitlines()

# there are 25, 487 words in dictionary (chronological). select numerical range
# to see what random combination of words you get within that range (500 to 13,000)
# for reference: letter L is in the middle, roughly 12,000

def select_make_sentence(number_of_words, first_word_number=0, last_word_number=len(WORDS)):
    numbers = []
    byte_sentence = []
    sentence = []
    for i in range(0, number_of_words):
        numbers.append(np.random.randint(first_word_number, last_word_number))
    for i in numbers:
        byte_sentence.append(WORDS[i])
    for sent in byte_sentence:
        sentence.append(sent.decode('ASCII'))
    return " ".join(sentence)
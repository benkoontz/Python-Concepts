# Word Frequency counter program
# This program counts all of the words on a webpage and stores them in a dictionary

import requests # used to download info from a webpage
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list = []
    source_code = requests.get(url).text # connect to webpage and use it as plaintext
    soup = BeautifulSoup(source_code)
    for post_text in soup.findAll('a', {'class': 'mw-jump-link'}):
        content = post_text.string
        words = content.lower().split() # lowerclass everything and split splits of the string based on spaces
        for each_word in words:
            word_list.append(each_word)
    clean_up_list(word_list)

# method to remove symbols from words
def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = "!@#$%^&*()_+{}:<>?,./;'[]-='"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "") # replace the symbol with a blank space
        if len(word) > 0:
            clean_word_list.append(word)
    create_dictionary(clean_word_list)


def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            #item get gets item from dictionary to sort by
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):# first paramater is what you want to sort
        print(key, value)

start('https://en.wikipedia.org/wiki/Anchor_text')

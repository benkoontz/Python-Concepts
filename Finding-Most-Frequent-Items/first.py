# Finding Most frequent items

from collections import Counter

text = "blah ben tuna fish ben blah tuna tuna " \
       "ben ben tuna tuna tuna blah hello alright"

words = text.split()
print(words) # print list of words

counter = Counter(words)
top_three = counter.most_common(3) # print top 3 most common words
print(top_three)

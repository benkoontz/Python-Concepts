# Zip returns is used to return tuples

first = ['Bucky', 'Tom', 'Taylor']
last = ['Roberts', 'Hanks', 'Swift']

names = zip(first, last) # take first list and last list and tie them together, then store them in names


for a, b in names:
    print(a,b)

# outputs
# Bucky Roberts
# Tom Hanks
# Taylor Swift

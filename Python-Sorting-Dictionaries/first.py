# how to get min and max of dictonary
# how to sort a dictionary

stocks = {'GOOG': 520.54,
          'FB': 76.45,
          'YHOO': 39.28,
          'AMZN': 306.21,
          'AAPL': 99.76
}
print(min(zip(stocks.values(), stocks.keys()))) # get minimum value of zip list
print(max(zip(stocks.values(), stocks.keys()))) # get max value of zip list
print(sorted(zip(stocks.values(), stocks.keys()))) # sort by stock price values
print(sorted(zip(stocks.keys(), stocks.values()))) # sort alphabetically

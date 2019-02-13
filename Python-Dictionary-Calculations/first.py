# dictionary calculations


stocks = {
    'GOOG': 434,
    'AAPL': 325,
    'FB': 54,
    'AMAZN': 623,
    'F': 32,
    'MSFT': 549
}

print(min(stocks))

# (434, GOOG) (325, AAPL)
min_price = min(zip(stocks.values(), stocks.keys()))
print(min_price) 

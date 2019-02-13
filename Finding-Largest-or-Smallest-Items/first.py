# Finding largest or smallest items

import heapq  # allows you to sort items

grades = [32, 43, 654, 32, 132, 66, 99, 532]

print(heapq.nlargest(3, grades)) # print three largest values in grades

stocks = [
{'ticker': 'AAPL', 'price': 201},
{'ticker': 'GOOG', 'price': 800},
{'ticker': 'F', 'price': 54},
{'ticker': 'MSFT', 'price': 313},
{'ticker': 'TUNA', 'price': 68}

]

print(heapq.nsmallest(2, stocks, key = lambda stock: stock['price']))
# prints [{'ticker': 'F', 'price': 54}, {'ticker': 'TUNA', 'price': 68}]

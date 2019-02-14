players = [29, 58, 66, 71, 87]
print(players[2]) # prints 66

players[2] = 68;
print(players[2]) # changes 66 to 68

print(players + [90, 91, 98]) # adds numbers at end of list but not permanently

players.append(120) # permanently adds 120 to the end of the list
print(players)

print(players[:2]) # prints 29 and 58

players[:2] = [0,0]
print (players) # changes first two values to 0 permanently

players[:2] = [] #removes the first two 0's in the list
print (players)

players[:] = [] #empties the list
print (players)

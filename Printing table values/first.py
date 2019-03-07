number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[1][2]) #prints 6

# prints every value in the table
for row in number_grid:
    for col in row:
        print(col)

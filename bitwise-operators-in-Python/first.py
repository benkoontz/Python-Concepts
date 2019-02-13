# bitwise operators in Python

# -------- binary and --------

a = 50      # 110010
b = 25      # 011001
c = a & b   # 010000

print(c) # prints 16

# -------- binary right shift -------- # T
x = 240     # 11110000
y = x >> 2 # shift every bit two spots to the right 00111100

print(x)   # prints 240
print(y)   # prints 60

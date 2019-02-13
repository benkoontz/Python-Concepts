# Whenever you have to work with bytes you can use pack and unpack from struct

from struct import *

# store as bytes data
packed_data = pack('iif', 6, 19, 4.73) # two integers and a float

print(packed_data)

print(calcsize('i')) # 4 bytes for integer
print(calcsize('f')) # 4 bytes for float
print(calcsize('iif')) # 12 bytes for two ints and a float

# to get data back to normal
original_data = unpack('iif', packed_data)
print(original_data)

print(unpack('iif', b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@')) # prints 6, 19, 4.73

# Sorting Custom objects

from operator import attrgetter

class User:

    def __init__(self, x, y):
        self.name = x
        self.user_id = y

    def __repr__(self):
        return self.name + ": " + str()


users = [


User('Bucky', 43),
User('Sally', 5),
User('Tuna', 61),
User('Brian', 2),
User('Joby', 77),
User('Amanda', 9),


]

for user in users:
    print(user)

print('-------')
for user in sorted(users, key = attrgetter('name')): # sort by name alphabetically
    print(user)

print('-------')
for user in sorted(users, key = attrgetter('user_id')): # sort by id from smallest to largest
    print(user)

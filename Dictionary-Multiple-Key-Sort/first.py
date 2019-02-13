# Dictionary Multiple Key Sort

from operator import itemgetter

users = [
     {'fname': 'Bucky', 'lname': 'Roberts'},
    {'fname': 'Tom', 'lname': 'Roberts'},
    {'fname': 'Bernie', 'lname': 'Zunks'},
    {'fname': 'Jenna', 'lname': 'Hayes'},
    {'fname': 'Sally', 'lname': 'Jones'},
    {'fname': 'Amanda', 'lname': 'Roberts'},
    {'fname': 'Tom', 'lname': 'Williams'},
    {'fname': 'Dean', 'lname': 'Hayes'},
    {'fname': 'Bernie', 'lname': 'Barbie'},
    {'fname': 'Tom', 'lname': 'Jones'}

]

for x in sorted(users, key = itemgetter('fname')): # sort only by first name
    print(x)

print('------')
for x in sorted(users, key = itemgetter('fname', 'lname')): # sort by first and last name
    print(x)


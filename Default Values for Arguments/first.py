# default values for arguments

def get_gender(gender = 'unknown'):
    if gender is 'm':
        gender = "male"
    elif gender is 'f':
        gender = "female"
    print (gender)

get_gender('m') # prints male
get_gender('f') # prints female
get_gender() # prints unknown

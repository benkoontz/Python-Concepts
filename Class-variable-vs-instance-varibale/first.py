# class variable vs instance variable
# a class variable is anytime you create an object from a class it's the varibales the class has by default
# an instance varable is unique to a specific instance of a class

class Girl:

    gender = 'female'

    def __init__(self, name):
        self.name = name

r = Girl('Rachel') 
s = Girl('Serah') 
print(r.gender) # prints female
print(s.gender) # prints female
print(r.name) # prints Rachel
print(s.name) # prints Serah

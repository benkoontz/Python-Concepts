#Inherticance is a way to use methods and fields from one class in another class

class Parent ():
    def print_last_name(self):
        print('Roberts')

class Child(Parent): # tell Python to pass inherit print_last_name
    def print_first_name(self):
        print('Bucky')

    def print_last_name(self): # overide the last name in the Parent function
        print('Sniztzelberg')

bucky = Child()
bucky.print_first_name()
bucky.print_last_name()

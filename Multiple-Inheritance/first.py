#Multiple Inhertitance is a way to inherit from more than one class

class Mario():
    def move(self):
        print('I am moving')

class Shroom():
    def eat_shroom(self):
        print('now i am big')

class BigMario(Mario, Shroom): # contains Mario and Shroom classes
    pass # used to not create anything in the class

bm = BigMario()
bm.move()
bm.eat_shroom()

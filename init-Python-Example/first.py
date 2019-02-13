# init is a special kind of function that gets called automatically


class Enemy:
    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)

Jason = Enemy(5)
sandy = Enemy(18)

Jason.get_energy() # returns 5
sandy.get_energy() # returns 18

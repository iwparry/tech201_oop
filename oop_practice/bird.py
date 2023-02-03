from animal import Animal

class Bird(Animal):

    def __init__(self):
        super().__init__()
        self.feathers = True
        self.beak = True
        self.wings = True
    def lay_eggs(self):
        print("I won't start counting chicks just yet")
    def mate(self):
        print("Find a mate")
    def peck(self):
        print("Check how sharp my beak is!")
barry = Bird()
# barry.eat()
# barry.peck()
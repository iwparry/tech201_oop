# Practicing Python OOP

class Animal:
    def __init__(self):
        self.limbs = None
        self.eyes = True
        self.lungs = True
        self.brain = True
    def breathe(self):
        print("Breathe in, breathe out")
    def eat(self):
        print("Mmm tasty!")
    def move(self):
        print("I need to go for a walk")

donkey = Animal()
# donkey.breathe()
# donkey.eat()
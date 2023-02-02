# Polmorphism

from snake import Snake

class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True     # General note with class variables, they MUST be set
        self.venom = False
        self.two_lungs = True

    def digest_large_prey(self):
        print("Ok let me get my stretchy pants")

    def constrict(self):
        print("Squeeeeeeeze")

    def climb(self):
        print("Look at me going up the ladder!")

    def shed_skin(self):
        print("I'm growing out of this now")

peter = Python()
peter.eat() # from Animal
peter.hunt() # from Reptile
peter.use_tongue_to_smell() # from Snake
peter.constrict() # from self
# Inheritance

from animal import Animal

class Reptile(Animal):    # We include our base class 'Animal' which is the superclass to Reptile

    def __init__(self):
        super().__init__()   # This is important, initialise with the superclass attributes first
        self.cold_blooded = True
        self.tetrapod = None # Not all reptiles are tetrapod
        self.heart_chambers = [3,4]
        self.amniotic_eggs = None

    def seek_heat(self):
        print("Its chilly outside, where is the sun?")

    def hunt(self):
        print("Wait, wait, wait ... Pounce")

    def use_venom(self):
        print("If I've got it, I'm going to use it")

    def attract_through_scent(self):
        print("Come take a whiff darling ;)")

jeremy_the_reptile = Reptile()
# jeremy_the_reptile.breathe()    # Animal class method
# jeremy_the_reptile.hunt()       # Reptile class method
# jeremy_the_reptile.eat()        # Animal class method
# jeremy_the_reptile.attract_through_scent()   # Reptile class method
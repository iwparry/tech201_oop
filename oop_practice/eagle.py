from bird import Bird

class Eagle(Bird):
    def __init__(self):
        super().__init__()
        self.powerful_vision = True
        self.talons = True
        self.curved_beak = True
    def defend_territory(self):
        print("Not in my house!")
    def hunt(self):
        print("Steady...steady...DIVE!")
    def sharpen_beak(self):
        print("Good to go!")

earnie = Eagle()
earnie.peck()
earnie.eat()
earnie.defend_territory()
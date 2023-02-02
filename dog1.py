# Initialisation

# Initialisation -> Setting particular data for an instance of a class

class Dog:

#    animal_kind = "canine"     # this can still be overwritten for all class instances

    def __init__(self, name, colour): # any instance created will require arguments name and colour
        self.animal_kind = "Canine"   # insert into our initialisation
        self.name = name
        self.colour = colour

    def bark(self):
        return "woof"

# __init__() - used to initialise a newly created object. It is called every time the class in instantiated
fido = Dog("Fido", "Brown")  # because we now need to specify a name and colour for our dog, fido
lassie = Dog("Lassie", "Brown")

print(fido.name) # prints "Fido"
print(fido.colour) # prints "Brown"
print(fido.animal_kind) # prints "Canine" because we initialised this in our class

Dog.animal_kind = "Donkey" # this will not overwrite animal_kind class variable because we initialised the class variable
print(lassie.animal_kind) # prints "Canine" - not to say we cannot still create instance variables

# Initialising classes with class variables is good practice. Can still do the first way but it is not advised
# Object-Oriented Programming (OOP)

# Everything in OOP is an object and objects are modelled against real world objects.

# Classes are the templates we use to create objects
# Classes are a way of bringing both data and functionality of our code together

class Dog:         # template

    animal_kind = "canine" # class Variable

    def bark(self):   # method
        print(self.animal_kind)
        return "woof"

# self - referring to the current class - in this case dog

# print(Dog.animal_kind)  # prints "canine"
# print(Dog.bark()) # ERROR

# Instantiation -  the class we made earlier is a template, we need to actually make the class in order to use it
fido = Dog()    # here we have created two instances
lassie = Dog()
# print(fido.bark()) # prints "canine" and "woof"
# print(lassie.bark()) # prints same
#
# print(type(fido)) # prints <class '__main__.Dog'>
# print(type(lassie)) # same
#
# print(fido.animal_kind) # prints "canine"
# print(lassie.animal_kind) # same

fido.animal_kind = "Big Dog"  # changes the class variable for the instance "fido"

# print(fido.animal_kind)  # prints "Big Dog"
# print(lassie.animal_kind) # prints "canine"

Dog.animal_kind = "Dolphin"   # changes the class variable for the template - Instance variable

print(fido.animal_kind) # we already overwrote the specific instance fido thus overwriting the template will not change
print(lassie.animal_kind)  # prints Dolphin because we had overwritten the template for class Dog

# The Dog can still access their method
print(fido.bark())
print(lassie.bark())


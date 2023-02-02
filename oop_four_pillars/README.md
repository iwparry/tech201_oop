# OOP Four Pillars

### What is OOP?
**Object-Oriented Programming** is a programming model based on the concept of "objects", which can contain data and code.
The object can be bases on a blueprint or parent which defines properties and methods it inherits and has access to and can use.
An example of a blueprint or parent that objects inherit from would be "classes".
![](classes_diagram.png)

### The Four Pillars of OOP
OOP has 4 main theoretical principles which are:
- Abstraction
- Inheritance
- Encapsulation
- Polymorphism
### Abstraction
Abstraction is the concept of hiding all the implementation of your class away from anything outside of the class.
```python
class Animal:   # In the class we can see all the attributes and methods we've set
    def __init__(self):    # But the user does not need to see these
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True
    def breathe(self):
        print("One breath in, one breath out")

    def eat(self):
        print("Nom Nom Nom")
        
    def procreate(self):
        print("Find a mate")

    def move(self):
        print("Onwards and Upwards")
```
### Inheritance
Inheritance is the mechanism for creating a child class (subclass) that can inherit behaviour and properties from a parent class (superclass).
```python
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
jeremy_the_reptile.breathe()    # Animal class method
jeremy_the_reptile.hunt()       # Reptile class method
```
### Encapsulation
Encapsulation is the method of keeping all the state, variables, and methods private unless declared to the user
```python
from reptile import Reptile

class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.venom = None
        self.limbs = False

    def use_tongue_to_smell(self):
        print("Do I say it smells or tastes nice?")

sidney = Snake()
sidney.hunt()     # Reptile class method, the user does not need to see how it works
```
### Polymorphism
Polymorphism is a way of interfacing with objects and receiving different results.
```python
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
```
### What are the Benefits of OOP?
The benefits of OOP include:
- Modularity
- Reusability
- Flexibility
- Security 
- Easily upgradable and scalable
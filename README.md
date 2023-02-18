# Tech 201 Object-Oriented Programming
## What is Object-Oriented Programming(OOP)?
**Object-Oriented Programming**, or simply OOP, is a programming model based on the concept of "objects", which can contain data and code.
Everything in OOP is an object and objects are modelled against real world objects.
Take a car for example, a car is an object, and it possesses several attributes such as colour, style, make. A car also exhibits several behaviours such as accelerate, brake, steer.
In OOP we model our "objects" in the same way.
## Classes
Of course in OOP we need a way to create our objects, fortunately we have a way to make a template that we use to create objects, we do this via **classes**.
As said previously classes are templates that we use in order to create objects.
Classes are a way of bringing both data and functionality of our code together. So how do we create a class?
```python
class ClassName: # how we create a class
    pass # classes require indentation like functions etc.
```
If we look back earlier in our documentation with the car example, we mentioned that a car is an object and it possesses several attributes and behaviours. In Python, when creating these classes we represent these attrubites and behaviours via class variables and methods respectively.
```Python
class ClassName:

    class_variable = "I am a Class Variable!"

    def class_method(self):
        return "I am a Class Method!"
# self - referring to the current class
```
In Python, class variables are defined outsode all methods and have the same value for every instance of the class. Methods are functions that are defined as part of the class. It is common practice that the first argument of any method that is part of a class is the object itself, hence this argument is called `self`.

As we mentioned previously, classes are templates we use to create objects. So how do we create the objects? We do this via Instantiation, this way we can actually use the object. To create a class instance we simply do the following:
```Python
class Class():
    pass
# Class Instantiation
class_instance = Class()
```
There is no limit on how many intsances of a class we can make either, as long as we have the template we can make as many objects as we want.

Classes also have an "init" method that needs to be called every time a class is instantiated. 
```Python
class ClassName:
    def __init__(self, class_var):
        self.class_var = class_var
```
When a class instance is created, the instance variable 'class_var' is created and set to the input value.
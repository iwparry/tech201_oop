# Methods

class MethodExamples:

#    this_can_be_easily_accessed = "Hi, I'm easily found!"  # moved to __init__()

    def __init__(self):
        self.this_can_be_easily_accessed = "Hi, I'm easily found!"

x = MethodExamples()  # instance of class

print(x.this_can_be_easily_accessed)  # prints "Hi, I'm easily found!"
x.this_can_be_easily_accessed = "I have been changed!"
print(x.this_can_be_easily_accessed)  # prints changed class variable

# Public and Private
# class MethodExamples:
#
# #    this_can_be_easily_accessed = "Hi, I'm easily found!"  # moved to __init__()
#
#     def __init__(self):
#         self._this_can_be_easily_accessed = "Hi, I'm easily found!"
#
#     def get_this_can_be_easily_accessed(self):
#         return self.this_can_be_easily_accessed
#
#     def set_this_can_be_easily_accessed(self, value_to_be_set):
#         self.this_can_be_easily_accessed = value_to_be_set
#
#
# x = MethodExamples()  # instance of class
#
# print(x._this_can_be_easily_accessed)  # prints "Hi, I'm easily found!"
# x.set_this_can_be_easily_accessed = "I have been changed!"
# print(x._this_can_be_easily_accessed)  # prints changed class variable
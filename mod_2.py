import mod_1

print("This is mod 2's name -> " + __name__)
# will not run the program in mod_1 because we have currently set our function
# in mod_1 to execute only if its being ran directly in mod_1
# hence it won't run in any other file
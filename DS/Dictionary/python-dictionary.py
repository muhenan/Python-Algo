from collections import defaultdict

"""
A defaultdict is a class from the collections module that is a subclass of dict.

It allows you to specify a default value or factory function that is used when accessing a missing key.

This means that if you try to access a key that doesn't exist, instead of raising a KeyError, 
the defaultdict will return the default value or value returned by the factory function.
"""
my_dictionary = defaultdict(int) # must be a type or lamda
print(my_dictionary[4])

my_dictionary = defaultdict(list)
print(my_dictionary[4])

my_dictionary = defaultdict(bool)
print(my_dictionary[4])

my_dictionary = defaultdict(lambda : -1)
print(my_dictionary[4])

my_dictionary = defaultdict(lambda : True)
print(my_dictionary[4])

my_dictionary = defaultdict(lambda : "xx")
print(my_dictionary[4])
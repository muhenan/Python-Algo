import bisect

my_array = [1,4,6,8,10,13]

print(bisect.bisect(my_array, 0))
print(bisect.bisect(my_array, 1))
print(bisect.bisect(my_array, 2))
print(bisect.bisect(my_array, 4))
print(bisect.bisect(my_array, 14))

"""
for bisect.bisect

for example
we try to find x
return the index of the first element which is larger that x
even if x is literally in the array, return the bigger one

"""

my_array = [1,4,6,8,10,13]

print(bisect.bisect_left(my_array, 0))
print(bisect.bisect_left(my_array, 1))
print(bisect.bisect_left(my_array, 2))
print(bisect.bisect_left(my_array, 4))
print(bisect.bisect_left(my_array, 14))

"""
for bisect_left

if found that one, return the index
if no, return the larger one
"""

my_array = [1,4,6,8,10,13]

print(bisect.bisect_right(my_array, 0))
print(bisect.bisect_right(my_array, 1))
print(bisect.bisect_right(my_array, 2))
print(bisect.bisect_right(my_array, 4))
print(bisect.bisect_right(my_array, 14))
"""
same as bisect, always return the larger one
"""


"""
Note:

DO NOT USE BISECT

ALWAYS USE BISECT_LEFT OR BISECT_RIGHT

left means return the exact one
right means always return the larger one

"""

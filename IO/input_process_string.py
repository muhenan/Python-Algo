"""
input is simply string

after we get strings, all we need to do is
processing string

So within python, processing input is literally processing string
"""

line = "  34 34 56 1 3  \n"

line = line.strip()
print(line)
# strip, remove the leading and trailing whitespaces

print(line.split())
# split, return a list of string

# to get int, we have to convert string to int
numbers = [int(number) for number in line.split()]

# parse the array, get specific values
a, b, c, d, e = [int(number) for number in line.split()]
# list to variables

print(numbers)
print(a)
print(d)
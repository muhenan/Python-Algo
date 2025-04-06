import copy
from bisect import *

print("hello")

a = 1
b = 2
c = 3

# b, a = c, b
a, b = b, a # swap

print(a,b,c)


res = ["", ""] * 5 # ['', '', '', '', '', '', '', '', '', '']
print(res)

res = ["" for i in range(5)] # quicker ['', '', '', '', '']
print(res)

scores = [3,2,1,5,0,8]

print(scores)
print(scores[1:3]) # [1, 3) 左闭右开

arr = list(enumerate(scores)) # [(0, 3), (1, 2), (2, 1), (3, 5), (4, 0), (5, 8)]
print(arr)

# key (Optional) - A function that serves as a key for the sort comparison. Defaults to None.
arr = sorted(list(enumerate(scores)), key= lambda x : x[1], reverse=True)
print(arr)

# sorted(arr) Return a new list

for index, element in arr:
    print(index, element)

for i, (index, element) in enumerate(arr):
    print(i, index, element)

for i in range(len(arr)):
    print(i, arr[i], arr[i][0])


sortedArr = [0,1,2,3,3,3,5,6]
print(sortedArr)

print(bisect_left(sortedArr, 4))
print(bisect_right(sortedArr, 4))


tupleOfMine = (2,3,4)
print(tupleOfMine)
print(tupleOfMine[1])



import heapq
myHeap = []
heapq.heapify(myHeap)

class Node:
    def display(self):
        print("hhhh")

heapq.heappush(myHeap, (3, Node()))
heapq.heappush(myHeap, (4, Node()))
heapq.heappush(myHeap, (1, Node()))



print(myHeap)


my_dict = dict()
print(my_dict.get(0))


print(copy.deepcopy([2]))
print(copy.deepcopy([]))



#####################################################


import sys
# import numpy as np
# import pandas as pd
# from sklearn import ...
my_index = 0
my_rates = []
sc = 'x'
tc = 'c'
for line in sys.stdin:
    line = line.replace("\n", "")
    #print(line, end="")
    #print(my_index)
    if my_index == 0:
        rates = line.split(';')
        for r in rates:
            my_rates.append(r.split(','))
    elif my_index == 1:
        sc = line
    else:
        tc = line
    my_index += 1
#print(my_rates)
#print(sc)
#print(tc)


#######################################################


import sys

class Node:
    def __init__(self, currency, val):
        self.currency = currency
        self.val = val

def find(map, original, target, value, visited, max_value):
    if original in visited:
        return -1.0  # if got into a loop
    if original not in map:
        return -1.0  # if original doesn't exist

    if original == target:
        return value  # if found the target

    visited.add(original)
    # iterate through all possible transactions
    for next_node in map[original]:
        sub = find(map, next_node.currency, target, value * next_node.val, visited, max_value)
        max_value[0] = max(max_value[0], sub)  # update the max value

    visited.remove(original)
    return max_value[0]

map = {}  # store all the currencies and their forwarding currency
counter = 0
original = ""  # store the original currency
target = ""  # store the target currency
separate = []  # store the separated transactions in line 0

for line in sys.stdin:
    line = line.strip()

    if counter == 0:
        separate = line.split(";")
    elif counter == 1:
        original = line
    else:
        target = line

    counter += 1

for s in separate:
    trans = s.split(",")
    from_currency = trans[0]
    to_currency = trans[1]
    value = float(trans[2])

    # create a new node for 'from_currency' if it doesn't exist
    if from_currency not in map:
        map[from_currency] = []

    # connect 'from_currency' to 'to_currency'
    map[from_currency].append(Node(to_currency, value))

    # create a new node for 'to_currency' if it doesn't exist
    if to_currency not in map:
        map[to_currency] = []

max_value = [-1.0]  # initial double that stores the maximum transaction value achieved
result = find(map, original, target, 1, set(), max_value)
print(result)

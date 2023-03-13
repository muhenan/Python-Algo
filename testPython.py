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
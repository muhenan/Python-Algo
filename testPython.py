from bisect import *

print("hello")

a = 1
b = 2
c = 3

# b, a = c, b
a, b = b, a

print(a,b,c)


res = ["", ""] * 5
print(res)

res = ["" for i in range(5)] # quicker
print(res)

scores = [3,2,1,5,0,8]

print(scores)
print(scores[1:3])

arr = list(enumerate(scores))
print(arr)

# key (Optional) - A function that serves as a key for the sort comparison. Defaults to None.
arr = sorted(list(enumerate(scores)), key= lambda x : x[1], reverse=True)
print(arr)

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
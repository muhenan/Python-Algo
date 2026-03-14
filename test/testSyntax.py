import math

print(math.sqrt(2))
print(math.floor(2.5))


arr = [2,3,4]

print(arr)

arr.pop(0)

print(arr)
arr.pop()

print(arr)


strings = ["a", "b", "c"]
print("-".join(strings))

for i in range(5 + 1, -1, -1):
    print(i)
# all()

number = 1
lists = [[0,1,2], [1,3], [0,1]]
print([number in curr_list for curr_list in lists])

# 1
print(all(number in curr_list for curr_list in lists))

# 2
print(all([number in curr_list for curr_list in lists]))


test = 10
print(test)
for i in range(5):
    test += i
print(test)

max_end = 1000_000
print(max_end)
print(max_end < 9998340)
my_list = [[3, 1, 4], [1, 5, 9], [1, 6, 9], [2, 6, 5], [3, 5, 8]]
print(my_list)

# ascending
my_list.sort(key=lambda x: x[0])  # Sort based on the first element of each inner list
print(my_list)

# for 1st element, ascending; for 2nd element, descending
my_list.sort(key=lambda x: (x[0], -x[1]))
print(my_list)

# without using extra space

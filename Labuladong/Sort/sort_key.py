my_list = [[3, 1, 4], [1, 5, 9],[1, 6, 9], [2, 6, 5], [3, 5, 8]]

# 从小到大
my_list.sort(key=lambda x: x[0])  # Sort based on the first element of each inner list

print(my_list)

# 第一个从小到大，第二个从大到小
my_list.sort(key=lambda x: (x[0], -x[1]))

print(my_list)

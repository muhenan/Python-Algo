

def print_matrix(arr_2d, index , res):
    if len(arr_2d) % 2 == 1 and index == len(arr_2d) // 2:
        res.append(arr_2d[index][index])
        return res
    if len(arr_2d) % 2 == 0 and index == len(arr_2d) // 2:
        return res
    for i in range(index, len(arr_2d) - index - 1):
        res.append(arr_2d[index][i])
    for i in range(index, len(arr_2d) - index - 1):
        res.append(arr_2d[i][len(arr_2d) - index - 1])
    for i in range(index, len(arr_2d) - index - 1):
        res.append(arr_2d[len(arr_2d) - index - 1][len(arr_2d) - 1 - i])
    for i in range(index, len(arr_2d) - index - 1):
        res.append(arr_2d[len(arr_2d) - 1 - i][index])
    print_matrix(arr_2d, index + 1, res)
    return res

res = []
print_matrix([[1,2,3],[4,5,6],[7,8,9]], 0, res)
print(res)
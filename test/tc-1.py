# Ascending order
def partition(num, left, right):
    pivot = num[right]
    index = left
    for i in range(left, right):
        if num[i] < pivot:
            num[i], num[index] = num[index], num[i]
            index += 1
    num[index], num[right] = num[right], num[index]
    return index

def top_k(num, k):
    k = len(num) - k
    left = 0
    right = len(num) - 1
    while left < right:
        index = partition(num, left, right)
        if index == k:
            break
        elif index < k:
            left = index + 1
        else:
            right = index - 1
    return num[k]

# Descending order
def partition_descending(num, left, right):
    pivot = num[right]
    index = left
    for i in range(left, right):
        if num[i] > pivot:
            num[i], num[index] = num[index], num[i]
            index += 1
    num[right], num[index] = num[index], num[right]
    return index

def top_k_descending(num, k):
    k -= 1
    left = 0
    right = len(num) - 1
    while left < right:
        index = partition_descending(num, left, right)
        if index == k:
            break
        elif index < k:
            left = index + 1
        else:
            right = index - 1
    return num[k]


if __name__ == "__main__":
    test_cases = [
        {"nums": [2, 4, 1, 6], "k": 2, "expected": 4},
        {"nums": [3, 2, 1, 5, 6, 4], "k": 2, "expected": 5},
        {"nums": [3, 2, 3, 1, 2, 4, 5, 5, 6], "k": 4, "expected": 4},
        {"nums": [7], "k": 1, "expected": 7},
        {"nums": [5, 5, 5, 5], "k": 3, "expected": 5},
        {"nums": [9, 1, 8, 2], "k": 1, "expected": 9},
        {"nums": [9, 1, 8, 2], "k": 4, "expected": 1},
    ]
    descending_test_cases = [
        {"nums": [2, 4, 1, 6], "k": 2, "expected": 4},
        {"nums": [3, 2, 1, 5, 6, 4], "k": 2, "expected": 5},
        {"nums": [3, 2, 3, 1, 2, 4, 5, 5, 6], "k": 4, "expected": 4},
        {"nums": [7], "k": 1, "expected": 7},
        {"nums": [5, 5, 5, 5], "k": 3, "expected": 5},
        {"nums": [9, 1, 8, 2], "k": 1, "expected": 9},
        {"nums": [9, 1, 8, 2], "k": 4, "expected": 1},
    ]

    for i, case in enumerate(test_cases, 1):
        ans = top_k(case["nums"][:], case["k"])
        print(f"top_k case {i}: nums={case['nums']}, k={case['k']}, ans={ans}")
        assert ans == case["expected"]

    for i, case in enumerate(descending_test_cases, 1):
        ans = top_k_descending(case["nums"][:], case["k"])
        print(f"top_k_descending case {i}: nums={case['nums']}, k={case['k']}, ans={ans}")
        assert ans == case["expected"]

    print("all passed")

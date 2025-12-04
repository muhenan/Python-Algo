def heapify(arr, n, i):

    largest = i  # 初始化最大值为根节点
    left = 2 * i + 1  # 左子节点索引
    right = 2 * i + 2  # 右子节点索引

    # 如果左子节点存在且比根节点大
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 如果右子节点存在且比当前最大值大
    if right < n and arr[right] > arr[largest]:
        largest = right

    # 如果最大值不是根节点，交换并继续调整
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换
        heapify(arr, n, largest)  # 递归调整子树


def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):  # 从最后一个非叶子节点开始调整
        heapify(arr, n, i)

    # 2. 依次取出堆顶元素，放到数组末尾
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # 将堆顶元素与最后一个元素交换
        heapify(arr, i, 0)  # 重新调整堆，排除最后一个元素

    return arr

def print_heap(arr):
    if len(arr) == 0:
        return
    print(arr[0])
    if len(arr) == 1:
        return
    start = 1
    while True:
        for i in range(start, 2 * start + 1):
            if i == len(arr):
                return
            else:
                print(arr[i], end=" ")
        print()
        start = start * 2 + 1

# 测试代码
if __name__ == "__main__":
    arr = [4, 10, 0, 3, 9, 3, 5, 1,12]
    print_heap(arr)
    print("原始数组:", arr)
    sorted_arr = heap_sort(arr)
    print("排序后数组:", sorted_arr)
    print_heap(arr)
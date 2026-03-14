lst = [4,3,2,9,3,8,2,7]

def quicksort(nums,l,r):
    if l>=r:
        return
    idx = partition_a(nums,l,r)
    quicksort(nums,l,idx-1)
    quicksort(nums,idx+1,r)


def partition_d(nums,l,r):
    """
    版本 1：
    - pivot 选最右边 nums[r]
    - i 从左往右扫
    - j 表示“下一个应该放 > pivot 的位置”

    这个 partition 结束后：
    - nums[l : j] 都是 > pivot
    - nums[j] 是 pivot
    - nums[j + 1 : r] 都是 <= pivot

    注意：
    这个写法分出来的是“降序 partition”风格，
    因为它把 > pivot 的数放到了左边。
    """
    pivot = nums[r]
    j = l
    # range(l, r) 不会遍历到 r，因为 r 位置本身就是 pivot
    for i in range(l,r):
        # 如果当前数比 pivot 大，就应该被放到左边那一堆
        if nums[i]>pivot:
            nums[j],nums[i] = nums[i],nums[j]
            j += 1
    # 扫描结束后，把 pivot 放到中间分界点 j
    nums[r],nums[j] = nums[j],nums[r]
    print(nums)
    return j

"""
重中之重
从小到大排序的 partition 函数，pivot 选最右边的元素
j 是大于 pivot 的元素的第一个位置，是要换掉的位置
"""

def partition_a(nums, l, r):
    """
    版本 2：
    - pivot 选最左边 nums[l]
    - i 从右往左扫
    - idx 表示“下一个应该放 > pivot 的位置”

    这个 partition 结束后：
    - nums[l : idx] 都是 <= pivot
    - nums[idx] 是 pivot
    - nums[idx + 1 : r] 都是 > pivot

    这是当前 quicksort() 真正在调用的版本。
    最后 pivot 左边是较小元素，右边是较大元素，
    所以更符合“从小到大排序”的递归直觉。
    """
    pivot = nums[l]
    idx = r
    # range(r, l, -1) 不会遍历到 l，因为 l 位置本身就是 pivot
    for i in range(r,l,-1):
        # 如果当前数比 pivot 大，就把它交换到右侧区域
        if nums[i] > pivot:
            nums[idx],nums[i] = nums[i],nums[idx]
            idx -= 1
    # 扫描结束后，把 pivot 放到中间分界点 idx
    nums[l],nums[idx] = nums[idx],nums[l]
    print(nums)
    return idx


"""
这两个 partition 的核心区别：

1. pivot 选的位置不同
- partition_d: 选最右边
- partition_a: 选最左边

2. 扫描方向不同
- partition_d: 从左往右扫
- partition_a: 从右往左扫

3. 分区结果不同
- partition_d: 左边是 > pivot，右边是 <= pivot
- partition_a: 左边是 <= pivot，右边是 > pivot

4. 对应的排序方向直觉不同
- partition_d 更像“把大的丢左边”
- partition_a 更像“把小的留左边，把大的丢右边”

所以虽然两者都能作为 quicksort 的 partition，
但你在递归时，必须清楚它最后到底把哪一边分成了“小于等于 pivot”，
哪一边分成了“大于 pivot”，否则很容易把逻辑写反。
"""


import random


def quick_sort_optimized(nums, l, r):
    if l >= r:
        return

    # 优化1：随机选择 Pivot，避免有序数组导致的 O(N^2)
    # 这一步是竞赛存活的关键
    rand_idx = random.randint(l, r)
    nums[l], nums[rand_idx] = nums[rand_idx], nums[l]
    pivot = nums[l]

    # 优化2：三路切分 (3-Way Partition)
    # lt 指向 < pivot 部分的最后一个元素的下一个位置（初始为 l）
    # gt 指向 > pivot 部分的第一个元素的前一个位置（初始为 r）
    # i 是当前扫描指针
    lt = l  # nums[l+1...lt] < pivot
    gt = r  # nums[gt...r] > pivot
    i = l + 1  # nums[lt+1...i-1] == pivot

    while i <= gt:
        if nums[i] < pivot:
            nums[lt], nums[i] = nums[i], nums[lt]
            lt += 1
            i += 1
        elif nums[i] > pivot:
            nums[i], nums[gt] = nums[gt], nums[i]
            gt -= 1
            # 注意：这里 i 不自增，因为从 gt 换过来的元素还没看过
        else:  # nums[i] == pivot
            i += 1

    # 此时：
    # nums[l...lt-1] 是 < pivot
    # nums[lt...gt] 是 == pivot (不需要再递归这一段了！)
    # nums[gt+1...r] 是 > pivot

    quick_sort_optimized(nums, l, lt - 1)
    quick_sort_optimized(nums, gt + 1, r)


print(lst)
print("Start")
quicksort(lst,0,len(lst)-1)
print("End")
print(lst)

for i in range(22,8,-1):
    print(i)

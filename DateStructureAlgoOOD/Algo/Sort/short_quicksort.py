lst = [4,3,2,9,3,8,2,7]

def quicksort(nums,l,r):
    if l>=r:
        return
    idx = partition_a(nums,l,r)
    quicksort(nums,l,idx-1)
    quicksort(nums,idx+1,r)

def partition_d(nums,l,r):
    pivot = nums[r]
    j = l
    for i in range(l,r): # 实际这里每次都到不了最后一个
        if nums[i]>pivot:
            nums[j],nums[i] = nums[i],nums[j]
            j += 1
    nums[r],nums[j] = nums[j],nums[r]
    print(nums)
    return j

def partition_a(nums, l, r):
    pivot = nums[l]
    idx = r
    for i in range(r,l,-1): # 这里每次也到不了第一个
        if nums[i] > pivot:
            nums[idx],nums[i] = nums[i],nums[idx]
            idx -= 1
    nums[l],nums[idx] = nums[idx],nums[l]
    print(nums)
    return idx


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

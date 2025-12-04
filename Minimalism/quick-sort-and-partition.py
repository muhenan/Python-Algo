"""
Minimalism version of quick sort partition
核心就是这个函数，其他都是调用这个函数
"""
def partition(nums, left, right):
    pivot = nums[right]
    l = left
    for i in range(left, right):
        if nums[i] < pivot:
            nums[l], nums[i] = nums[i], nums[l]
            l += 1
    nums[l], nums[right] = nums[right], nums[l]
    return l


def quick_sort(nums, left, right):
    if left >= right:
        return
    pivot_idx = partition(nums, left, right)
    quick_sort(nums, left, pivot_idx - 1)
    quick_sort(nums, pivot_idx + 1, right)

def largest_k_element(nums, k):
    if k > len(nums):
        return None
    k = len(nums) - k
    left, right = 0, len(nums) - 1
    while left < right:
        pivot_idx = partition(nums, left, right)
        if pivot_idx == k:
            return nums[k]
        elif pivot_idx < k:
            left = pivot_idx + 1
        else:
            right = pivot_idx - 1
    return nums[k]


nums = [3,9,2,1,5,0,6,4]
# print(partition(nums, 0, len(nums) - 1))
# print(nums)

# quick_sort(nums, 0, len(nums) - 1)
# print(nums) 

print(largest_k_element(nums, 4))
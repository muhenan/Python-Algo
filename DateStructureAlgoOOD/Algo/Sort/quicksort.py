from typing import List
import random


class QuickSort:
    """
    快速排序的标准实现
    
    包含三种不同的partition策略：
    1. 使用最右元素作为pivot
    2. 使用随机元素作为pivot（推荐）
    3. 三数取中法选择pivot
    
    时间复杂度：
    - 平均情况：O(nlogn)
    - 最坏情况：O(n^2)
    - 最好情况：O(nlogn)
    
    空间复杂度：O(logn)，递归调用栈的深度
    """
    
    def quickSort(self, nums: List[int]) -> List[int]:
        """快速排序主函数"""
        self._quickSort(nums, 0, len(nums) - 1)
        return nums
    
    def _quickSort(self, nums: List[int], left: int, right: int) -> None:
        """递归实现快速排序"""
        if left < right:
            # 可以选择使用_partition_left
            pivot_idx = self._partition_left(nums, left, right)
            # 递归排序左右两部分
            self._quickSort(nums, left, pivot_idx - 1)
            self._quickSort(nums, pivot_idx + 1, right)

    """
    快速排序的partition方法
    就是找一个基准元素，然后把这个基准元素放在它应该在的位置，使得左边的都小于它，右边的都大于它
    这就是一次划分
    在各式各样的 partition 方法中，双指针交替移动的实现方式是最容易理解的
    """


    def _partition_left(self, nums: List[int], left: int, right: int) -> int:
        """
        使用最左元素作为pivot的partition方法
        这里的 pivot 的意思就是以最左边的为基准，把最左边的点放在它应该在的位置，使得左边的都小于它，右边的都大于它
        双指针交替移动的实现方式
        
        工作原理：
        1. 选择最左元素作为pivot
        2. 从右向左找第一个小于pivot的数
        3. 从左向右找第一个大于pivot的数
        4. 交换这两个数
        5. 重复2-4直到指针相遇
        
        例如：对于数组 [5,3,1,4,8,2], pivot=5
        第一轮：找到 2 和 8，交换 -> [5,3,1,4,2,8]
        第二轮：找到 2 和 4，交换 -> [5,3,1,2,4,8]
        最后：将pivot放到正确位置 -> [2,3,1,5,4,8]
        """
        pivot = nums[left]    # 选择最左元素作为pivot
        start = left         # 记录pivot的初始位置
        
        while left < right:
            # 从右向左找第一个小于pivot的数
            while left < right and nums[right] >= pivot:
                right -= 1
            # 从左向右找第一个大于pivot的数
            while left < right and nums[left] <= pivot:
                left += 1
            # 如果指针未相遇，交换两个数
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
        
        # 将pivot放到最终位置
        nums[start] = nums[left]
        nums[left] = pivot
        return left  # left和right相等，返回哪个都一样
    
    def _partition_right(self, nums: List[int], left: int, right: int) -> int:
        """
        使用最右元素作为pivot的partition方法
        可能在已排序数组上性能较差
        双指针！！！！
        """
        pivot = nums[right]  # 选择最右元素作为pivot
        i = left - 1        # i指向小于pivot的最后一个元素
        
        # j遍历数组，将小于pivot的元素移到左边
        for j in range(left, right):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        
        # 将pivot放到正确位置
        nums[i + 1], nums[right] = nums[right], nums[i + 1]
        return i + 1
    
    def _partition_random(self, nums: List[int], left: int, right: int) -> int:
        """
        使用随机元素作为pivot的partition方法（推荐）
        能够避免最坏情况，期望时间复杂度O(nlogn)
        """
        # 随机选择pivot并与最右元素交换
        pivot_idx = random.randint(left, right)
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        return self._partition_right(nums, left, right)
    
    def _partition_median(self, nums: List[int], left: int, right: int) -> int:
        """
        三数取中法选择pivot
        从左端、右端和中间选择中间值作为pivot
        """
        mid = (left + right) // 2
        # 将左端、中间、右端三个数排序
        if nums[left] > nums[mid]:
            nums[left], nums[mid] = nums[mid], nums[left]
        if nums[left] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[mid] > nums[right]:
            nums[mid], nums[right] = nums[right], nums[mid]
        
        # 将中间值（现在在mid位置）换到right-1位置
        nums[mid], nums[right - 1] = nums[right - 1], nums[mid]
        return self._partition_right(nums, left, right)


# 测试代码
if __name__ == "__main__":
    sorter = QuickSort()
    
    # 测试用例
    test_cases = [
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],  # 普通数组
        [1, 2, 3, 4, 5],                     # 已排序数组
        [5, 4, 3, 2, 1],                     # 逆序数组
        [1],                                 # 单元素数组
        [],                                  # 空数组
        [1, 1, 1, 1, 1],                    # 相同元素数组
    ]
    
    for arr in test_cases:
        original = arr.copy()
        sorted_arr = sorter.quickSort(arr)
        print(f"Original: {original}")
        print(f"Sorted: {sorted_arr}")
        print()

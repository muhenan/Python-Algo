import heapq
from typing import List
import random


class KthLargestFinder:
    """
    LeetCode 215: Kth Largest Element in an Array
    
    Problem Description:
    给定一个未排序的数组，找到其中第k大的元素。
    注意是排序后的第k个最大元素，而不是第k个不同的元素。
    
    Example:
    Input: [3,2,1,5,6,4] and k = 2
    Output: 5
    
    解题思路：
    1. 堆排序：维护大小为k的小顶堆
    2. 快速选择：基于快排的partition
    3. 直接排序：最简单但不是最优
    
    Time Complexity:
    - 堆: O(NlogK)
    - 快速选择: 期望O(N)
    - 排序: O(NlogN)
    """
    
    def findKthLargest_heap(self, nums: List[int], k: int) -> int:
        """
        方法一：堆排序（使用小顶堆）
        时间复杂度：O(NlogK)
        空间复杂度：O(K)
        
        优化：通过控制堆的大小为k，降低时间复杂度
        """
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
    
    def findKthLargest_sort(self, nums: List[int], k: int) -> int:
        """
        方法二：直接排序
        时间复杂度：O(NlogN)
        空间复杂度：O(1)
        """
        nums.sort()
        return nums[len(nums) - k]
    
    def findKthLargest_quickselect(self, nums: List[int], k: int) -> int:
        """
        方法三：快速选择
        时间复杂度：期望O(N)，最坏O(N²)
        空间复杂度：O(1)

        我没有用random，所以我的时间复杂度应该更像是 O(Nlogk)
        """
        k = len(nums) - k  # 转换为第k小的元素
        left, right = 0, len(nums) - 1
        
        while left < right:
            pivot_idx = self._partition(nums, left, right)
            if pivot_idx == k:
                break
            elif pivot_idx < k:
                left = pivot_idx + 1
            else:
                right = pivot_idx - 1
        return nums[k]
    
    def _partition(self, nums: List[int], left: int, right: int) -> int:
        """
        快速选择的partition操作
        使用最左元素作为pivot
        特点：先处理大于等于pivot的元素，确保相遇点是较小的元素
        """
        pivot = nums[left]
        start = left
        
        while left < right:
            # 从右向左找第一个小于pivot的数
            while left < right and nums[right] >= pivot:
                right -= 1
            # 从左向右找第一个大于pivot的数
            while left < right and nums[left] <= pivot:
                left += 1
            # 交换这两个数
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
        
        # 将pivot放到最终位置
        nums[start] = nums[left]
        nums[left] = pivot
        return left  # left和right相等，返回哪个都一样


# 测试代码
if __name__ == "__main__":
    solution = KthLargestFinder()
    test_cases = [
        ([3,2,1,5,6,4], 2),  # 应该返回5
        ([3,2,3,1,2,4,5,5,6], 4),  # 应该返回4
        ([-1,2,0], 2)  # 应该返回0
    ]
    
    for nums, k in test_cases:
        nums_copy = nums.copy()
        print(f"Array: {nums}, k: {k}")
        print(f"Heap result: {solution.findKthLargest_heap(nums_copy, k)}")
        print(f"Sort result: {solution.findKthLargest_sort(nums_copy, k)}")
        print(f"Quickselect result: {solution.findKthLargest_quickselect(nums_copy, k)}")
        print() 
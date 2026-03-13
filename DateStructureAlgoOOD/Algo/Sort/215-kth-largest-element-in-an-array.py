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
        使用最右元素作为pivot
        """
        pivot = nums[right]
        l = left
        
        for i in range(left, right):
            if nums[i] < pivot:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
        nums[l], nums[right] = nums[right], nums[l]
        return l
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """寻找数组中的第k个最大元素"""
        random.seed()  # 初始化随机数种子，确保每次基准选择随机
        return self.quickSelect(nums, k)
    
    def quickSelect(self, nums: List[int], k: int) -> int:
        """快速选择核心函数：在nums中找到第k大元素"""
        # 随机选择基准元素
        pivot = nums[random.randint(0, len(nums) - 1)]
        
        # 划分为三个子数组：
        # big：存储所有 大于基准 的元素
        # equal：存储所有 等于基准 的元素
        # small：存储所有 小于基准 的元素
        big, equal, small = [], [], []
        for x in nums:
            if x > pivot:
                big.append(x)
            elif x < pivot:
                small.append(x)
            else:
                equal.append(x)
        
        # 根据三个子数组的长度与k比较的情况，决定递归方向
        # 情况1：第k大元素在big数组中（k <= big的长度）
        if k <= len(big):
            return self.quickSelect(big, k)
        # 情况2：第k大元素在small数组中（k > big + equal的长度）
        elif k > len(big) + len(equal):
            # 调整k：减去big和equal的长度
            return self.quickSelect(small, k - (len(big) + len(equal)))
        # 情况3：第k大元素在equal数组中（直接返回基准值）
        else:
            return pivot

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
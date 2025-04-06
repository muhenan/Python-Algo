from typing import List


class ThreeSumClosest:
    """
    LeetCode 16: 3Sum Closest
    
    两种实现方式：
    1. 使用去重优化的双指针方法
    2. 不去重的简单双指针方法
    
    最优时间复杂度：O(n²)
    - 无法优化到O(n)，因为必须考虑所有可能的三数组合
    - 即使使用哈希表也无法优化时间复杂度
    """
    def threeSumClosest_with_dedup(self, nums: List[int], target: int) -> int:
        """
        方法一：去重优化的双指针
        优点：减少重复计算
        缺点：代码较复杂
        """
        nums.sort()
        n = len(nums)
        best = float('inf')
        
        def update(cur):
            nonlocal best
            if abs(cur - target) < abs(best - target):
                best = cur
        
        for i in range(n):
            # 去重：跳过重复的第一个数
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            j, k = i + 1, n - 1
            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]
                
                if curr_sum == target:
                    return target
                
                update(curr_sum)
                
                if curr_sum > target:
                    # 去重优化：跳过重复的第三个数
                    k0 = k - 1
                    while j < k0 and nums[k0] == nums[k]:
                        k0 -= 1
                    k = k0
                else:
                    # 去重优化：跳过重复的第二个数
                    j0 = j + 1
                    while j0 < k and nums[j0] == nums[j]:
                        j0 += 1
                    j = j0
        
        return best

    def threeSumClosest_simple(self, nums: List[int], target: int) -> int:
        """
        方法二：简单双指针（不去重）
        优点：代码简洁，易于理解
        缺点：可能有重复计算
        """
        nums.sort()
        n = len(nums)
        best = float('inf')
        
        for i in range(n - 2):
            left, right = i + 1, n - 1
            
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                
                # 更新最接近的和
                if abs(curr_sum - target) < abs(best - target):
                    best = curr_sum
                
                # 根据和的大小移动指针
                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    return target
                    
        return best


# 测试代码
if __name__ == "__main__":
    solution = ThreeSumClosest()
    test_cases = [
        ([-1, 2, 1, -4], 1),          # 标准测试
        ([0, 0, 0], 1),               # 相同元素
        ([1, 1, 1, 0], 100),          # 多个重复元素
        ([1, 2, 4, 8, 16, 32, 64], 82)  # 大数测试
    ]
    
    for nums, target in test_cases:
        print(f"Array: {nums}")
        print(f"Target: {target}")
        print(f"Result with dedup: {solution.threeSumClosest_with_dedup(nums.copy(), target)}")
        print(f"Result simple: {solution.threeSumClosest_simple(nums.copy(), target)}")
        print() 
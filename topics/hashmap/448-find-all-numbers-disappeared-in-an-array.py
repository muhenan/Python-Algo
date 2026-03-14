"""
LeetCode 448: Find All Numbers Disappeared in an Array
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

Problem Description:
给定一个长度为 n 的数组 nums，其中所有数字都在范围 [1, n] 内。
找出所有在范围 [1, n] 内但没有出现在 nums 中的数字。

要求：不使用额外空间（返回结果不计入空间复杂度）

Example:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
解释：数组长度为8，应该包含1-8，但5和6没有出现

Tag: array, hash table
"""

class FindDisappearedNumbers:
    def findDisappearedNumbers_bitmap(self, nums: List[int]) -> List[int]:
        """
        方法一：位图法
        Time: O(n)
        Space: O(n) - 使用了额外数组
        """
        result = []
        length = len(nums)
        # 创建位图数组，标记数字是否出现
        bitmap = [False] * (length + 1)  # 索引0不使用
        
        # 标记出现的数字
        for val in nums:
            bitmap[val] = True
            
        # 找出未标记的数字
        for i in range(1, length + 1):
            if not bitmap[i]:
                result.append(i)
                
        return result
    
    def findDisappearedNumbers_inplace(self, nums: List[int]) -> List[int]:
        """
        方法二：原地修改法
        Time: O(n)
        Space: O(1) - 不使用额外空间，使用原数组当 hash map，通过取余既保留原来的信息，又记录是否出现过
        
        核心思想：利用数组索引来标记数字的出现情况
        - 将每个数对应位置的数加上n
        - 最后检查哪些位置的数小于等于n
        """
        length = len(nums)
        
        # 标记出现的数字（通过增加length）
        for num in nums:
            # 获取原始值的索引（减1是因为数字范围是1-n）
            index = (num - 1) % length
            # 在对应位置加上length
            nums[index] += length
        
        # 找出未出现的数字（值小于等于length的位置）
        result = [i + 1 for i, num in enumerate(nums) if num <= length]
        
        return result


def test_find_disappeared_numbers():
    """测试寻找消失的数字"""
    solution = FindDisappearedNumbers()
    
    # 测试用例
    test_cases = [
        ([4,3,2,7,8,2,3,1], [5,6]),
        ([1,1], [2]),
        ([1,1,2,2], [3,4]),
        ([1,2,3,4], []),
    ]
    
    for nums, expected in test_cases:
        # 测试两种方法
        assert solution.findDisappearedNumbers_bitmap(nums[:]) == expected
        assert solution.findDisappearedNumbers_inplace(nums[:]) == expected
        print(f"Test case passed: {nums} -> {expected}")

if __name__ == "__main__":
    test_find_disappeared_numbers() 
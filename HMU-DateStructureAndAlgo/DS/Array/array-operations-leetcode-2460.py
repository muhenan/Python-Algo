from typing import List


class ArrayOperator:
    """
    LeetCode 2460: Apply Operations to an Array
    
    Problem Description:
    给定一个下标从 0 开始的数组 nums，对这个数组执行以下操作：
    1. 如果 nums[i] == nums[i+1]，则：
       - nums[i] 的值变成原来的 2 倍
       - nums[i+1] 的值变成 0
    2. 将所有 0 移动到数组末尾
    3. 保持非零元素的相对顺序不变
    
    Examples:
    Input: nums = [1,2,2,1,1,0]
    Output: [1,4,1,1,0,0]
    解释：
    - i=0: 1 != 2, 保持不变
    - i=1: 2 == 2, 所以 nums[1] = 4, nums[2] = 0, 变成 [1,4,0,1,1,0]
    - i=2: 0 != 1, 保持不变
    - i=3: 1 == 1, 所以 nums[3] = 2, nums[4] = 0, 变成 [1,4,0,2,0,0]
    - 移动零到末尾: [1,4,2,0,0,0]
    """
    
    def applyOperations_extraSpace(self, nums: List[int]) -> List[int]:
        """
        方法一：使用额外空间
        Time: O(n)
        Space: O(n)
        """
        length = len(nums)
        # 步骤1：处理相邻相等的元素
        for i in range(length - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        # 步骤2：创建新数组，按顺序放入非零元素
        result = [0] * length  # 创建同样大小的数组
        index = 0  # 记录非零元素应该放置的位置
        
        # 将非零元素按顺序放入新数组
        for i in range(length):
            if nums[i] != 0:
                result[index] = nums[i]
                index += 1
                
        return result

    def applyOperations_inPlace(self, nums: List[int]) -> List[int]:
        """
        方法二：原地修改（一次遍历）
        Time: O(n)
        Space: O(1)
        """
        length = len(nums)
        index = 0  # 记录非零元素应该放置的位置
        
        # 一次遍历同时完成两个任务
        for i in range(length - 1):
            # 任务1：处理相邻相等的元素
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
            
            # 任务2：如果当前元素非零，移动到正确位置
            if nums[i]:
                old = nums[i]      # 保存当前值
                nums[i] = 0        # 清空当前位置
                nums[index] = old  # 将值放到正确位置
                index += 1         # 更新下一个非零元素的位置
        
        # 特殊处理最后一个元素（因为它没有下一个元素可比较）
        if nums[-1]:
            old = nums[-1]
            nums[-1] = 0
            nums[index] = old
            
        return nums


# 测试代码
if __name__ == "__main__":
    solu = ArrayOperator()
    test_case = [1,2,2,1,1,0]
    print(solu.applyOperations_extraSpace(test_case.copy()))  # [1,4,1,1,0,0]
    print(solu.applyOperations_inPlace(test_case.copy()))     # [1,4,1,1,0,0] 
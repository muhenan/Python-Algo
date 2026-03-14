import collections
import math
from typing import List
import copy


class JumpGame:
    """
    LeetCode 55: Jump Game

    Problem Description:
    给定一个非负整数数组nums，你最初位于数组的第一个位置。
    数组中的每个元素代表你在该位置可以跳跃的最大长度。
    判断你是否能够到达最后一个位置。

    Example:
    Input: nums = [2,3,1,1,4]
    Output: true

    Tag: greedy
    """
    def canJump(self, nums: List[int]) -> bool:
        """
        从前向后遍历
        Time: O(n), Space: O(1)
        """
        max_reach = 0  # 当前能到达的最远位置
        for i, jump in enumerate(nums):
            if max_reach >= i and i + jump > max_reach:
                max_reach = i + jump
        return max_reach >= len(nums) - 1

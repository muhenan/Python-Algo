import collections
import math
from typing import List
import copy


class TicketBuyingTime:
    """
    LeetCode 2073: Time Needed to Buy Tickets
    
    Problem Description:
    有n个人排队买票，第i个人想买tickets[i]张票。
    每个人每次只能买一张票，如果一个人买完了所需的票，就会离开队伍。
    给定一个下标k，返回第k个人买完所需票数所需的时间。
    买一张票需要1单位时间。
    
    Example:
    Input: tickets = [2,3,2], k = 2
    Output: 6
    """
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        """
        方法一：模拟法
        Time: O(n * tickets[k])
        Space: O(1)
        """
        result = 0
        length = len(tickets)
        target = tickets[k]  # k位置需要买的票数
        
        # 模拟每一轮买票
        for _ in range(target):
            for i in range(length):
                if tickets[i] == 0:  # 已经买完的跳过
                    continue
                tickets[i] -= 1  # 买一张票
                result += 1      # 增加时间
                # 如果是目标位置且买完了，直接返回
                if i == k and tickets[i] == 0:
                    break
        return result
    
    def timeRequiredToBuy2(self, tickets: List[int], k: int) -> int:
        """
        方法二：数学方法
        Time: O(n)
        Space: O(1)
        
        对于每个位置i：
        - 如果i <= k，贡献min(tickets[i], tickets[k])
        - 如果i > k，贡献min(tickets[i], tickets[k]-1)
        """
        return sum(min(x, tickets[k] if i <= k else tickets[k] - 1) 
                  for i, x in enumerate(tickets))

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
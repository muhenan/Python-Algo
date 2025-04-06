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
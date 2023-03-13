from collections import Counter
from typing import List


class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        my_map = Counter([0])
        ans, state = 0, 0
        for n in nums:
            state = state ^ n
            ans += my_map[state]
            my_map[state] += 1
        return ans
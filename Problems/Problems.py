import collections
import math
from typing import List


class Solution6:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag
        return "".join(res)


class Solution914(object):
    def hasGroupsSizeX(self, deck):
        count = collections.Counter(deck)
        N = len(deck)
        for X in range(2, N+1):
            if N % X == 0:
                if all(v % X == 0 for v in count.values()):
                    return True
        return False

for x in range(2, 6):
    print(x)

arr = [1,1,1,2,2,3,3]
count = collections.Counter(arr)
for k, v in count.items():
    print(k, v)

solu914 = Solution914()
print(solu914.hasGroupsSizeX([1,1,1,2,2]))

for value in arr:
    print(value)


class Solution2465:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        n, u = len(nums), set()

        for i in range(0, n // 2):
            u.add((nums[i] + nums[n - i - 1]) / 2)

        return len(u)


class Solution2073:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        result = 0
        length = len(tickets)
        times = tickets[k]
        for _ in range(times):
            for i in range(length):
                if tickets[i] == 0: continue
                tickets[i] -= 1
                result += 1
                if i == k and tickets[i] == 0: break
        return result
    def timeRequiredToBuy2(self, tickets: List[int], k: int) -> int: # slower
        return sum(min(x, tickets[k] if i <= k else tickets[k] - 1) for i, x in enumerate(tickets))

class Solution49:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = collections.defaultdict(list)
        for str in strs:
            key = "".join(sorted(str))
            my_map[key].append(str)
        return list(my_map.values())
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        my_map = collections.defaultdict(list)
        for str in strs:
            #counts = [0 for _ in range(26)]
            counts = [0] * 26
            for c in str:
                counts[ord(c) - ord("a")] += 1
            my_map[tuple(counts)].append(str)
        return list(my_map.values())

#counts = [0] * 26
counts = [0 for _ in range(26)]
print(counts)

print(ord("a"))

class Solution55:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        if (length == 1): return True
        closestOne = length - 1
        for i in reversed(range(length - 1)):
            if nums[i] + i >= closestOne:
                closestOne = i
        return True if closestOne == 0 else False
    def canJump1(self, nums) :
        max_i = 0       #初始化当前能到达最远的位置
        for i, jump in enumerate(nums):   #i为当前位置，jump是当前位置的跳数
            if max_i>=i and i+jump>max_i:  #如果当前位置能到达，并且当前位置+跳数>最远位置
                max_i = i+jump  #更新最远能到达位置
        return max_i>=i

length = 4
for i in reversed(range(length - 1)):
    print(i)

class Solution96:
    def numTrees(self, n: int) -> int:
        dp = [1, 1] + [0] * (n - 1)
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]
    def numTrees1(self, n: int) -> int:
        dp=[1]+[0]*n
        for i in range(1,n+1):
            for j in range(i):
                dp[i]+=dp[j]*dp[i-j-1]
        return dp[n]

# 155
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = [math.inf]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(self.min_stack[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]



print(math.inf)
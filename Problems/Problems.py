import collections
import math
from typing import List
import copy


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
        max_i = 0       #???????????????????????????????????????
        for i, jump in enumerate(nums):   #i??????????????????jump????????????????????????
            if max_i>=i and i+jump>max_i:  #????????????????????????????????????????????????+??????>????????????
                max_i = i+jump  #???????????????????????????
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

class Solution438:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s, len_p = len(s), len(p)
        if len_s < len_p: return []
        ans = []
        s_count = [0] * 26
        p_count = [0] * 26
        for i in range(len_p):
            s_count[ord(s[i]) - ord("a")] += 1
            p_count[ord(p[i]) - ord("a")] += 1
        if s_count == p_count: ans.append(0)
        for i in range(len_s - len_p):
            s_count[ord(s[i]) - ord("a")] -= 1
            s_count[ord(s[i + len_p]) - ord("a")] += 1
            if s_count == p_count: ans.append(i + 1)
        return ans

class Solution621:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = collections.Counter(tasks)
        maxCount = max(counts.values())
        numberOfMax = sum(1 for v in counts.values() if v == maxCount)
        return max(((maxCount - 1) * (n + 1) + numberOfMax), len(tasks))

print(collections.Counter(["a", "c", "b", "a"]))

class Solution394:
    def decodeString(self, s: str) -> str:
        stack, cur_str, multi = [], "", 0
        for c in s:
            if '0' <= c <= '9':
                multi = multi * 10 + int(c)
            elif c == '[':
                stack.append([multi, cur_str])
                cur_str, multi = "", 0
            elif c == ']':
                cur_multi, previousStr = stack.pop()
                cur_str = previousStr + cur_multi * cur_str
            else: cur_str += c
        return cur_str
    def decodeString2(self, s: str) -> str: # one python method can return different values
        def dfs(s, i):
            currentStr, multi = "", 0
            while i < len(s):
                if '0' <= s[i] <= '9':
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':
                    i, subStr = dfs(s, i + 1)
                    currentStr += multi * subStr
                    multi = 0
                elif s[i] == ']':
                    return i, currentStr
                else: currentStr += s[i]
                i += 1
            return currentStr
        return dfs(s, 0)

class Solution581:
    def findUnsortedSubarray(self, nums: List[int]) -> int: # python's sorted is very fast, this solution beat 98.67%
        sortedArr = sorted(nums)
        left, right = -1, -2
        for i in range(len(nums)):
            if sortedArr[i] != nums[i]:
                left = i
                break
        for i in range(len(nums)):
            if sortedArr[i] != nums[i]:
                right = i
        return right - left + 1
    def findUnsortedSubarray2(self, nums: List[int]) -> int: # quicker
        if len(nums) == 1: return 0
        # find left
        left = -3
        for i in range(1, len(nums)):
            if left == -1: break
            if nums[i] < nums[i - 1]:
                if left == -3:
                    left = i - 1
                while  left != -1 and nums[left] > nums[i]: left -= 1
        # find right
        right = -2
        for i in reversed(range(len(nums) - 1)):
            if right == len(nums): break
            if nums[i] > nums[i + 1]:
                if right == -2:
                    right = i + 1
                while right != len(nums) and nums[right] < nums[i]: right += 1
        return right - left - 1
    def findUnsortedSubarray3(self, nums: List[int]) -> int:
        n = len(nums)
        maxn, right = float("-inf"), -1
        minn, left = float("inf"), -1

        for i in range(n): # find right
            if maxn > nums[i]:
                right = i
            else:
                maxn = nums[i]

            if minn < nums[n - i - 1]: # from the last one, find left
                left = n - i - 1
            else:
                minn = nums[n - i - 1]

        return 0 if right == -1 else right - left + 1

arr = [2,6,4,8,10,9,15]
solu581 = Solution581()
solu581.findUnsortedSubarray2(arr)
# print(sorted(arr))
# print(arr)

print(float('inf'))
print(float('-inf'))

class Solution739:
    # n^2 ...
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]: # Monotonic stack
        length = len(temperatures)
        res = [0] * length
        my_queue = []
        for i in range(length):
            while my_queue and temperatures[i] > temperatures[my_queue[-1]]:
                pre_index = my_queue.pop()
                res[pre_index] = i - pre_index
            my_queue.append(i)
        return res
    # Time limited
    # def dailyTemperatures2(self, temperatures: List[int]) -> List[int]:
    #     length = len(temperatures)
    #     res = [0] * length
    #     for i in range(length):
    #         right = i
    #         for j in range(i + 1, length):
    #             if temperatures[j] > temperatures[i]:
    #                 right = j
    #                 break
    #         res[i] = right - i
    #     return res

for i in range(8,2,-1): print(i)

class Solution448:
    # use a ???????????? which is a bit map
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        length = len(nums)
        bitmap = [False] * (length + 1)
        for val in nums: bitmap[val] = True
        for i in range(1, length + 1):
            if not bitmap[i]: res.append(i)
        return res
    """
    ?????? nums ?????????????????????[1, n][1, n]
    ?????????????????????????????????????????????????????????????????????????????????????????????

    ????????????????????? nums?????????????????????
    x????????? nums[x???1] ??????
    n????????? nums ??????????????????[1, n][1, n]
    ?????????????????????????????????????????? n???
    """
    def findDisappearedNumbers2(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for num in nums:
            x = (num - 1) % length
            nums[x] += length
        res = [i + 1 for i, num in enumerate(nums) if num <= length]
        return res


from collections import deque

# class LRUCache146:
#
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.my_dict = dict()
#         self.que = deque()
#         return None
#
#     def get(self, key: int) -> int:
#         if not key in self.my_dict: return -1
#         self.updataQue(key)
#         return self.my_dict[key]
#
#     def put(self, key: int, value: int) -> None:
#         self.updataQue(key)
#         self.my_dict[key] = value
#         if len(self.my_dict) > self.capacity:
#             self.my_dict.pop(self.que[0])
#             self.que.popleft()
#
#     def updataQue(self, key:int):
#         if self.que and self.que[0] == key:
#             self.que.popleft()
#         if not self.que or self.que and self.que[-1] != key:
#             self.que.append(key)

"""
??????????????? ??? LinkedList ?????????????????????
?????????????????????????????????????????????
??? LinkedList ???????????? node ?????????????????????
"""

class LRUCache(collections.OrderedDict):

    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity


    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

"""
hashmap (dictionary) + delinkedlist
"""
"""
??? head ??? tail node?????????????????????
"""
class LRUCache146:

    def __init__(self, capacity: int):
        self.cache = dict()
        # ?????????????????????????????????
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # ?????? key ???????????????????????????????????????????????????
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # ?????? key ????????????????????????????????????
            node = DLinkedNode(key, value)
            # ??????????????????
            self.cache[key] = node
            # ??????????????????????????????
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # ??????????????????????????????????????????????????????
                removed = self.removeTail()
                # ??????????????????????????????
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # ?????? key ????????????????????????????????????????????? value??????????????????
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node

"""
Don't use [[v]*n]*n, it is a trap!
"""
class Solution221:
    def maximalSquare(self, matrix: List[List[str]]) -> int: # dp
        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0 for i in range(columns)] for j in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0: # ??????????????????
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])
        return maxSide * maxSide








import collections
from typing import List
import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)
        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])
        return ans

    '''双端队列构造单调队列'''
    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = collections.deque()
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i) # 至少留下一个就够了

        ans = [nums[q[0]]]
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i) # 至少留下一个就够了
            while q[0] <= i - k:
                q.popleft()
            ans.append(nums[q[0]])

        return ans



arr = [5,3,7,2,8,1]

arr2 = [(arr[i], i) for i in range(len(arr))]
print(arr2)

heapq.heapify(arr2)

print(arr2)
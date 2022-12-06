import heapq
from typing import List

'''
所有和优先队列有关的题

控制队列的长度至关重要！！！！！！

因为队列的长度决定着时间复杂度
'''

class Solution:
    '''暴力方法，超时'''
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        q = []
        for num1 in nums1:
            for num2 in nums2:
                q.append((num1 + num2, num1, num2))
        heapq.heapify(q)
        ans = []
        length = len(q)
        indexk, indexq = 0, 0
        while indexk < k and indexq < length:
            item = heapq.heappop(q)
            ans.append([item[1], item[2]])
            indexk += 1
            indexq += 1
        return ans
    '''控制队列长度'''
    def kSmallestPairs2(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        ans = []
        '''
        这里的逻辑是 所有的 mk, n0 都已经加进去了
        找到一个最小的之后，ni++ 即可，因为所有的 mi 都已经加过了
        时间复杂度是 klogk
        （存 index 方便遍历）
        
        // 也可以用 set 来避免重复，就不用考虑这么多了
        '''
        pq = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, m))]
        while pq and len(ans) < k:
            _, i, j = heapq.heappop(pq)
            ans.append([nums1[i], nums2[j]])
            if j + 1 < n:
                heapq.heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
        return ans

q = [4,6,8,10,5,7]
print(q)
print(type(q))
heapq.heapify(q)
print(type(q))
print(q)

while q:
    print(heapq.heappop(q))

# arr = [5,3,7,2,8,1]
#
# arr2 = [(arr[i], i) for i in range(len(arr))]
# print(arr2)
#
# heapq.heapify(arr2)
#
# print(arr2)

q = [4,6,8,10,5,7]
heapq.heapify(q)
print(heapq.nlargest(len(q),q))
print(heapq.nsmallest(len(q), q))
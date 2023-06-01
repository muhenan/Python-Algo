from typing import List
import bisect

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                  103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                  211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
                  331, 337, 347, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449,
                  457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587,
                  593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709,
                  719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853,
                  857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991,
                  997]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= nums[i + 1]:
                ok = False
                for p in primes:
                    if p < nums[i] and nums[i] - p < nums[i + 1]:
                        nums[i] = nums[i] - p
                        ok = True
                        break
                    if p >= nums[i]:
                        break
                if not ok:
                    return False
        return True

    def minOperations1(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = []
        my_map = {}
        for q in queries:
            curr = 0
            if q in my_map:
                ans.append(my_map[q])
                continue
            for n in nums:
                curr += abs(n - q)
            my_map[q] = curr
            ans.append(curr)
        return ans

    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        ans = []
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] + nums[i]
        for q in queries:
            if nums[0] >= q or nums[-1] <= q:
                ans.append(abs(prefix[-1] - q * len(nums)))
            else:
                index = bisect.bisect(nums, q)
                ans.append(abs(prefix[index - 1] - q * index) + abs(prefix[-1] - prefix[index - 1] - q * (len(nums) - index)))
        return ans

    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(edges) + 1
        my_map = [[] for _ in range(n)]
        for a, b in edges:
            my_map[a].append(b)
            my_map[b].append(a)
        visited = [False] * n
        def dfs(c):
            if visited[c]:
                return 0, 0
            visited[c] = True
            curr_lay, curr_res = 1 if c in coins else 0, 0
            for i in my_map[c]:
                i_lay, i_res = dfs(i)
                curr_lay = max(curr_lay, i_lay)
                curr_res += i_res
        return 0
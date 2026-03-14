from typing import List


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        ans = 0
        visited = [False] * len(nums)
        nums = sorted(nums)
        right = len(nums) - 1
        left = 0
        print(nums)
        for i in range(right - 1, -1, -1):
            if nums[i] * 2 <= nums[right]:
                left = i
                break
        while left >= 0 and right >= 0:
            if visited[left] or visited[right]:
                if visited[left]:
                    left -= 1
                if visited[right]:
                    right -= 1
                break
            if nums[left] * 2 <= nums[right]:
                ans += 2
                print(nums[left], nums[right])
                visited[left] = True
                visited[right] = True
                left -= 1
                right -= 1
            else:
                left -= 1
        return ans

# Java solution (Dijkstra / 最短路 approach):
# public int maxNumOfMarkedIndices(int[] nums) {
#     Arrays.sort(nums);
#     int count = 0;
#     for (int i = 0, j = (nums.length + 1) / 2; j < nums.length; j++) {
#         count += 2 * nums[i] <= nums[j] ? 2 : 0;
#         i += 2 * nums[i] <= nums[j] ? 1 : 0;
#     }
#     return count;
# }

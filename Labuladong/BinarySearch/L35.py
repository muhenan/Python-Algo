from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 找不到的话返回插入位置，也就是比它大的第一个数
        left, right = 0, len(nums) - 1
        ans = len(nums)
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                ans = mid
                right = mid - 1
        return ans

# class Solution {
#     public int searchInsert(int[] nums, int target) {
#         int left = 0, right = nums.length - 1;
#         while(left <= right) {
#             int mid = (left + right) / 2;
#             if(nums[mid] == target) {
#                 return mid;
#             } else if(nums[mid] < target) {
#                 left = mid + 1;
#             } else {
#                 right = mid - 1;
#             }
#         }
#         return left;
#     }
# }
#
#
#
# 结束条件是 left 比 right 还大 1，所以最小时，right 会变成 -1，最大时，left 会出去，变成 length，<= 预示着一直走

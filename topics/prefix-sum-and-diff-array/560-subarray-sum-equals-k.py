from typing import List


class SubarraySumEqualsK:
    """
    LeetCode 560: Subarray Sum Equals K · 和为 K 的子数组

    Given an array of integers nums and an integer k,
    return the total number of subarrays whose sum equals to k.

    A subarray is a contiguous non-empty sequence of elements within an array.

    Example 1:
    Input: nums = [1,1,1], k = 2
    Output: 2

    Example 2:
    Input: nums = [1,2,3], k = 3
    Output: 2

    Constraints:
    - 1 <= nums.length <= 2 * 10^4
    - -1000 <= nums[i] <= 1000
    - -10^7 <= k <= 10^7

    Tags:
    - Prefix Sum
    - Hash Map
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        pre_sum = 0
        pre_sum_count = {0:1}
        for num in nums:
            pre_sum += num
            if pre_sum - k in pre_sum_count:
                ans += pre_sum_count[pre_sum - k]
            pre_sum_count[pre_sum] = pre_sum_count.get(pre_sum, 0) + 1
        return ans


if __name__ == "__main__":
    sol = SubarraySumEqualsK()

    # Test 1: basic case
    assert sol.subarraySum([1, 1, 1], 2) == 2

    # Test 2: multiple subarrays
    assert sol.subarraySum([1, 2, 3], 3) == 2

    # Test 3: single element equals k
    assert sol.subarraySum([3], 3) == 1

    # Test 4: negative numbers
    assert sol.subarraySum([1, -1, 1], 1) == 3

    # Test 5: no valid subarray
    assert sol.subarraySum([1, 2, 3], 7) == 0

    # Test 6: entire array is the answer
    assert sol.subarraySum([1, 2, 3], 6) == 1

    print("All tests passed!")

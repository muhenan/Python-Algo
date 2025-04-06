from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i - 1] + nums[i])
        return max(nums)

"""

/**

method 1
for
    for
        for Calculate the sum of the subarray
n cubic
sc O(1)

method 2
prefixSum[]
subarray(3, 5) = prefixSum[5] - prefix[3]

for generate the prefixSum array
for
    for
        Calculate the sum of the subarray
n squared
sc O(n)

从一个点开始，记录了这个点向后的和，找出最大和
同样 n2

method 3
minPrefixSum
for
    generate the prefixSum array -> prefixSum
    update minPrefixSum
    ans[i] = prefixSum[i] - minPrefixSum
n
n

 */
class Solution {
    public int maxSubArray(int[] nums) {
        // int sum = 0;
        // for (int num: nums) sum += num;
        // int max = sum;
        // int left = 0;
        // int right = nums.length - 1;
        // while (left <= right) {
        //     if (nums[left] < nums[right]) {
        //         left++;
        //         sum -= nums[left];
        //     } else {
        //         right--;
        //         sum -= nums[right];
        //     }
        //     max = Math.max(max, sum);
        // }
        // return max;
        int max = nums[0];
        int prefixSum = nums[0];
        int minPrefixSum = Math.min(0, nums[0]);
        for (int i = 1; i < nums.length; i++) {
            prefixSum += nums[i];
            max = Math.max(max, prefixSum - minPrefixSum);
            minPrefixSum = Math.min(minPrefixSum, prefixSum);
        }
        return max;
    }
}

"""
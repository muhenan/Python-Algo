def three_sum(nums, sum):
    if len(nums) <= 2:
        return []
    nums = sorted(nums)
    ans = []
    for i in range(0, len(nums) - 2):
        target_sum = sum - nums[i]
        l, r = i + 1, len(nums) - 1
        while l < r:
            current_sum = nums[l] + nums[r]
            if current_sum == target_sum:
                ans.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
            elif current_sum < target_sum:
                l += 1
            else:
                r -= 1
    return ans
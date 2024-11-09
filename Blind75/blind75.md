# Blind 75

[toc]



## Array

### [1. Two Sum](https://leetcode.com/problems/two-sum/)

```python
class Solution(object):
    def twoSum(self, original_nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # method 1
        for left in range(len(nums)):
            for right in range(left + 1, len(nums)):
                if nums[left] + nums[right] == target: return [left, right]
        
        # method 2
        nums = sorted(original_nums)
        left = 0
        right = len(nums) - 1
        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum == target:
                for i in range(len(nums)):
                    if original_nums[i] == nums[left]:
                        left = i
                        break
                for i in range(len(nums)):
                    if original_nums[len(nums) - 1 - i] == nums[right]:
                        right = len(nums) - 1 - i
                        break
                return [left, right]
            elif curr_sum > target: 
                right -= 1
            else: 
                left += 1

        # method 3
        my_map = {}
        for i in range(len(original_nums)):
            if target - original_nums[i] in my_map:
                return [my_map[target - original_nums[i]], i]
            else:
                my_map[original_nums[i]] = i
```

```python
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] oldArray = Arrays.copyOf(nums, nums.length);
        int left = 0;
        int right = nums.length - 1;
        Arrays.sort(nums);
        while (left < right) {
            int sum = nums[left] + nums[right];
            if (sum == target) break;
            else if (sum < target) left++;
            else right--;
        }
        int former = nums[left];
        int latter = nums[right];
        for (left = 0; left < nums.length; left++) {
            if (oldArray[left] == former) break;
        }
        for (right = nums.length - 1; right >= 0; right--) {
            if (oldArray[right] == latter) break;
        }
        return new int[]{left, right};

        // sort + binary search / two pointers

        // hash map
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(nums[i])) {
                return new int[]{map.get(nums[i]), i};
            } else {
                map.put(target - nums[i], i);
            }
        }
        return null;
    }
}
```

### [2. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

```python
class Solution {
    public int maxProfit(int[] prices) {
        int max = 0;
        int length = prices.length;

        // method 1
        // for (int i = 0; i < prices.length; i++) {
        //     for (int j = i + 1; j < prices.length; j++) {
        //         int current = prices[j] - prices[i];
        //         max = Math.max(max, current);
        //     }
        // }

        // method 2
        // int[] maxPrices = new int[length];
        // int maxPrice = prices[length - 1];
        // for (int i = length - 1; i >= 1; i--) {
        //     maxPrice = Math.max(maxPrice, prices[i]);
        //     maxPrices[i] = maxPrice;
        // }
        // for (int i = 0; i < length - 1; i++) {
        //     int current = maxPrices[i + 1] - prices[i];
        //     max = Math.max(max, current);
        // }

        int maxPrice = prices[length - 1];
        for (int i = length - 2; i >= 0; i--) {
            int current = maxPrice - prices[i];
            max = Math.max(max, current);
            maxPrice = Math.max(maxPrice, prices[i]);
        }

        return max;
    }
}
```

### [3. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

```python
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # method 1 n2
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]: return True
        return False

        # method 2 nlogn
        nums = sorted(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]: return True
        return False

        # method 3 n
        my_dictionary = {}
        for num in nums:
            if num in my_dictionary:
                return True
            else:
                my_dictionary[num] = 'a'
        return False

        # method 4
        my_dictionary = {}
        for num in nums:
            my_dictionary[num] = 'a'
        return len(my_dictionary) < len(nums)

        # method 5
        return len(set(nums)) < len(nums)
```

### [4. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

```python
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int length = nums.length;
        int[] ans = new int[length];

        // method 1
        for (int i = 0; i < length; i++) {
            int current = 1;
            for (int j = 0; j < length; j++) {
                if (j != i) current *= nums[j];
            }
            ans[i] = current;
        }

        // method 2
        int[] left = new int[length];
        int[] right = new int[length];

        for(int i = 0; i < length; i++) {
            if (i == 0) {
                left[i] = nums[i];
            } else left[i] = left[i - 1] * nums[i];
        }

        for (int i = length - 1; i >= 0; i--) {
            if (i == length - 1) {
                right[i] = nums[i];
            } else right[i] = right[i + 1] * nums[i];
        }

        for (int i = 0; i < length; i++) {
            if (i == 0) {
                ans[i] = right[i + 1];
            } else if (i == length - 1) {
                ans[i] = left[i - 1];
            } else ans[i] = left[i - 1] * right[i + 1];
        }

        // method 3
        for(int i = 0; i < length; i++) {
            if (i == 0) {
                ans[i] = nums[i];
            } else ans[i] = ans[i - 1] * nums[i];
        }

        int right = 1;
        for (int i = length - 1; i >= 0; i--) {
            if (i == length - 1) {
                ans[i] = ans[i - 1];
            } else if (i == 0) {
                ans[i] = right;
            } else {
                ans[i] = ans[i - 1] * right;
            }
            right *= nums[i];
        }

        return ans;
    }

public int[] productExceptSelf(int[] nums) {
        int[] res = new int[nums.length];
        int k = 1;
        for(int i = 0; i < res.length; i++){
            res[i] = k;
            k = k * nums[i]; // 此时数组存储的是除去当前元素左边的元素乘积
        }
        k = 1;
        for(int i = res.length - 1; i >= 0; i--){
            res[i] *= k; // k为该数右边的乘积。
            k *= nums[i]; // 此时数组等于左边的 * 该数右边的。
        }
        return res;
    }

}
```

### [5. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

```python
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
n -> O(1)

 */
class Solution {
    public int maxSubArray(int[] nums) {
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

class Solution {
    public int maxSubArray(int[] nums) {
        int pre = 0, maxAns = nums[0];
        for (int x : nums) {
            pre = Math.max(pre + x, x);
            maxAns = Math.max(maxAns, pre);
        }
        return maxAns;
    }
}
```

### [6. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # method 1
        result = nums[0]
        for i in range(len(nums)):
            current = 1
            for j in range(i, len(nums)):
                current *= nums[j]
                result = max(result, current)
        return result

        # method 2
        result = nums[0]
        currentMax = 1
        currentMin = 1
        for element in nums:
            arr = sorted([currentMax * element, currentMin * element, element])
            currentMax = arr[2]
            currentMin = arr[0]
            result = max(result, currentMax)
        return result

        # method 3
        result = nums[0]
        currentMax, currentMin = 1, 1
        for element in nums:
            currentMax, currentMin = max(currentMax * element, currentMin * element, element), min(currentMax * element, currentMin * element, element)
            result = max(result, currentMax)
        return result
```

### [7. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

```python
"""
 *
* 
       *
     *
   *
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # method 1
        # return min(nums)

        # method 2
        left, right = 0, len(nums) - 1

        leftOne = nums[left]
        rightOne = nums[right]

        if leftOne < rightOne:
            return nums[0]
        
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < leftOne:
                right = mid
            elif nums[mid] >= leftOne:
                left = mid + 1

        return nums[left]

# 下面是官方解法，把特殊情况也包括了
# 和 right one 比较，如果 mid 小，就一直移动 right
class Solution:
    def findMin(self, nums: List[int]) -> int:    
        low, high = 0, len(nums) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if nums[pivot] < nums[high]:
                high = pivot 
            else:
                low = pivot + 1
        return nums[low]
```

<aside>
🔥 二分查找，搞 mid = right，可以用 while left < right，因为总能走到两者相等，如果是 mid = left，那么也可以用  while left < right，但是就要改一下 mid 的生成方式了

</aside>

具体见 leetcode 篇中的二分查找

### [8. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:\

        # method 1
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # return -1

        # method 2 六种情况变四种情况了，因为归根结底，就是 2 * 2，四种情况
        left, right = 0, len(nums) - 1
        leftOne = nums[0]
        while left <= right:
            mid = left + (right - left) // 2
            midOne = nums[mid]
            if midOne == target:
                return mid
            if midOne >= leftOne:
                if leftOne <= target < midOne:
                    right = mid - 1 
                else:
                    left = mid + 1
            else:
                if midOne < target < leftOne:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
```

### [9. Three Sum](https://leetcode.com/problems/3sum/)

### [10. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # n2 方法
        # answer = 0
        # for left in range(len(height)):
        #     for right  in range(left + 1, len(height)):
        #         answer = max(answer, (right - left) * min(height[left], height[right]))
        # return answer
        
        # n 方法
        # 双指针，贪心解决问题了
        answer = 0
        left, right = 0, len(height) - 1
        while left < right:
            answer = max(answer, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return answer
```

---

## Binary

### 11. Sum of Two Integers
[link](https://leetcode.com/problems/sum-of-two-integers/)

### 12. Number of 1 Bits
[link](https://leetcode.com/problems/number-of-1-bits/)

### 13. Counting Bits
[link](https://leetcode.com/problems/counting-bits/)

### 14. Missing Number
[link](https://leetcode.com/problems/missing-number/)

### 15. Reverse Bits
[link](https://leetcode.com/problems/reverse-bits/)

---

## Dynamic Programming

### [16. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) 同斐波那契

最最简单的 dp，三种方法：

1. 函数递归调用
2. dp 表一维数组
3. 空间优化，把一维数组变成两个变量

### [17. Coin Change](https://leetcode.com/problems/coin-change/) 完全背包问题

必须搞懂！！！！

分析：

- 其实这个题有很多解法做法可以用，并不是非要 dp
    1. 可以正常回溯来做，说白了回溯就是便利，便利所有可能的情况，或者说这种方法叫 dfs，就是便利所有的情况，但是时间复杂度可能是指数的
        - 简单来说就是暴力 dfs
    2. 第二种，优化一下，我感觉就是 dp。东西可以无限拿，看成类似一个完全背包问题。在每一个硬币的基础上，循环答案的可能性，最后返回把所有硬币都用上以后的答案

<aside>
🔥 完全背包问题，东西可以无限拿的时候，外 for 是循环东西，里面 for 是循环答案

</aside>

dfs 爆搜，超时，时间复杂度类似指数的

```python
class Solution:
    answer = float('inf')
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        def dfs(index, current_amount, num_coins):
            if current_amount == 0:
                self.answer = min(self.answer, num_coins)
            elif current_amount > 0:
                for i in range(index, len(coins)):
                    current_num_coins = num_coins + 1
                    dfs(i, current_amount - coins[i], current_num_coins)
        for i in range(len(coins)):
            dfs(i, amount - coins[i], 1)
        return self.answer if self.answer != float('inf') else -1
```

dp ，自己最直接的想法

```python
def coinChange2(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(len(dp)):
                if i < coin:
                    continue
                elif i == coin:
                    dp[i] = 1
                else:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1
```

外 for coin 内 for amount

dp 优化后

```python
def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        dp = [inf] * (amount + 1)
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        for coin in coins:
            for i in range(coin + 1, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return -1 if dp[-1] == inf else dp[-1]
```

### [18. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)

第二种方法，考虑让 increasing subsequence 尽量小

```jsx
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # bf n2
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
    def lengthOfLIS2(self, nums: List[int]) -> int:
        d = []
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                l, r = 0, len(d) - 1
                loc = r
                while l <= r:
                    mid = (l + r) // 2
                    if d[mid] >= n:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                d[loc] = n
        return len(d)
```

### [19. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)

```jsx
def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]
        for index2 in range(1, len(text2) + 1):
            for index1 in range(1, len(text1) + 1):
                if text1[index1 - 1] == text2[index2 - 1]:
                    dp[index2][index1] = 1 + dp[index2 - 1][index1 - 1]
                else:
                    dp[index2][index1] = max(dp[index2 - 1][index1], dp[index2][index1 - 1])
        # for row in dp:
        #     print(row)
        return dp[-1][-1]
```

### [20. Word Break Problem](https://leetcode.com/problems/word-break/)

其实这个感觉类似于前缀和了

<aside>
🔥 这里其实就有了前缀和和 DP 的奇妙联系

</aside>

通过类似于前缀和形式，不断的向后得到结果

```jsx
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        check = [False] * (len(s) + 1)
        check[0] = True
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                check[j] = check[j] or check[i] and (s[i:j] in wordDict)
        return check[-1]
```

我就把这种称之为前缀和加 dp

通过前面一个决定后面一个

另外还有一种 backtracking 爆搜的方法，但是函数调用栈太多，超时

必须加了一行 @functools.lru_cache(None) 才过的

这种爆搜方法暂且不说了

```jsx
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def back_track(s):
            if not s: return True
            for i in range(1,len(s)+1):
                if s[:i] in wordDict and back_track(s[i:]):
                    return True
            return False
        return back_track(s)
```

递归嘛，把任务交给下一个函数，这个函数只检测当前的很小的一小段字符串在不在

### [21. Combination Sum](https://leetcode.com/problems/combination-sum-iv/)

最暴力的 DFS，便利所有可能情况，直接超时

```jsx
class Solution:
    ans = 0
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.ans = 0
        my_stack = []
        def dfs(amount, target):
            if amount == target:
                self.ans += 1
                return
            elif amount > target:
                return
            else:
                for num in nums:
                    dfs(amount + num, target)
        for num in nums:
            dfs(num, target)
        return self.ans
```

做一点点优化呢，来个提早结束

```jsx
class Solution:
    ans = 0
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.ans = 0
        my_stack = []
        nums = sorted(nums)
        def dfs(amount, target):
            if amount == target:
                self.ans += 1
                return
            elif amount > target:
                return
            else:
                for num in nums:
                    if amount + num > target:
                        break
                    dfs(amount + num, target)
        for num in nums:
            if num <= target:
                dfs(num, target)
        return self.ans
```

依旧超时，可能要换思路了

当完全背包问题做，两个 for，循环找到答案数组

```jsx
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        ans = [0] * (target + 1)
        for i in range(1, target + 1):
            for num in nums:
                if num > i:
                    continue
                elif num == i:
                    ans[i] += 1
                else:
                    ans[i] += ans[i - num]
        return ans[-1]
```

### [22. House Robber](https://leetcode.com/problems/house-robber/)

```jsx
# 经典 dp 题目
# 1. （自顶向下）迭代如果单纯迭代的话，复杂度是指数的，2^n
# 2. （自顶向下）用一个 dp map 字典 （自底向上）

# 3. （自底向上）用一个 dp 数组，从后往前，找到答案
# 4. （自底向上）把空间复杂再优化，把数组变成两个变量
class Solution:
    def rob1(self, nums: List[int]) -> int: # 2^n 超时
        def findMax(nums, index):
            if index == len(nums) - 1:
                return nums[-1]
            elif index == len(nums) - 2:
                return max(nums[-1], nums[-2])
            else:
                return max(nums[index] + findMax(nums, index + 2), findMax(nums, index + 1))
        return findMax(nums, 0)
    def rob2(self, nums: List[int]) -> int: # 时间效率基本无敌，超越 96.29%
        my_map = {}
        def findMax(nums, index):
            if index in my_map:
                return my_map[index]
            if index == len(nums) - 1:
                return nums[-1]
            elif index == len(nums) - 2:
                return max(nums[-1], nums[-2])
            else:
                maxOne = max(nums[index] + findMax(nums, index + 2), findMax(nums, index + 1))
                my_map[index] = maxOne
                return maxOne
        return findMax(nums, 0)
    def rob3(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        dp = [0] * len(nums)
        dp[-1], dp[-2] = nums[-1], max(nums[-1], nums[-2])
        for i in range(len(nums) - 3, -1, -1):
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
        return dp[0]
    def rob4(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        pre1, pre2 = nums[-1], max(nums[-1], nums[-2])
        result = max(pre1, pre2)
        for i in range(len(nums) - 3, -1, -1):
            result = max(nums[i] + pre1, pre2)
            pre1 = pre2
            pre2 = result
        return result
```

### [23. House Robber II](https://leetcode.com/problems/house-robber-ii/)

直接就是用的自底向上的方法，用了一个一维数组，这里懒得优化成变量了

不过这个肯定是可以优化的，最后优化成四个变量

算法的思路是考虑了两种情况，带第一个和不带第一个

```jsx
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        withFirst, noFirst = [0] * len(nums), [0] * len(nums)
        withFirst[0], withFirst[1], noFirst[0], noFirst[1] = nums[0], max(nums[0], nums[1]), 0, nums[1]
        for i in range(2, len(nums)):
            withFirst[i] = max(nums[i] + withFirst[i - 2], withFirst[i - 1])
            noFirst[i] = max(nums[i] + noFirst[i - 2], noFirst[i - 1])
        return max(noFirst[-1], withFirst[-2])
```

### [24. Decode Ways](https://leetcode.com/problems/decode-ways/)

同样的思路，前缀和，影响下一个，DP

```jsx
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        if len(s) == 2:
            if s[1] != '0':
                return 2 if int(s) <= 26 else 1
            else:
                return 1 if s[0] in '12' else 0
        ans = [0] * len(s)
        ans[0] = 1
        if s[1] != '0':
            ans[1] += 1
        if int(s[:2]) <= 26:
            ans[1] += 1
        for i in range(2, len(s)):
            if s[i] != '0':
                ans[i] += ans[i - 1]
            if 10 <= int(s[i-1:i + 1]) <= 26:
                ans[i] += ans[i - 2]
        return ans[-1]
```

### [25. Unique Paths](https://leetcode.com/problems/unique-paths/)

数学方法，这里就不说了，直接返回，C(m, m + n)

动态规划的方法，最简单的是直接二维数组，思路也非常简单

最简单直接的解法

```jsx
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n == 1 or m == 1:
            return 1
        dp = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    dp[r][c] = 1
                else:
                    dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        return dp[-1][-1]
```

可以把空间再压缩成一维数组，，既在之前的空间上做更改

类似于这样

```jsx
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        return cur[-1]
```

### [26. Jump Game](https://leetcode.com/problems/jump-game/)

感觉太简单了，又有点不太像 DP，好像就是**不断的更新这个最多能到的位置**，如果中途有个地方走不下去了，就返回 False，如果是都走过去了，最后返回 True

```jsx
def canJump(self, nums: List[int]) -> bool:
        longest = 0
        for i in range(len(nums)):
            if i > longest:
                return False
            longest = max(longest, i + nums[i])
        return True
```

---

## Graph

### [27. Clone Graph](https://leetcode.com/problems/clone-graph/)

传统 DFS 解决问题，用一个字典，记录了对应的新老 node

```jsx
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        self.visited = {}
        def dfs(curr_node:'Node'):
            if not curr_node:
                return curr_node
            if curr_node in self.visited:
                return self.visited[curr_node]
            clone_node = Node(curr_node.val)
            self.visited[curr_node] = clone_node
            if len(curr_node.neighbors) != 0:
                for n in curr_node.neighbors:
                    clone_node.neighbors.append(dfs(n))
            return clone_node
        return dfs(node)
```

### [28. Course Schedule](https://leetcode.com/problems/course-schedule/)

首先图不一定是连通图

但这种一般告诉你，有多少个节点，这样的话，就从各个节点开始往下走

这个题返回 false 只有一种可能性，就是有环，这样就有死锁，不能全部学到，所以肯定就不行了

我们只要找这个多联通分量的图里有没有环就行了

如果我们从环中的一个点开始走，可能还能走到这个点，所以我们的方法是，每个点都有三个状态：

1. 未 visit 过
2. 在 visit 中
3. visit 完毕

如果我们 visit 到一个在 visit 中的点，那么这里就是环了

<aside>
🔥 这种不连通的图，一定会告诉你有多少节点的，然后你从每个点都去走就好了

</aside>

```jsx
def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            edges[edge[1]].append(edge[0])
        self.result = True
        visited = [0] * numCourses
        def dfs(index):
            if not self.result: return
            visited[index] = 1
            for n in edges[index]:
                if visited[n] == 1:
                    self.result = False
                elif visited[n] == 0:
                    dfs(n)
            visited[index] = 2
        for i in range(numCourses):
            dfs(i)
        return self.result
```

### [29. Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)

经典 DFS

正难则反，以退为进

```jsx
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # 最直接思路，从两个海 DFS，标记所有能到的
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        def dfs(r, c, visited):
            visited[r][c] = True
            for d in directions:
                nr, nc = r + d[0], c + d[1]
                if 0 <= nr < row and 0 <= nc < col and not visited[nr][nc] and heights[r][c] <= heights[nr][nc]:
                    dfs(r + d[0], c + d[1], visited)
        row, col = len(heights), len(heights[0])
        pVisited = [[False] * col for _ in range(row)]
        aVisited = [[False] * col for _ in range(row)]
        for i in range(col):
            dfs(0, i, pVisited)
        for i in range(row):
            dfs(i, 0, pVisited)
        for i in range(col):
            dfs(row - 1, i, aVisited)
        for i in range(row):
            dfs(i, col - 1, aVisited)
        ans = []
        for r in range(row):
            for c in range(col):
                if pVisited[r][c] and aVisited[r][c]:
                    ans.append([r, c])
        return ans
```

### [30. Number of Islands](https://leetcode.com/problems/number-of-islands/)

自解方法问题也不大，直接从每个点都开始 dfs ，标记所有岛

```jsx
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        def dfs(r, c):
            grid[r][c] = '0'
            for d in directions:
                nr, nc = r + d[0], c + d[1]
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == '1':
                    dfs(nr, nc)
            return 
        ans = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    ans += 1
                    dfs(r, c)
        return ans
```

### [31. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

1. 最直接的，排序
2. 哈希表记录，然后从每个点开始搜索

```jsx
class Solution:
    def longestConsecutive1(self, nums: List[int]) -> int: # 最直接，排序，找连续 substring
        if len(nums) == 0:
            return 0
        longest = 1
        curr_long = 1
        nums = sorted(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                curr_long += 1
                longest = max(longest, curr_long)
            elif nums[i] == nums[i - 1]:
                continue
            else:
                curr_long = 1
        return longest
    def longestConsecutive(self, nums: List[int]) -> int:
        my_map = {}
        for num in nums:
            my_map[num] = False
        ans = 0
        for num in nums:
            if my_map[num] == True:
                continue
            curr_ans = 1
            my_map[num] == True

            next_index = num + 1
            while next_index in my_map and not my_map[next_index]:
                my_map[next_index] = True
                curr_ans += 1
                next_index += 1
            
            next_index = num - 1
            while next_index in my_map and not my_map[next_index]:
                my_map[next_index] = True
                curr_ans += 1
                next_index -= 1
            ans = max(ans, curr_ans)
        return ans
```

```jsx
class Solution {
    public int longestConsecutive(int[] nums) {
        HashMap<Integer, Integer> my_map = new HashMap<>();
        for (int num: nums) {
            my_map.put(num, null);
        }
        int longest = 0;
        for (int num: nums) {
            if(!my_map.containsKey(num - 1)) {
                int current = num;
                int current_longest = 1;
                while (my_map.containsKey(current + 1)) {
                    current ++;
                    current_longest ++;
                }
                longest = Math.max(current_longest, longest);
            }
        }
        return longest;

    }
}
```

### 32. Alien Dictionary (Leetcode Premium)
[link](https://leetcode.com/problems/alien-dictionary/)

### 33. Graph Valid Tree (Leetcode Premium)
[link](https://leetcode.com/problems/graph-valid-tree/)

### 34. Number of Connected Components in an Undirected Graph (Leetcode Premium)
[link](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)

---

## Interval

### [35. Insert Interval](https://leetcode.com/problems/insert-interval/)

```python
class Solution:
    # 两种情况
    #  1. 没交集
    #   1.1 interval is left to the new
    #   1.2 ...         right ...
    #  2. 有交集 -> update left and right
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = newInterval
        done = False
        ans = []
        for li, ri in intervals:
            if ri < newInterval[0]:
                ans.append([li, ri])
            elif newInterval[1] < li:
                if not done:
                    ans.append([left, right])
                    done = True
                ans.append([li, ri])
            else:
                left = min(left, li)
                right = max(right, ri)
        if not done:
            ans.append([left, right])
        return ans
```

### [36. Merge Intervals](https://leetcode.com/problems/merge-intervals/)

```python
class Solution:
    """
    先按照开始时间排序一下，这样就让我们是在按照开始顺序处理每一个 interval
    对于每一个 interval 和它的上一个，有两种情况
    1. 完全不重叠，append pre，更新 pre，pre = current
    2. 重叠，更新 pre.right = max(pre.right, intervals[i].right)
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals = sorted(intervals, key= lambda x : x[0])
				#intervals.sort(key=lambda x: x[0])
        left, right = intervals[0]
        for i in range(1, len(intervals)):
            if right < intervals[i][0]:
                ans.append([left, right])
                left, right = intervals[i]
            else:
                right = max(right, intervals[i][1])
        ans.append([left, right])
        return ans
```

以后排序都这么写，都用 .sort

```python
intervals.sort(key=lambda x: x[0])
```

我们就理解为原地排序，这里就理解为原地！！！！！！！！

就理解为排序没有占用额外的空间，还是原数组

以后都用

```python
.sort(arr , key = lambda x : …)
```

### [37. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)

直接 intervals.sort(key = lambda x:x[0])

贪心，找最早结束

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        pre = intervals[0][1]
        ans = 0
        for i in range(1, len(intervals)):
            if pre <= intervals[i][0]:
                pre = intervals[i][1]
            else:
                ans += 1
                pre = min(pre, intervals[i][1])
        return ans
```

#### 436 寻找右区间

可以直接暴力 n2 做

二分查找 → nlogn

```python
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        my_map = {}
        for i, (start, _) in enumerate(intervals):
            my_map[start] = i
        starts = [interval[0] for interval in intervals]
        starts.sort()
        ans = [-1] * len(intervals)
        def find_min_start(val):
            left, right = 0, len(starts) - 1
            while left < right:
                mid = (left + right) // 2
                if starts[mid] == val:
                    return val
                if starts[mid] >= val:
                    right = mid
                else:
                    left = mid + 1
            if starts[left] >= val:
                return starts[left]
            else:
                return None
        for i in range(len(intervals)):
            min_start = find_min_start(intervals[i][1])
            if min_start != None:
                ans[i] = my_map[min_start]
        return ans
```

### [38. Meeting Rooms (Leetcode Premium)](https://leetcode.com/problems/meeting-rooms/)

### [39. Meeting Rooms II (Leetcode Premium)](https://leetcode.com/problems/meeting-rooms-ii/)

#### meeting rooms 3

莫名的bug，用 10000000这种最大值不行，在 python中，最大值一定要使用

```python
float('inf') # 这也是一个习惯问题，避免使用 Magic number，用 maximum
```

!!!!!!!!!!!!!!，自解方法更推荐用 12，就避免这个最大值的问题了

```python
class Solution:
    def mostBooked11(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = lambda x:x[0])
        count = [0] * n
        pre = [-1] * n
        for m in meetings:
            flag = False
            min_end, min_room_id = float('inf'), 0
            for i in range(n):
                if pre[i] <= m[0]:
                    pre[i] = m[1]
                    count[i] += 1
                    flag = True
                    break
                if pre[i] < min_end:
                    min_end = pre[i]
                    min_room_id = i
            if not flag:
                count[min_room_id] += 1
                pre[min_room_id] = pre[min_room_id] - m[0] + m[1]
        print(count)
        max_count = max(count)
        for i in range(len(count)):
            if count[i] == max_count:
                return i
        return 0

    def mostBooked12(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = lambda x:x[0])
        count = [0] * n
        pre = [-1] * n
        for m in meetings:
            flag = False
            for i in range(n):
                if pre[i] <= m[0]:
                    pre[i] = m[1]
                    count[i] += 1
                    flag = True
                    break
            if not flag:
                min_end = min(pre)
                for i in range(n):
                    if pre[i] == min_end:
                        count[i] += 1
                        pre[i] = pre[i] - m[0] + m[1]
                        break
        print(count)
        max_count = max(count)
        for i in range(len(count)):
            if count[i] == max_count:
                return i
        return 0
```

时间复杂度是 O(mn)

下面是双堆模拟，时间复杂度到类似 nlogn，（优先队列，堆）

- 一个堆模拟 idle
- 一个堆模拟 using

每个不同的时刻要更新 idle 和 using，随着时间的推移，using 的可能变成 idle

```python
def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        cnt = [0] * n

        meetings.sort(key=lambda m: m[0])

        idle, using = list(range(n)), []
        
        for st, end in meetings:
            while using and using[0][0] <= st:
                heappush(idle, heappop(using)[1])  # 维护在 st 时刻空闲的会议室
            if len(idle) == 0:
                e, i = heappop(using)  # 没有可用的会议室，那么弹出一个最早结束的会议室（若有多个同时结束的，会弹出下标最小的）
                end += e - st  # 更新当前会议的结束时间
            else:
                i = heappop(idle)
            cnt[i] += 1
            heappush(using, (end, i))  # 使用一个会议室
        ans = 0
        for i, c in enumerate(cnt):
            if c > cnt[ans]:
                ans = i
        return ans
```

#### 扫描线算法

1353

```python
class Solution:
    """
    思路和我们想的差不多
    从开始时间早的开始处理，然后先结束结束时间最早的
    本质上就是贪心

    但是实际的操作中，要用一个 最小堆 来维护这个结束时间，随着时间的推移 update 堆
    类似于之前做过的双堆模拟

    扫描线算法：
    个人理解，就是循环时间，模拟时间的推移，实时更新最小堆
    """
    def maxEvents(self, events: List[List[int]]) -> int:
        starts = {}
        for e in events:
            arr = starts.get(e[0], [])
            arr.append(e[1])
            starts[e[0]] = arr
        max_start = 10 ** 5 + 1
        ans = 0
        min_end = []
        for i in range(max_start):
            if i in starts:
                for end in starts[i]:
                    heapq.heappush(min_end, end)
            while min_end and min_end[0] < i:
                heapq.heappop(min_end)
            if min_end:
                heapq.heappop(min_end)
                ans += 1
        return ans
```

- 双堆模拟
- 循环时间

- 看 会议室 3

---

## Linked List 但凡链表题，必须有 dummy

### [Reverse a Linked List](https://leetcode.com/problems/reverse-linked-list/)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        三种方法
        1. 最简单的，把东西都放在一个 list 里，然后重新构建一个 linkedlist 空间 O(n)
        2. 递归，用函数帮忙 reverse，时空都 n
        3. 直接原地 reverse，while 外声明一个 pre，while 内 4 行
        """
        # method 1
        myArr = []
        while head:
            myArr.append(head.val)
            head = head.next
        dummy = ListNode()
        curr = dummy
        for num in myArr[::-1]:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next

        # method 2
        if head == None or head.next == None: return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead

        # method 3
        pre = None
        while head:
            oldHead = head
            head = head.next
            oldHead.next = pre
            pre = oldHead
        return pre
```

### [Detect Cycle in a Linked List](https://leetcode.com/problems/linked-list-cycle/)

```python
"""
1. 链表方法，快慢指针相遇
2. set 有重复
"""
class Solution:
    # method 1
    def hasCycle1(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
        return False
    # method 2
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        mySet = set()
        while head:
            if head in mySet: return True
            mySet.add(head)
            head = head.next
        return False
```

### [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

use old nodes

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        iterate = dummy
        while list1 and list2:
            if list1.val < list2.val:
                iterate.next = list1
                list1 = list1.next
            else:
                iterate.next = list2
                list2 = list2.next
            iterate = iterate.next
        if list1: iterate.next = list1
        if list2: iterate.next = list2
        return dummy.next

# 也有递归的写法，但要用比较多额外的空间，很简单，这里暂且不写了 like f(x) = 1 + f(x - 1)
```

### [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

```python
from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    """
    最简单的 merge two
    生成一个新 linkedlist
    也可以在原来的 list 上操作，打乱顺序，重新连起来
    """
    def mergeTwo(self, list1, list2):
        dummy = ListNode(-1)
        iteratePointer = dummy
        while list1 and list2:
            if list1.val < list2.val:
                iteratePointer.next = ListNode(list1.val)
                list1 = list1.next
            else:
                iteratePointer.next = ListNode(list2.val)
                list2 = list2.next
            iteratePointer = iteratePointer.next
        if list1: iteratePointer.next = list1
        if list2: iteratePointer.next = list2
        return dummy.next

    """
    method 1
    不断调用merge two
    time:
    最长的 list 是 n
    merge 一次平均的时间复杂度是 O(n * (k/2))
    merge k 次
    时间复杂度 O(k) * O(n * (k/2)) = O(k * k * n)
    所有 kn 都被使用了 k/2 次
    """
    def mergeKLists1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # method 1
        answer = None
        for head in lists:
            answer = self.mergeTwo(answer, head)
        return answer

    """
    method 2
    所有 kn 都被使用了 logk 次
    time O(logk * k * n)
    """
    def mergeKLists2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        length = len(lists)
        if length == 0: return None
        if length == 1: return lists[0]
        mid = length // 2
        list1 = self.mergeKLists(lists[:mid])
        list2 = self.mergeKLists(lists[mid:])
        return self.mergeTwo(list1, list2)

    """
    method 3
    PQ / heap
    python 的最直接的优先队列方法，相当于把所有的都放进去排序了
    这样的话，时间复杂度是不如分治的
    时间复杂度是
    O(nklog(nk))
    但是实际跑起来是非常快的，有时候，真正运行的速度不知和时间复杂度有关，也和代码具体的写法有关
    """
    def mergeKLists3(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        iterateNode = dummy
        myHeap = []
        heapq.heapify(myHeap)
        for head in lists:
            while head:
                heapq.heappush(myHeap, head.val)
                head = head.next
        while myHeap:
            iterateNode.next = ListNode(heapq.heappop(myHeap))
            iterateNode = iterateNode.next
        return dummy.next

    """
    method 4
    和 Java 的优先队列的方法一样
    这里是直接把 ListNode 丢进 pq
    所以需要我们自己定义了 ListNode类 的比较规则（定义了一个小于）
    注意这里 __lt__ 的写法，直接就是 mergeKLists 中的一个子函数
    并不是 solution 的 self 函数
    所以直接在 mergeKLists 用 __lt__ 名字调用这个函数即可
    """
    def mergeKLists4(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # def __lt__(self, other):
        #     return self.val < other.val
        # ListNode.__lt__ = __lt__
        ListNode.__lt__ = lambda A, B: A.val < B.val
        dummy = ListNode(-1)
        iterateNode = dummy
        myHeap = []
        heapq.heapify(myHeap)
        for i in lists:
            if i :heapq.heappush(myHeap, i)
        while myHeap:
            node = heapq.heappop(myHeap)
            iterateNode.next = node
            iterateNode = iterateNode.next
            node = node.next
            if node: heapq.heappush(myHeap, node)
        return dummy.next
```

### [Remove Nth Node From End Of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

```python
"""
1. 数组
2. 快慢指针
"""
class Solution:
    def removeNthFromEnd1(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = dummy = ListNode()
        array = []
        while head:
            array.append(head.val)
            head = head.next
        for i in range(len(array)):
            if i != len(array) - n:
                curr.next = ListNode(array[i])
                curr = curr.next
        return dummy.next
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = fast = dummy
        while n >= 0:
            fast = fast.next
            n -= 1
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next
```

### [Reorder List](https://leetcode.com/problems/reorder-list/)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList1(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        """
        method 1
        用一个数组保存各个 node 的地址，这样就可以各种顺序找 node 了
        空间复杂度 O(n)
        """
        if head == None: return
        myArray = []
        iterateP = head
        while iterateP:
            myArray.append(iterateP)
            iterateP = iterateP.next
        left, right = 0, len(myArray) - 1
        while right - left > 1:
            myArray[left].next = myArray[right]
            myArray[right].next = myArray[left + 1]
            left += 1
            right -= 1
        myArray[right].next = None

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        method 2
        原地操作，各种简单的链表操作结合
        找中点，短成两半，reverse 后面一半
        重新接起来
        练习一下基础的链表操作
        555555555
        直接写哭了，太多子函数，太多代码了
        """
        if head == None or head.next == None: return
        def breakAndFindMidPoint(head):
            dummy = ListNode(0, head)
            slow, fast = dummy, dummy
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            secondStart = slow.next
            slow.next = None
            return secondStart
        secondStart = breakAndFindMidPoint(head)
        def reverseLinkedList(head):
            if head == None or head.next == None: return head
            newStart = head
            rest = newStart.next
            newStart.next = None
            while rest:
                oldStart = newStart
                newStart = rest
                rest = rest.next
                newStart.next = oldStart
            return newStart
        secondStart = reverseLinkedList(secondStart)
        iterateHead = head
        while secondStart:
            oldIterate = iterateHead
            iterateHead = iterateHead.next
            oldIterate.next = secondStart
            secondStart = secondStart.next
            oldIterate.next.next = iterateHead

## 第二个方法是个很好的锻炼，自己的方法逻辑写的不是特别清晰，参考一下答案的方法
## 把每一个小函数都写清晰

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return
        
        mid = self.middleNode(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = self.reverseList(l2)
        self.mergeList(l1, l2)
    
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
        return prev

    def mergeList(self, l1: ListNode, l2: ListNode):
        while l1 and l2:
            l1_tmp = l1.next
            l2_tmp = l2.next

            l1.next = l2
            l1 = l1_tmp

            l2.next = l1
            l2 = l2_tmp
```

---

## Matrix

### [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)

- [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)
- [Rotate Image](https://leetcode.com/problems/rotate-image/)
- [Word Search](https://leetcode.com/problems/word-search/)

---

## String

### [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

滑动窗口的题目，还需要重点学习

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # method 1
        answer = 0
        for i in range(len(s)):
            mySet = set()
            for j in range(i, len(s)):
                if s[j] not in mySet:
                    mySet.add(s[j])
                    answer = max(answer, len(mySet))
                else:
                    break
        return answer

        # method 2 sliding window set
        answer = 0
        if len(s) == 0: return answer
        mySet = set()
        slow = -1
        for fast in range(len(s)):
            if s[fast] in mySet:
                while True:
                    slow += 1
                    if s[slow] == s[fast]: break
                    else: mySet.remove(s[slow])
            mySet.add(s[fast])
            answer = max(answer, fast - slow)
        return answer

        # method 3 sliding window array (better and faster)
        answer = 0
        if len(s) == 0: return answer
        arr = [False] * 200
        slow = -1
        for fast in range(len(s)):
            if arr[ord(s[fast])]:
                while True:
                    slow += 1
                    if s[slow] == s[fast]: break
                    else: arr[ord(s[slow])] = False
            arr[ord(s[fast])] = True
            answer = max(answer, fast - slow)
        return answer

        # method 4 不用 while 来移动 left 了，直接用记住的 index，跳跃着移动 left
        answer = 0
        arr = [-1] * 200 # 上次出现的位置
        left = -1
        for right in range(len(s)):
            if arr[ord(s[right])] > left:
                left = arr[ord(s[right])]
            arr[ord(s[right])] = right
            answer = max(answer, right - left)
        return answer
```

### [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)

所有子字符串相关的，特别是连续的子字符串，都去想滑动窗口！！！！

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # method 1 
        # brute force n2 方法，把每一个点都看成起点，然后便利以这个点开始的子字符串
        answer = 0
        for i in range(len(s)):
            myMap = [0] * 26
            currMax = 0
            for j in range(i, len(s)):
                myMap[ord(s[j]) - ord('A')] += 1
                currMax = max(currMax, myMap[ord(s[j]) - ord('A')])
                if currMax + k < j - i + 1:
                    break
                else:
                    answer = max(answer, j - i + 1)
        return answer

        # method 2 sliding window n
        answer = 0
        myMap = [0] * 26
        left = -1
        for right in range(len(s)): # 放 right 进去
            myMap[ord(s[right]) - ord('A')] += 1
            while max(myMap) + k < right - left: # 如果不符合要求，缩小 left
                left += 1
                myMap[ord(s[left]) - ord('A')] -= 1
            answer = max(answer, right - left) # 得到符合要求的 substr 更新一下 answer
        return answer
```

- [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)

### [Valid Anagram](https://leetcode.com/problems/valid-anagram/)

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # method 1
        # return sorted(s) == sorted(t) # nlogn
        
        # method 2
        countOfS = [0] * 26
        for char in s:
            countOfS[ord(char) - ord('a')] += 1
        countOfT = [0] * 26
        for char in t:
            countOfT[ord(char) - ord('a')] += 1
        return countOfS == countOfT

        # method 3
        # s = Counter(s)
        # t = Counter(t)
        # return s == t
```

### [Group Anagrams](https://leetcode.com/problems/group-anagrams/)

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = dict()
        for current_str in strs:
            current_key = " ".join(sorted(current_str))
            if current_key not in my_dict:
                my_dict[current_key] = []
            my_dict[current_key].append(current_str)
        return list(my_dict.values())
```

### [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

基本的就是 stack 的做法

如果是要再优化一点运行时间，其实就是判断越多，速度越慢，把判断变少，就可以提高一点速度

判断太多的话，可以适当弄点字典，括号相互对应，也能减少一些判断

```jsx
class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = deque([])
        for c in s:
            if c in "({[":
                my_stack.appendleft(c)
            else:
                if c == ')':
                    if not my_stack or my_stack[0] != '(':
                        return False
                    else:
                        my_stack.popleft()
                if c == ']':
                    if not my_stack or my_stack[0] != '[':
                        return False
                    else:
                        my_stack.popleft()
                if c == '}':
                    if not my_stack or my_stack[0] != '{':
                        return False
                    else:
                        my_stack.popleft()
        return len(my_stack) == 0
```

### [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

```jsx
class Solution:
    def isPalindrome(self, s: str) -> bool:
        my_str = []
        for c in s:
            if '0' <= c <= '9' or 'a' <= c <= 'z':
                my_str.append(c)
            elif 'A' <= c <= 'Z':
                my_str.append(c.lower())
        left, right = 0, len(my_str) - 1
        while left < right:
            if my_str[left] != my_str[right]:
                return False
            left += 1
            right -= 1
        return True
```

- [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
- [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)
- [Encode and Decode Strings (Leetcode Premium)](https://leetcode.com/problems/encode-and-decode-strings/)

---

## Tree

### [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

```jsx
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    直接递归做
    时间和空间复杂度都是 O(N)
    其实这种做法就是 dfs
    也可以用 bfs 做
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

### [Same Tree](https://leetcode.com/problems/same-tree/)

也是 DFS 和 BFS 的做法

DFS 其实就是最简单无脑的递归

```jsx
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        else:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

// 自己写的话，肯定是 DFS 最无脑好写
// 但 BFS 也可以做，可以看看代码

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        queue1 = collections.deque([p])
        queue2 = collections.deque([q])

        while queue1 and queue2:
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            if node1.val != node2.val:
                return False
            left1, right1 = node1.left, node1.right
            left2, right2 = node2.left, node2.right
            if (not left1) ^ (not left2):
                return False
            if (not right1) ^ (not right2):
                return False
            if left1:
                queue1.append(left1)
            if right1:
                queue1.append(right1)
            if left2:
                queue2.append(left2)
            if right2:
                queue2.append(right2)

        return not queue1 and not queue2

// ^ 就是抑或的意思
```

### [Invert/Flip Binary Tree](https://leetcode.com/problems/invert-binary-tree/)

无脑递归

```jsx
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        new_left = self.invertTree(root.right)
        new_right = self.invertTree(root.left)
        root.left, root.right = new_left, new_right
        return root
```

BFS 的话，队列用 list 就行

```python
class Solution(object):
	def invertTree(self, root):
		"""
		:type root: TreeNode
		:rtype: TreeNode
		"""
		if not root:
			return None
		# 将二叉树中的节点逐层放入队列中，再迭代处理队列中的元素
		queue = [root]
		while queue:
			# 每次都从队列中拿一个节点，并交换这个节点的左右子树
			tmp = queue.pop(0)
			tmp.left,tmp.right = tmp.right,tmp.left
			# 如果当前节点的左子树不为空，则放入队列等待后续处理
			if tmp.left:
				queue.append(tmp.left)
			# 如果当前节点的右子树不为空，则放入队列等待后续处理	
			if tmp.right:
				queue.append(tmp.right)
		# 返回处理完的根节点
		return root
```

### [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)

思路就是：

dfs 中算的是，以当前节点为根结点的最大的

返回的是有当前节点的，一边的最大的

```jsx
def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxsum = float('-inf')
        def dfs(node):
            if not node:
                return 0
            leftVal = dfs(node.left)
            rightVal = dfs(node.right)
            self.maxsum = max(self.maxsum, max(0, leftVal) + max(0, rightVal) + node.val)
            return node.val + max(leftVal, rightVal, 0)
        dfs(root)
        return self.maxsum
```

### [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)

层次遍历，就是 BFS，

队列

```jsx
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            currLevel = []
            for _ in range(size):
                currNode = queue.popleft()
                currLevel.append(currNode.val)
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            ans.append(currLevel)
        return ans
```

### [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)

输入是字符串，基本无敌

自己的做法，考虑的比较多，字符串的一些细节都考虑到了，而且 serialize 的时候还考虑了后面全是 null 的情况，其实不考虑也可以，因为测的是你的整个状态，包括，前后的那些细节都无所谓其实，只要保证你这两个函数能够互相转换回去就行

deserialize 能处理那个后面 全是 None 的情况就行

一下是最基础的一版（两个函数都是 BFS，都是队列）：

```jsx
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        ans = []
        queue = deque([root])
        hasTrue = True
        while queue and hasTrue:
            hasTrue = False
            size = len(queue)
            for _ in range(size):
                currNode = queue.popleft()
                if currNode != None:
                    ans.append(str(currNode.val))
                    if currNode.left:
                        queue.append(currNode.left)
                        hasTrue = True
                    else:
                        queue.append(None)
                    if currNode.right:
                        queue.append(currNode.right)
                        hasTrue = True
                    else:
                        queue.append(None)
                else:
                    ans.append("null")
        return '[' + ','.join(ans) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) <= 2:
            return None
        data = data[1:len(data) - 1]
        data = data.split(',')
        root = TreeNode(int(data[0]))
        queue = deque([root])
        index = 1
        while queue:
            currNode = queue.popleft()
            if index < len(data):
                if data[index] != 'null':
                    newLeft = TreeNode(int(data[index]))
                    currNode.left = newLeft
                    queue.append(newLeft)
                index += 1
            if index < len(data):
                if data[index] != 'null':
                    newRight = TreeNode(int(data[index]))
                    currNode.right = newRight
                    queue.append(newRight)
                index += 1

        return root
```

带着最后全是 None 的情况

```jsx
def serialize(self, root):
        if not root:
            return ""
        ans = []
        queue = deque([root])
        while queue:
            currNode = queue.popleft()
            if currNode != None:
                ans.append(str(currNode.val))
                queue.append(currNode.left)
                queue.append(currNode.right)
            else:
                ans.append("null")
        return '[' + ','.join(ans) + ']'
```

力扣网友给的简洁的 BFS 解法

```jsx
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        queue = collections.deque([root])
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append('None')
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []
        dataList = data[1:-1].split(',')
        root = TreeNode(int(dataList[0]))
        queue = collections.deque([root])
        i = 1
        while queue:
            node = queue.popleft()
            if dataList[i] != 'None':
                node.left = TreeNode(int(dataList[i]))
                queue.append(node.left)
            i += 1
            if dataList[i] != 'None':
                node.right = TreeNode(int(dataList[i]))
                queue.append(node.right)
            i += 1
        return root
```

DFS

```jsx
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'None'
        return str(root.val) + ',' + str(self.serialize(root.left)) + ',' + str(self.serialize(root.right))
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs(dataList):
            val = dataList.pop(0)
            if val == 'None':
                return None
            root = TreeNode(int(val))
            root.left = dfs(dataList)
            root.right = dfs(dataList)
            return root

        dataList = data.split(',')
        return dfs(dataList)
```

### [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)

暴力 DFS

```jsx
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        def isSubtreeStartFromRoot(c_root, c_subRoot):
            if not c_root and not c_subRoot:
                return True
            if not c_root or not c_subRoot:
                return False
            return c_root.val == c_subRoot.val and isSubtreeStartFromRoot(c_root.left, c_subRoot.left) and isSubtreeStartFromRoot(c_root.right, c_subRoot.right)
        return isSubtreeStartFromRoot(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
```

- [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

### [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)

暴力 DFS

```python
"""
def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidBST(c_root, lower, upper):
            if not c_root:
                return True
            if c_root.left and c_root.left.val >= c_root.val or c_root.right and c_root.right.val <= c_root.val or c_root.val <= lower or c_root.val >= upper:
                return False
            return isValidBST(c_root.left, lower, c_root.val) and isValidBST(c_root.right, c_root.val, upper)
        return isValidBST(root, float('-inf'), float('inf'))
"""
```

简化一步的写法

```jsx
def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidBST(c_root, lower, upper):
            if not c_root:
                return True
            return lower < c_root.val < upper and isValidBST(c_root.left, lower, c_root.val) and isValidBST(c_root.right, c_root.val, upper)
        return isValidBST(root, float('-inf'), float('inf'))
```

或者 python 可以直接改参数

还有中序和后序的写法，也可以看看

```python
# 中序
class Solution:
    pre = -inf
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if not self.isValidBST(root.left) or root.val <= self.pre:
            return False
        self.pre = root.val
        return self.isValidBST(root.right)

# 后序
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> Tuple:
            if node is None:
                return inf, -inf
            l_min, l_max = dfs(node.left)
            r_min, r_max = dfs(node.right)
            x = node.val
            # 也可以在递归完左子树之后立刻判断，如果不是二叉搜索树，就不用递归右子树了
            if x <= l_max or x >= r_min:
                return -inf, inf
            return min(l_min, x), max(r_max, x)
        return dfs(root)[1] != inf
```

- [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

### [Lowest Common Ancestor of BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

```python
class Solution:
    # time optimal
    # used extra space
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        max_val, min_val = max(p.val, q.val), min(p.val, q.val)
        if min_val <= root.val <= max_val:
            return root
        if root.val < min_val:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > max_val:
            return self.lowestCommonAncestor(root.left, p, q)
    # time optimal
    # space o(1)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = root
        while (ans.val - p.val) * (q.val - ans.val) < 0:
            ans = ans.left if p.val < ans.val and q.val < ans.val else ans.right
        return ans
```

- [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)

- [Add and Search Word](https://leetcode.com/problems/add-and-search-word-data-structure-design/)
- [Word Search II](https://leetcode.com/problems/word-search-ii/)

---

## Heap (and Sort)

- [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

- [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

- [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)

---

## Important Link:

[14 Patterns to Ace Any Coding Interview Question](https://hackernoon.com/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed)

---

两个DFS，搜单词

* [211 Add and Search Word](https://leetcode.com/problems/add-and-search-word-data-structure-design/)
* [212 Word Search II](https://leetcode.com/problems/word-search-ii/)
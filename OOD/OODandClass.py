from typing import List


class TripPlan:
    @classmethod
    def giveMEAPlan(self, bigs, smalls):
        print(bigs, smalls)
    def move(self, num_big, num_small, weight_big, weight_small, big_trunk, small_trunk):
        trips = 0
        while num_big > 0 or num_small > 0:
            current_big_trunk = big_trunk
            current_small_trunk = small_trunk
            trips += 1
            while num_small > 0 and current_big_trunk >= weight_small:
                num_small -= 1
                current_big_trunk -= weight_small
            while num_small > 0 and current_small_trunk >= weight_small:
                num_small -= 1
                current_small_trunk -= weight_small
            while num_big > 0 and current_big_trunk >= weight_big:
                num_big -= 1
                current_big_trunk -= weight_big
            while num_big > 0 and current_small_trunk >= weight_big:
                num_big -= 1
                current_small_trunk -= weight_big
        return trips

    def hop(self, a, f):
        return 0 if a[f] == f else 1 + self.hop(a, a[f])




TripPlan.giveMEAPlan(34, 67)

tp = TripPlan()

print(tp.move(1,2,6,4,10,4))


"""

4 large -> 6
8 small -> 2

Trunk small -> 10
Trunk big -> 15


4 4
6

10
4

"""
class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            LeftSum = 0
            for j in range(0, i):
                LeftSum += nums[j]
            RightSum = 0
            for j in range(i+1, len(nums)):
                RightSum += nums[j]
            answer.append(abs(RightSum - LeftSum))
        return answer
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        mod = 0
        ans = []
        for char in word:
            mod *= 10
            num = int(char)
            mod = (mod + num) % m
            if mod == 0:
                ans.append(1)
            else:
                ans.append(0)
        return ans
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

solu = Solution()
solu.maxNumOfMarkedIndices([42,83,48,10,24,55,9,100,10,17,17,99,51,32,16,98,99,31,28,68,71,14,64,29,15,40])



# class Solution {
#
# 	public int maxNumOfMarkedIndices(int[] nums) {
# 		Arrays.sort(nums);
# 		int count = 0;
# 		for (int i = 0, j = (nums.length + 1) / 2; j < nums.length; j++) {
# 			count += 2 * nums[i] <= nums[j] ? 2 : 0;
# 			i += 2 * nums[i] <= nums[j] ? 1 : 0;
# 		}
# 		return count;
# 	}
# }


# public class Solution {
#     public static void main(String[] args) {
#     }
#
#     int[][] grid;
#
#     public boolean check(int x, int y) {
#         return x >= 0 && y >= 0 && x < grid.length && y < grid[0].length;
#     }
#
#     public int minimumTime(int[][] grid) {
#         this.grid = grid;
#         int[][] dirs = new int[][]{
#                 {-1, 0},
#                 {1, 0},
#                 {0, 1},
#                 {0, -1}
#         };
#         if (grid[0][1] > 1 && grid[1][0] > 1) {
#             return -1;
#         }
#         PriorityQueue<Event> pq = new PriorityQueue<>(Comparator.comparingInt(x -> x.time));
#         pq.add(new Event(0, 0, 0));
#         int[][] time = new int[grid.length][grid[0].length];
#         int inf = (int) 1e9;
#         for (int[] t : time) {
#             Arrays.fill(t, inf);
#         }
#
#         while (!pq.isEmpty()) {
#             var head = pq.remove();
#             if (time[head.x][head.y] <= head.time) {
#                 continue;
#             }
#             time[head.x][head.y] = head.time;
#             for (int[] d : dirs) {
#                 int x = head.x + d[0];
#                 int y = head.y + d[1];
#                 if (!check(x, y)) {
#                     continue;
#                 }
#                 pq.add(new Event(x, y, Math.max(head.time + 1, grid[x][y] + (grid[x][y] % 2 != (x + y) % 2 ? 1 : 0))));
#             }
#         }
#
#         return time[grid.length - 1][grid[0].length - 1];
#     }
# }
#
# class Event {
#     int x;
#     int y;
#     int time;
#
#     public Event(int x, int y, int time) {
#         this.x = x;
#         this.y = y;
#         this.time = time;
#     }
# }

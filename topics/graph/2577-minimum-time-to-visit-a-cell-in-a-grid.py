"""
LeetCode 2577. Minimum Time to Visit a Cell In a Grid

题意：
在一个网格里移动，每个格子只能在某个最早时间之后进入，求到右下角的最短时间。
通常用 Dijkstra / 最短路。

# Java solution:
# public class Solution {
#     int[][] grid;
#
#     public boolean check(int x, int y) {
#         return x >= 0 && y >= 0 && x < grid.length && y < grid[0].length;
#     }
#
#     public int minimumTime(int[][] grid) {
#         this.grid = grid;
#         int[][] dirs = new int[][]{{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
#         if (grid[0][1] > 1 && grid[1][0] > 1) {
#             return -1;
#         }
#         PriorityQueue<Event> pq = new PriorityQueue<>(Comparator.comparingInt(x -> x.time));
#         pq.add(new Event(0, 0, 0));
#         int[][] time = new int[grid.length][grid[0].length];
#         int inf = (int) 1e9;
#         for (int[] t : time) Arrays.fill(t, inf);
#
#         while (!pq.isEmpty()) {
#             var head = pq.remove();
#             if (time[head.x][head.y] <= head.time) continue;
#             time[head.x][head.y] = head.time;
#             for (int[] d : dirs) {
#                 int x = head.x + d[0], y = head.y + d[1];
#                 if (!check(x, y)) continue;
#                 pq.add(new Event(x, y, Math.max(head.time + 1,
#                     grid[x][y] + (grid[x][y] % 2 != (x + y) % 2 ? 1 : 0))));
#             }
#         }
#         return time[grid.length - 1][grid[0].length - 1];
#     }
# }
#
# class Event {
#     int x, y, time;
#     public Event(int x, int y, int time) { this.x = x; this.y = y; this.time = time; }
# }
"""

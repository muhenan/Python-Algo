import collections
from typing import List


class TaskScheduler:
    """
    LeetCode 621: Task Scheduler

    Problem Description:
    给定一个字符数组tasks，表示CPU需要执行的任务。
    每个任务都可以在1个单位时间内完成。
    每个任务执行后需要等待n个单位时间才能执行相同的任务。
    返回完成所有任务所需的最少时间单位。

    Example:
    Input: tasks = ["A","A","A","B","B","B"], n = 2
    Output: 8
    解释: A -> B -> idle -> A -> B -> idle -> A -> B
    """
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        贪心算法
        Time: O(N), N为任务总数
        Space: O(1), 因为最多26个不同的任务
        """
        # 统计每个任务的出现次数
        counts = collections.Counter(tasks)

        # 找出出现次数最多的任务的次数
        maxCount = max(counts.values())

        # 计算有多少个任务出现次数等于maxCount
        numberOfMax = sum(1 for v in counts.values() if v == maxCount)

        # 计算最少需要的时间单位
        # 公式：max((maxCount-1)*(n+1) + numberOfMax, len(tasks))
        # 解释：
        # 1. (maxCount-1)*(n+1)：除最后一组外的必需时间
        # 2. numberOfMax：最后一组的任务数
        # 3. len(tasks)：考虑任务数量足够多的情况
        return max(((maxCount - 1) * (n + 1) + numberOfMax), len(tasks))

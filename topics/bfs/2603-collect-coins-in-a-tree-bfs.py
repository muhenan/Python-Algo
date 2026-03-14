from collections import deque
from typing import List

"""
是一颗合法的树，树是没有环的

首先剪枝，去掉不带金币的叶子节点（因为这些肯定没用），通过拓扑排序一圈一圈删

剪枝了以后，只要搞定叶子（叶子此时肯定是带金币的）就可以了，因为中间的肯定会顺便就收集到

对剪完的树进行标记，叶子是0，即带金币，距离叶子距离为1的是1，再往里是2，我们要便利所有的2

所有都是 2 组成的图，所有边乘2，因为每条边都要走两次，就是答案
"""
class Solution:
    """
    LeetCode 2603: Collect Coins in a Tree
    
    Problem Description:
    给定一棵 n 个节点的树，节点编号从 0 到 n-1，还有一个长度为 n 的数组 coins，
    其中 coins[i] 表示节点 i 是否有金币（1表示有，0表示没有）。
    你可以从任意节点出发，每次可以移动到相邻节点。
    目标是收集所有金币并返回起始位置，求最少需要移动多少步。
    
    解题思路：
    1. 首先通过拓扑排序删除所有不含金币的叶子节点（这些节点没必要访问）
    2. 然后从剩余的带金币的叶子节点开始，计算每个节点到叶子的距离
    3. 最后统计所有距离>=2的节点之间的边的数量，每条边都需要来回走两次
    """
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        # 建图：使用邻接表表示树
        g = [[] for _ in range(n)]
        # 记录每个节点的度数（相连边的数量）
        deg = [0] * n
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)  # 无向图需要双向添加边
            deg[x] += 1
            deg[y] += 1

        # 用拓扑排序「剪枝」：去掉没有金币的子树
        q = deque()
        # 找到所有度为1（叶子）且没有金币的节点
        for i, (d, c) in enumerate(zip(deg, coins)):
            if d == 1 and c == 0:  # 无金币叶子
                q.append(i)
                
        # 删除过程：每次删除一个叶子，更新相邻节点的度数
        while q:
            x = q.popleft()
            for y in g[x]:
                deg[y] -= 1  # 删除一条边，度数减1
                # 如果删除后变成了无金币叶子，继续删除
                if deg[y] == 1 and coins[y] == 0:
                    q.append(y)

        # 第二次拓扑排序：从带金币的叶子开始计算距离
        q.clear()
        for i, (d, c) in enumerate(zip(deg, coins)):
            if d == 1 and c:  # 找到所有带金币的叶子
                q.append(i)
        # 特殊情况：如果带金币的叶子节点不超过1个，不需要移动
        if len(q) <= 1:
            return 0

        # 先都标记成 0，然后计算每个节点到叶子的距离
        time = [0] * n
        while q:
            x = q.popleft()
            for y in g[x]:
                deg[y] -= 1
                if deg[y] == 1: # 只剩一个度的时候才可以入队，然后之后删
                    time[y] = time[x] + 1  # 记录入队时间
                    q.append(y)

        # 统计答案：
        # 1. 对于每条边(x,y)，如果两端点都距离叶子>=2，这条边需要走
        # 2. 每条边都需要来回走两次
        return sum(time[x] >= 2 and time[y] >= 2 for x, y in edges) * 2

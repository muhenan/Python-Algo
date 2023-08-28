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
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        g = [[] for _ in range(n)]
        deg = [0] * n
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)  # 建图
            deg[x] += 1
            deg[y] += 1

        # 用拓扑排序「剪枝」：去掉没有金币的子树
        q = deque()
        for i, (d, c) in enumerate(zip(deg, coins)):
            if d == 1 and c == 0:  # 无金币叶子
                q.append(i) # 找到所有无金币叶子
        while q: # 开始删
            for y in g[q.popleft()]:
                deg[y] -= 1
                if deg[y] == 1 and coins[y] == 0:
                    q.append(y)

        # 再次拓扑排序
        for i, (d, c) in enumerate(zip(deg, coins)):
            if d == 1 and c:  # 有金币叶子
                q.append(i) # 找到所有叶子
        if len(q) <= 1:  # 至多一个有金币的叶子，直接收集
            return 0

        # 先都标记成 0
        time = [0] * n
        while q:
            x = q.popleft()
            for y in g[x]:
                deg[y] -= 1
                if deg[y] == 1: # 只剩一个度的时候才可以入队，然后之后删
                    time[y] = time[x] + 1  # 记录入队时间
                    q.append(y)

        # 统计答案
        return sum(time[x] >= 2 and time[y] >= 2 for x, y in edges) * 2

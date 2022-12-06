import collections
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n)]

        """ build graph """
        for fromNode, toNode, distance in times:
            graph[fromNode - 1].append([toNode - 1, distance])


        k -= 1

        """ dfs """
        vis = set()

        # def dfs(startNode, oldD):
        #     vis.add(startNode)
        #     self.maxD = max(self.maxD, oldD)
        #     for toNode, newD in graph[startNode]:
        #         if toNode not in vis:
        #             dfs(toNode, oldD + newD)

        def dfs(startNode):
            vis.add(startNode)
            for toNode, newD in graph[startNode]:
                if toNode not in vis:
                    dfs(toNode)

        dfs(k)

        if len(vis) < n: return -1

        """ bfs """

        """ Dijkstra """

        """
            这里有问题，这是实现了 BFS，没有实现 Dijkstra，因为没有从最短的边开始走
        """
        #
        # out = set()
        # dijkstraDict = dict()
        # dijkstraDict[k] = 0
        # q = collections.deque([k])
        # while q:
        #     parent = q.popleft()
        #     for child, newD in graph[parent]:
        #         if child not in dijkstraDict:
        #             dijkstraDict[child] = dijkstraDict[parent] + newD
        #         else:
        #             dijkstraDict[child] = min(dijkstraDict[child], dijkstraDict[parent] + newD)
        #         if child not in out:
        #             q.append(child)
        #     out.add(parent)
        #
        # print(dijkstraDict)
        #
        # ans = 0
        # for value in dijkstraDict.values():
        #     ans = max(ans, value)
        #
        #
        # return ans

        """ 最朴素的狄杰斯特拉，临接表实现 """
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """ build graph"""
        g = [[float('inf')] * n for _ in range(n)]  # 默认的距离都是无限远 float('inf')
        for x, y, time in times:
            g[x - 1][y - 1] = time

        """ dist 记录自己离 root 的 min distance"""
        dist = [float('inf')] * n
        dist[k - 1] = 0
        used = [False] * n  # 是否已经用过
        for _ in range(n):  # 每次都用一个 node
            curr = -1
            for nextMin, isused in enumerate(used):  # 找到距离最小的那个
                if not isused:
                    if curr == -1 or dist[nextMin] < dist[curr]:
                        curr = nextMin
            used[curr] = True
            for y, time in enumerate(g[curr]):  # 更新与之相连的点的 min distance
                dist[y] = min(dist[y], dist[curr] + time)

        print(dist)

        ans = max(dist)
        return ans if ans < float('inf') else -1

    """ 用小根堆（优先队列）代替第二个 for 找距离最短的一个 """

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = [[] for _ in range(n)]
        for x, y, time in times:
            g[x - 1].append((y - 1, time))

        dist = [float('inf')] * n
        dist[k - 1] = 0
        q = [(0, k - 1)]

        while q:
            time, x = heapq.heappop(q)
            if dist[x] < time: # 中途多加的，不是最短的，没用的
                continue
            for y, time in g[x]: # 这个循环，或者说这个队列能循环下去的点在于，总能找到更短的距离，如果找不到了就都 pop 然后 continue 了
                d = dist[x] + time
                if d < dist[y]:
                    dist[y] = d
                    heapq.heappush(q, (d, y))

        ans = max(dist)
        return ans if ans < float('inf') else -1
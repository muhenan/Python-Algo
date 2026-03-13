from typing import List

'''
    并查集 Python
    * 路径压缩 find 中实现
    * 权重 weight
'''


class UnionFind:
    def __init__(self):
        self.parent = {}  # 或许用 root 是更好的命名，复议！
        self.weight = {}  # 保存相对同集合内其他节点的权重

    def union(self, x, y, value):
        if x not in self.parent:  # add x
            self.parent[x] = x
            self.weight[x] = 1
        if y not in self.parent:  # add y
            self.parent[y] = y
            self.weight[y] = 1
        parent_x = self.find(x)
        parent_y = self.find(y)
        if parent_x != parent_y:
            self.parent[parent_x] = parent_y
            self.weight[parent_x] = (self.weight[y] * value) / self.weight[x]

    def find(self, x):
        if self.parent[x] != x:
            nearest_parent = self.parent[x]
            self.parent[x] = self.find(self.parent[x])
            self.weight[x] *= self.weight[nearest_parent]
        return self.parent[x]

    def isConnected(self, x, y):
        if x in self.parent and y in self.parent:
            parent_x = self.find(x)
            parent_y = self.find(y)
            if parent_x == parent_y:
                return self.weight[x] / self.weight[y]
        return -1


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        # 1. preprocess
        unionfind = UnionFind()
        for i in range(len(equations)):
            unionfind.union(equations[i][0], equations[i][1], values[i])

        # 2. query
        res = [unionfind.isConnected(q[0], q[1]) for q in queries]

        return res

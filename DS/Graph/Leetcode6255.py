from math import inf
from typing import List


'''

pytho build graph

using dict

key: number
value: list

DFS

'''


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        '''Build Graph'''

        my_graph = {}

        for x, y, road in roads:
            if x not in my_graph: my_graph[x] = []
            if y not in my_graph: my_graph[y] = []
            my_graph[x].append([y, road])
            my_graph[y].append([x, road])


        ''' DFS '''

        self.minRoad = 100000

        checked = [False] * (n + 1)

        def dfs(node):
            if checked[node]: return
            checked[node] = True
            nodes = my_graph[node]

            for anotherNode, road in nodes:
                self.minRoad = min(self.minRoad, road)
                dfs(anotherNode)

        dfs(n)
        return self.minRoad





class TestGlobalVar:
    def f1(self):
        self.val = 5
        def f11():
            self.val += 5
        f11()

Solu = TestGlobalVar()
Solu.f1()
print(Solu.val)


'''

UnionFind

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def merge(self, a, b):
        self.parent[self.find(b)] = self.find(a)

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        union = UnionFind(n+1)
        for x, y, v in roads: union.merge(x, y)
        ans = inf
        for x, y, v in roads:
            if union.find(x) == union.find(1):
                ans = min(ans, v)
        return ans

# Union Find

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        d = list(range(n+1))
        
        def find(a):
            nonlocal d
            if d[a] == a:
                return a
            d[a] = find(d[a])
            return d[a]
            
        
        r = 10000000
        for a,b,c in roads:
            d[find(a)] = find(b)
        
        for a,b,c in roads:
            if find(a) == find(1):
                r = min(r, c)
        return r
'''


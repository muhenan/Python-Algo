from collections import deque
from typing import List

"""
Easy 啦
Topo
先分别找是否有环
没环就分层，然后把矩阵构建出来
"""
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo_layers(num, arr : List[List[int]]): # 直接返回分层，如果有环，就返回空 []
            adjecency = [[] for _ in range(num + 1)]
            indegrees = [0] * (num + 1)
            for start, to in arr:
                if to in adjecency[start]:
                    continue
                adjecency[start].append(to)
                indegrees[to] += 1
            layer = deque([])
            for i in range(1, len(indegrees)):
                if indegrees[i] == 0:
                    layer.append(i)
            layers = []
            visited_count = 0
            while layer:
                count = len(layer)
                visited_count += count
                layers.append(list(layer))
                for _ in range(count):
                    curr = layer.popleft()
                    for i in adjecency[curr]:
                        indegrees[i] -= 1
                        if indegrees[i] == 0:
                            layer.append(i)
            return layers if visited_count == num else []
        rowLayers = topo_layers(k, rowConditions) # 分层其实也不用分，直接把所有都加到一次就行了，一维数组
        colLayers = topo_layers(k, colConditions)
        if len(rowLayers) == 0 or len(colLayers) == 0:
            return []
        ans = [[0] * k for _ in range(k)]
        locations = [[] for _ in range(k + 1)]
        for row in range(len(rowLayers)): # 这里也可以用一个 1 来累加，这样也行，也很简单，就类似数独的排布了
            for element in rowLayers[row]:
                locations[element].append(row)
        curr_col = 0
        for col in range(len(colLayers)):
            for element in colLayers[col]:
                locations[element].append(curr_col)
                curr_col += 1
        for i in range(1, len(locations)):
            ans[locations[i][0]][locations[i][1]] = i
        return ans



solu = Solution()
solu.buildMatrix(8, [[1,2],[7,3],[4,3],[5,8],[7,8],[8,2],[5,8],[3,2],[1,3],[7,6],[4,3],[7,4],[4,8],[7,3],[7,5]], [[5,7],[2,7],[4,3],[6,7],[4,3],[2,3],[6,2]])
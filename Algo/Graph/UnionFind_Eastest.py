class UnionFind_Eastest:
    def __init__(self, k):
        self.count = k
        self.parent = list(range(k))
    def find(self, i):
        curr_root = self.parent[i]
        while curr_root != self.parent[curr_root]:
            curr_root = self.parent[curr_root]
        return curr_root
    # def connect(self, parent_from, child_to):
    #     self.parent[child_to] = self.find(parent_from)

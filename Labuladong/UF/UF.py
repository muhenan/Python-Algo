class WeightedQuickUnionPathCompressionUF:
    def __init__(self, n):
        """
        Initializes an empty union-find data structure with `n` elements `0` through `n-1`.
        Initially, each element is in its own set.

        :param n: the number of elements
        :raises ValueError: if `n < 0`
        """
        self.count = n
        self.parent = list(range(n))
        self.size = [1] * n

    def count(self):
        """
        Returns the number of sets.

        :return: the number of sets (between 1 and n)
        """
        return self.count

    def find(self, p):
        """
        Returns the canonical element of the set containing element `p`.

        :param p: an element
        :return: the canonical element of the set containing `p`
        :raises ValueError: unless `0 <= p < n`
        """
        self._validate(p)
        root = p
        while root != self.parent[root]:
            root = self.parent[root]
        while p != root:
            newp = self.parent[p]
            self.parent[p] = root
            p = newp
        return root

    def connected(self, p, q):
        """
        Returns True if the two elements are in the same set.

        :param p: one element
        :param q: the other element
        :return: True if `p` and `q` are in the same set; False otherwise
        :raises ValueError: unless both `0 <= p < n` and `0 <= q < n`
        """
        return self.find(p) == self.find(q)

    def union(self, p, q):
        """
        Merges the set containing element `p` with the set containing element `q`.

        :param p: one element
        :param q: the other element
        :raises ValueError: unless both `0 <= p < n` and `0 <= q < n`
        """
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return
        if self.size[rootP] < self.size[rootQ]:
            self.parent[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]
        else:
            self.parent[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]
        self.count -= 1

    def _validate(self, p):
        """
        Validates that `p` is a valid index.

        :param p: an index
        :raises ValueError: if `p` is not between 0 and n-1
        """
        n = len(self.parent)
        if p < 0 or p >= n:
            raise ValueError("Index " + str(p) + " is not between 0 and " + str(n - 1))

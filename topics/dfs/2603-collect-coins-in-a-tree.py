from typing import List


class CoinTreePruner:
    """
    LeetCode 2603: Collect Coins in a Tree (Hard)
    
    Given an undirected tree where:
    - nodes[i] may contain a coin (coins[i] = 1) or not (coins[i] = 0)
    - edges represent connections between nodes
    - you must wait 2 moves after collecting a coin before moving again
    
    Return minimum number of edges needed to collect all coins.
    
    Example:
    Input: coins = [1,0,0,0,0,1], edges = [[0,1],[1,2],[2,3],[3,4],[4,5]]
    Output: 2
    
    Tags:
    - Tree
    - Graph
    - Pruning
    - BFS/DFS
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        """
        Solve using tree pruning strategy
        
        Strategy:
        1. Build undirected tree using adjacency sets
        2. Prune useless nodes in three steps:
           - Prune all leaf nodes without coins (and their paths)
           - Prune leaf nodes that are 2 steps away from needed nodes
           - Prune leaf nodes that are 1 step away from needed nodes
        3. Count remaining edges
        """
        n = len(coins)
        # Use sets for O(1) node removal
        tree = [set() for _ in range(n)]
        
        # Build undirected tree
        for a, b in edges:
            tree[a].add(b)
            tree[b].add(a)
        
        # Step 1: Aggressive Pruning - Remove all leaves without coins
        # Also remove entire paths of nodes without coins leading to leaves
        leaves = []
        for i in range(n):
            node = i
            # Keep pruning while we find leaf nodes without coins
            while len(tree[node]) == 1 and coins[node] == 0:
                parent = tree[node].pop()  # Get and remove parent connection
                tree[parent].remove(node)  # Remove child connection
                node = parent  # Move up the tree
            # If we stop at a leaf, record it for next phase
            if len(tree[node]) == 1:
                leaves.append(node)
        
        # Step 2: Distance-2 Pruning
        # Remove leaves that are 2 moves away from necessary nodes
        next_leaves = []
        for leaf in leaves:
            if len(tree[leaf]) == 1:  # Check if still a leaf
                parent = tree[leaf].pop()
                tree[parent].remove(leaf)
                # If parent becomes leaf, it's 1 move away
                if len(tree[parent]) == 1:
                    next_leaves.append(parent)
        
        # Step 3: Distance-1 Pruning
        # Remove leaves that are 1 move away from necessary nodes
        for leaf in next_leaves:
            if len(tree[leaf]) == 1:
                parent = tree[leaf].pop()
                tree[parent].remove(leaf)
        
        # Count remaining edges (each set entry represents one edge)
        return sum(len(connections) for connections in tree)
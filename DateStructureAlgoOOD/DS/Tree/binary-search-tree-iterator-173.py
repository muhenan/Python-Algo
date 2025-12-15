from typing import Optional

from DateStructureAlgoOOD.DS.Tree.TreeNode import TreeNode

"""
LeetCode 173: Binary Search Tree Iterator
Given a binary search tree (BST), implement an iterator to traverse the tree in an in-order manner.
Each call to the next() method should return the next smallest number in the BST.
Time: O(1) for next() and hasNext()
Space: O(h) for the stack, where h is the height of the tree

做简单的做法是先中序遍历，然后存到数组中，然后每次调用 next() 时，返回数组中的下一个元素。
但是这样会占用额外的空间。
时间复杂度是 O(1)，空间复杂度是 O(n)。

优化的的方向是空间复杂度，要优化到 O(h)，而不会占用额外的空间。
"""

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack: list[TreeNode] = []
        if root is None:
            return
        self.push(root)

    def push(self, root: TreeNode):
        """
        Push the leftmost node of the tree into the stack.
        Time: O(h)
        """
        while root is not None:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop()
        self.push(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

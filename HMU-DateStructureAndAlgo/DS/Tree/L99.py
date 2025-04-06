from typing import Optional

from Labuladong.Tree import TreeNode


class Solution:
    """
    搞一个中序遍历，BST，肯定和中序遍历有关
    在一个顺序中，交换两个之后，再从左到右遍历， 1 2 6 4 5 3 7 8
    第一次发现不对时（6，4），肯定是前面的 6 不对
    第二次发现不对时（5，3），肯定是后面的 3 不对
    """

    """
    代码多写几个函数是好习惯，虽然看着多，但可读性高
    """

    def __init__(self):
        self.prev = TreeNode(float("-inf"))
        self.firstOne = None
        self.secondOne = None

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.traverse(root)
        self.firstOne.val, self.secondOne.val = self.secondOne.val, self.firstOne.val

    def traverse(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        self.traverse(root.left)
        if root.val < self.prev.val:
            self.firstOne = self.prev if not self.firstOne else self.firstOne
            self.secondOne = root
        self.prev = root
        self.traverse(root.right)

    def recoverTree_it(self, root: Optional[TreeNode]) -> None:
        stack = []
        result = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr)
            curr = curr.right

        first = None
        second = None

        for i in range(len(result) - 1):
            if result[i].val > result[i + 1].val:
                first = result[i] if not first else first
                second = result[i + 1]

        first.val, second.val = second.val, first.val

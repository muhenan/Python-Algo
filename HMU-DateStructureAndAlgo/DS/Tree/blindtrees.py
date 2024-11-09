# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    直接递归做
    时间和空间复杂度都是 O(N)
    其实这种做法就是 dfs
    也可以用 bfs 做
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    """
    """
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxsum = float('-inf')
        def dfs(node):
            if not node:
                return 0
            leftVal = dfs(node.left)
            rightVal = dfs(node.right)
            self.maxsum = max(self.maxsum, max(0, leftVal) + max(0, rightVal) + node.val)
            return node.val + max(leftVal, rightVal, 0)
        dfs(root)
        return self.maxsum
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue = deque([root])
        while queue:
            size = len(queue)
            currLevel = []
            for _ in range(size):
                currNode = queue.popleft()
                currLevel.append(currNode.val)
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            ans.append(currLevel)
        return ans


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        ans = []
        queue = deque([root])
        hasTrue = True
        while queue and hasTrue:
            hasTrue = False
            size = len(queue)
            for _ in range(size):
                currNode = queue.popleft()
                if currNode != None:
                    ans.append(str(currNode.val))
                    if currNode.left:
                        queue.append(currNode.left)
                        hasTrue = True
                    else:
                        queue.append(None)
                    if currNode.right:
                        queue.append(currNode.right)
                        hasTrue = True
                    else:
                        queue.append(None)
                else:
                    ans.append("null")
        return '[' + ','.join(ans) + ']'


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) <= 2:
            return None
        data = data[1:len(data) - 1]
        data = data.split(',')
        root = TreeNode(int(data[0]))
        queue = deque([root])
        index = 1
        while queue:
            currNode = queue.popleft()
            if index < len(data):
                if data[index] != 'null':
                    newLeft = TreeNode(int(data[index]))
                    currNode.left = newLeft
                    queue.append(newLeft)
                index += 1
            if index < len(data):
                if data[index] != 'null':
                    newRight = TreeNode(int(data[index]))
                    currNode.right = newRight
                    queue.append(newRight)
                index += 1

        return root


solu = Codec()
inputArr = "[1,2,3,null,null,4,5]"
root = solu.deserialize(inputArr)
# print(root.val)
# print(root.left.val)
# print(root.right.val)

data = solu.serialize(root)

print(data)
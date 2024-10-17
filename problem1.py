# Time Complexity = O(n) | Space Complexity = O(n/2) = O(n)

from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        result = []
        if root is None: return result
        queue = deque()
        queue.append(root)

        while len(queue) != 0:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            result.append(node.val)

        return result

# Time Complexity = O(n) | Space Complexity = O(h)
class DFSSolution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        self.result = []
        self.dfsHelper(root, 0)
        return self.result

    def dfsHelper(self, node: TreeNode, level: int):
        # base case
        if node is None: return

        if level == len(self.result):
            self.result.append(0)
        self.result[level] = node.val

        self.dfsHelper(node.left, level+1)
        self.dfsHelper(node.right, level+1)


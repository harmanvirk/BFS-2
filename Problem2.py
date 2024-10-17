# Time Complexity = O(n) | Space Complexity = O(n/2) + O(n/2) = O(n)

from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root is None: return False
        queue = deque()
        queue.append(root)
        #pq = deque()
        #pq.append(root)

        x_found, y_found = False, False
        #x_parent, y_parent = None, None

        while len(queue) != 0:
            for i in range(len(queue)):
                node = queue.popleft()
                #parent = pq.popleft()
                if node.val == x:
                    x_found = True
                    #x_parent = parent
                if node.val == y:
                    y_found = True
                    #y_parent = parent

                if node.left is not None and node.right is not None:
                    if node.left.val == x and node.right.val == y: return False
                    if node.left.val == y and node.right.val == x: return False
                if node.left is not None:
                    queue.append(node.left)
                    #pq.append(node)
                if node.right is not None:
                    queue.append(node.right)
                    #pq.append(node)


            #if x_found and y_found: return x_parent != y_parent
            if x_found and y_found: return True
            if x_found or y_found: return False

        return False

# Time Complexity = O(n) | Space Complexity = O(h)
class DFSSolution:
    def __init__(self):
        self.x_level = -1
        self.y_level = -1
        self.x_parent = None
        self.y_parent = None

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.dfsHelper(root, x, y, 0, None)
        return self.x_level == self.y_level and self.x_parent != self.y_parent

    def dfsHelper(self, node: TreeNode, x: int, y: int, level: int, parent: TreeNode):
        # base case
        if node is None: return
        if node.val == x:
            self.x_level = level
            self.x_parent = parent

        if node.val == y:
            self.y_level = level
            self.y_parent = parent

        self.dfsHelper(node.left, x, y, level + 1, node)
        self.dfsHelper(node.right, x, y, level + 1, node)

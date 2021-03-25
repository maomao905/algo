"""
time and space: O(N)
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        q = deque([(float('-inf'), float('inf'), root)])
        
        while len(q) > 0:
            min, max, node = q.popleft()
            if node is None:
                continue
            if min < node.val < max:
                q.append((min, node.val, node.left))
                q.append((node.val, max, node.right))
            else:
                return False
        
        return True
        

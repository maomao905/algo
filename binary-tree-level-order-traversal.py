# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
BFS
time: O(N)
space: O(N) since O(N/2) at the lowest level
"""
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if root is None:
            return result
        
        current_level = 0
        q = deque([root])
        while len(q) > 0:
            result.append([])
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                result[current_level].append(node.val)
            current_level += 1
        return result
        
        

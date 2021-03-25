from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
time: O(N)
space: worst -> O(N), best -> O(logN)
"""
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # max_depth = 1
        # deque.append([root.left, root.right])
        # 
        # while len(deque) > 0:
        #     node = deque.popleft()
        #     if node is not None:
        
        return self.dfs(root)
    
    def dfs(self, node: TreeNode) -> int:
        if node is None:
            return 0
        return max(self.dfs(node.left), self.dfs(node.right)) + 1
        
                
        

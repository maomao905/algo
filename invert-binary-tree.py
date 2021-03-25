"""
recursively swap left and right subtree
time: O(N)
space: O(N) in worst
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if node is None:
                return
            
            left = dfs(node.left)
            node.left = dfs(node.right)
            node.right = left
            
            return node
        
        return dfs(root)
        
            

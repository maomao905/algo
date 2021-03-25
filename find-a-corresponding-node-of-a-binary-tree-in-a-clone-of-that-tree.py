"""
DFS simultaneously
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(orig, clone):
            if orig is None:
                return
            
            if orig == target:
                return clone
            
            return dfs(orig.left, clone.left) or dfs(orig.right, clone.right)
        
        return dfs(original, cloned)
            

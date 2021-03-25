"""
DFS

time: O(N), space: O(H)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        def dfs(node):
            l, l_level = dfs(node.left) if node.left else (node.val, 0)
            r, r_level = dfs(node.right) if node.right else (node.val, 0)
            
            if l_level >= r_level:
                return l, l_level + 1
            else:
                return r, r_level + 1
        
        return dfs(root)[0]
                

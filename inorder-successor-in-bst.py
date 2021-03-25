# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
in-order
left -> root -> right
"""
from lib.Tree import *

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        def dfs(node, is_successor=False):
            nonlocal ans
            if node is None:
                return is_successor
            
            is_successor = dfs(node.left, is_successor)
            if node == p:
                is_successor = True
            elif is_successor:
                ans = node
                is_successor = False
            
            is_successor = dfs(node.right, is_successor)
            return is_successor
                
        
        ans = None
        dfs(root)
        return ans
        
s = Solution()
print(s.inorderSuccessor(make([2,1,3]), 1))

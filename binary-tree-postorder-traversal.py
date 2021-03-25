"""
post order
left -> right -> root
DFS
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from lib.Tree import *
from typing import List
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(node):
            if node is None:
                return
            
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        
        res = []
        dfs(root)
        return res

s = Solution()
print(s.postorderTraversal(make([1,None,2,3])))
print(s.postorderTraversal(make([])))
print(s.postorderTraversal(make([1])))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
root -> left -> right

time: O(N)
space: O(N)
"""
from typing import List
from lib.Tree import *

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(node):
            if node is None:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        res = []
        dfs(root)
        return res
            
s = Solution()
print(s.preorderTraversal(make([1,None,2,3])))
print(s.preorderTraversal(make([])))
print(s.preorderTraversal(make([1])))
print(s.preorderTraversal(make([1,2])))

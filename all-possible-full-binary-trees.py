# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List
class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        def dfs(remain):
            if remain == 0:
                return []
            
            remain -= 1
            res = []
            if remain >= 2:
                for l, l_remain in dfs(remain):
                    for r, r_remain in dfs(l_remain):
                        node = TreeNode()
                        node.left = l
                        node.right = r
                        res.append((node, r_remain))
            res.append((TreeNode(), remain))
            return res
        
        return [node for node, remain in dfs(N) if remain == 0]

            

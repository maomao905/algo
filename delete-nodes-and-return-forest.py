from typing import List
from lib.Tree import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res = []
        def dfs(node):
            if node is None:
                return
            
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            
            if node.val in delete_nodes:
                for _node in (node.left, node.right):
                    if _node:
                        res.append(_node)
                return
            
            return node
        
        delete_nodes = set(to_delete)
        if root.val not in delete_nodes:
            res.append(root)
        dfs(root)
        return res
            
s = Solution()
print(s.delNodes(make([1,2,3,4,5,6,7]), [3,5]))

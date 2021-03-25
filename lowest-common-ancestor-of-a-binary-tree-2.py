"""
DFS
node returns array which contains matched node value (p o q)
LCA is the first value of array
array size is less than 2, they don't have LCA

time: O(N) space: O(H)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if node is None:
                return None, False
            
            l, l_found = dfs(node.left)
            r, r_found = dfs(node.right)
            
            if l and r:
                return node, True
            
            if node in (p, q):
                if l or r:
                    return node, True
                else:
                    return node, False
            else:
                return l or r, l_found or r_found
        
        LCA, found = dfs(root)
        if found:
            return LCA
        else:
            return None
                
            

"""
consider each node as LCA candidate
DFS to find p and q if left returns root and right returns true or root returns true, then it is LCA
-> if we find q/p, return parent node as LCA, and then parent's parent node as LCA if p's LCA == q's LCA, it is the final LCA
     p
    /  \ 
   q    
     p
    /  \ 
        q    
     
    /  \ 
   p    q    

time: O(N)
space: O(N) in worst
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        found = False
        def dfs(node):
            nonlocal found
            if node is None:
                return None
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if found:
                return left or right
            
            if (node == p or node == q):
                if left or right:
                    found = True
                return node
            
            else:
                if left and right:
                    found = True
                    return node
                else:
                    return left or right
                    
        return dfs(root)

"""
simpler with same approach
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        
        if root in [p, q]:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        else:
            return left or right
        

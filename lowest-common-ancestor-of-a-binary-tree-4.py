# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        def dfs(node):
            if node is None:
                return None, 0
            
            cnt = 0
            l, l_cnt = dfs(node.left)
            r, r_cnt = dfs(node.right)
            cnt += l_cnt + r_cnt
            
            if node in nodes:
                cnt += 1
            
            if cnt == len(nodes):
                return node, 0
            
            return l or r, cnt
                
            
        nodes = set(nodes)
        
        ans, _ = dfs(root)
        return ans

"""
more efficient and simpler solution
"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        def dfs(node):
            if node is None:
                return None
            
            if node in nodes:
                return node
            
            l = dfs(node.left)
            r = dfs(node.right)
            
            if l and r:
                return node
            
            return l or r
                
            
        nodes = set(nodes)
        
        return dfs(root)

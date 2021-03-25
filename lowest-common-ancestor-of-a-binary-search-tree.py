"""
BST
if root is LCA,
    1. left has p/q, right has q/p
    2. root is p/q, right has q/p
    3. root is p/q, left has q/p

left right
1    1     --> LCA
0    1     --> LCA
1    0     --> LCA
2    0     --> not LCA
0    2     --> not LCA

since it's BST, we don't have to traverse up to p/q node, but we know by value
time: O(N) in worst
space: O(N) in worst
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from lib.Tree import *

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        left_count = sum([p.val < root.val, q.val < root.val])
        right_count = sum([p.val > root.val, q.val > root.val])
        if left_count == 1 or right_count == 1:
            return root
        elif left_count > right_count:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)

s = Solution()
print(s.lowestCommonAncestor(make([6,2,8,0,4,7,9,None,None,3,5]), p = TreeNode(2), q = TreeNode(8)).val)
print(s.lowestCommonAncestor(make([6,2,8,0,4,7,9,None,None,3,5]), p = TreeNode(2), q = TreeNode(4)).val)

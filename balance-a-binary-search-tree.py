"""
balanced tree
1. get all elements in sorted order (inorder traversal)
2. create balanced binary search tree from sorted list

O(N)
"""
from lib.Tree import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        
        dfs(root)
        N=len(arr)

        def build(i,j):
            if not(0<=i<=j<N):
                return
            
            if i == j:
                return TreeNode(arr[i])
            
            mid = (i+j)//2
            node = TreeNode(arr[mid])
            node.left = build(i, mid-1)
            node.right = build(mid+1, j)
            return node
        
        return build(0,N-1)

s = Solution()
print(show(s.balanceBST(make([1,None,2,None,3,None,4,None,None]))))
        

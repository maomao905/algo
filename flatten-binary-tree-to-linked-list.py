"""
    1
   / \
  2   5
 / \   \
3   4   6

connect 3 -> 4, 4 -> 5 is the key
preorder traversal

parent node needs to know right-most node from left subtree
connect right-most node to right node

we also need to node.left = None

time: O(N) space: O(H)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from lib.Tree import *

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            if node is None:
                return
            
            right_most_node = node
            
            if node.left:
                right_most_node = dfs(node.left)
            
            right_most_node.right = node.right
            
            if node.right:
                right_most_node = dfs(node.right)
            
            node.right = node.left or node.right
            node.left = None
            return right_most_node
        
        dfs(root)

s = Solution()
root = make([1,2,5,3,4,None,6])
# root = make([1,2,None,3])
s.flatten(root)

while root:
    print(root.val)
    root = root.right

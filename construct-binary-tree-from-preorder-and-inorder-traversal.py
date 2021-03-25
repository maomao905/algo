# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
preorder: parent -> left -> right
rootは確定
[3,9,20,15,7]
    3
   / \
  9  20
    /  \
   15   7

     3
    / \
   9  7
  / \  
 20  15


inorder: left -> parent -> right
あるnodeよりleftにあるかrightにあるか確定できる
配列の順番通りに、left -> rightになっている
rootが3の場合、rootのleft subtreeは[9], right subtreeは[15,20,7]
[9,3,15,20,7]

    3
   / \
  9  20
    /  \
   15   7
    
      20
     /  \
    3    7
   / \
  9  15

再帰的にrootをpreorderから決定して、rootのleft subtree, right subtreeをinorderから決定すれば良い
use hash map to find the root value in inorder in O(1)
time: O(N)
space: O(N)
"""
from typing import List
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def recursive(inorder_start, inorder_end):
            nonlocal pre_idx
            # no candidates in this subtree
            if inorder_start > inorder_end:
                return None
            
            root_val = preorder[pre_idx]
            pre_idx += 1 # move root node next
            
            root = TreeNode(val=root_val)
            root_index = idx_map[root_val]
            root.left = recursive(inorder_start, root_index-1)
            root.right = recursive(root_index+1, inorder_end)
            return root
        
        idx_map = {inorder[i]: i for i in range(len(inorder))}
        pre_idx = 0
        return recursive(0, len(inorder)-1)
        
s = Solution()
root = s.buildTree([3,9,20,15,7], [9,3,15,20,7])

from collections import deque
q = deque([root])

graph = []
while len(q) > 0:
    node = q.popleft()
    v = node.val if node else None
    graph.append(v)
    if node is None:
        continue
    q.append(node.left)
    q.append(node.right)

print(graph)

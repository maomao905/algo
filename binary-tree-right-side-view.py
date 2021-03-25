"""
    1    <--
   / \
  2   5  <--
   \
    3    <--

BFS
at each level, pick the right-most node

time: O(N), space: O(N)
"""

from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from lib.Tree import *
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        q = deque([root])
        
        res = []
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if i == 0:
                    res.append(node.val)
                
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        return res

s = Solution()
print(s.rightSideView(make([1,2,3,None,5,None,4])))

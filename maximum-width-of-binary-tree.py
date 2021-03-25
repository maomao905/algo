"""
BFS
use bit representing each level node index
maximum difference of all level is the answer

O(N) space O(N)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from lib.Tree import *
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        q = deque([(root, 0)])
        ans = 0
        while q:
            l,r = float('inf'),float('-inf')
            for _ in range(len(q)):
                node, x = q.popleft()
                l = min(l,x)
                r = max(r,x)
                if node.left:
                    q.append((node.left, x << 1))
                if node.right:
                    q.append((node.right, (x << 1) + 1))
            
            ans = max(ans, max(r-l+1,0))
        return ans
        
s = Solution()            
print(s.widthOfBinaryTree(make([1,1,1,1,None,None,1,1,None,None,1])))
print(s.widthOfBinaryTree(make([1,3,2,5,3,None,9])))
print(s.widthOfBinaryTree(make([1,3,None,5,3])))
            

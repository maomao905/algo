"""
keep track of number of left path if right path, substract the num
visit leftmost node first because the result format is the array and leftmost nodes are in 0's index
BFS because result should be from top to bottom

time O(N) space O(N)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from lib.Tree import *
from typing import List
from collections import defaultdict, deque
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        res = defaultdict(list)
        
        min_level,max_level = 0, 0
        
        q = deque([(root, 0)])
        while q:
            for _ in range(len(q)):
                node, right_level = q.popleft()
                
                res[right_level].append(node.val)
                min_level = min(min_level, right_level)
                max_level = max(max_level, right_level)
                if node.left:
                    q.append((node.left, right_level-1))
                if node.right:
                    q.append((node.right, right_level+1))
            
        ans = []
        for level in range(min_level, max_level+1):
            ans.append(res[level])
        
        return ans

s = Solution()
print(s.verticalOrder(make([3,9,20,None,None,15,7])))
print(s.verticalOrder(make([3,9,8,4,0,1,7])))
print(s.verticalOrder(make([3,9,8,4,0,1,7,None,None,None,2,5])))
                
                
            

"""
hashmap

sort nodes and sort by x-axis to convert it to list

1. x-axis
- store min x, max axis
- store {x-axis: [nodes]} and at the end make list of length (max - min)

2. overlapping values
- BFS
    - store from smaller y axis order
    - we can get the overlapping values at each iteration (DFS cannot)
    - store result in hashmap {x-axis: [nodes]}
- many values might have same x and y
- keep temp list, if cur x > temp[-1].x, sort the temp values and store in hashmap

O(NlogN)
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
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        res = defaultdict(list) # key is x-axis
        
        q = deque([(0, root.val, root)])
        min_x, max_x = 0, 0
        
        while q:
            y_nodes = sorted(q)
            q.clear()
            for x, _, node in y_nodes:
                min_x = min(min_x, x)
                max_x = max(max_x, x)
                if node.left:
                    q.append((x-1, node.left.val, node.left))
                if node.right:
                    q.append((x+1, node.right.val, node.right))
                res[x].append(node.val)
            
        # print('res:', res)
        ans = [None] * (max_x - min_x + 1)
        for i, x in enumerate(range(min_x, max_x+1)):
            ans[i] = res[x]
        return ans

s = Solution()
print(s.verticalTraversal(make([3,9,20,None,None,15,7])))
print(s.verticalTraversal(make([1,2,3,4,6,5,7])))
print(s.verticalTraversal(make([0,1,2,4,5,9,3,11,None,None,10,15,None,6,18,14,None,None,21,None,None,7,12,None,None,22,None,None,24,13,8,None,17,None,None,None,None,None,None,16,19,None,None,None,None,23,20])))
            
        

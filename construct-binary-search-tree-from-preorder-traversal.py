"""
preorder traversal
find the root node from top of preorder list
"""
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def dfs(i, j):
            if i >= N or i > j:
                return None
            
            node = TreeNode(val=preorder[i])
            if i == j:
                return node
        
            if i+1 < left_bound[i]:
                node.left = dfs(i+1, left_bound[i]-1)
        
            if left_bound[i] <= j:
                node.right = dfs(left_bound[i], j)
        
            return node
        
        N=len(preorder)
        left_bound = [0] * N
        stack = []
        for i in range(N):
            while stack and preorder[stack[-1]] < preorder[i]:
                left_bound[stack.pop()] = i
                
            stack.append(i)
        
        while stack:
            i = stack.pop()
            left_bound[i] = N
        # print(left_bound)
        return dfs(0, N-1)

"""
set lower bound and upper bound and check if preorder[i] is within the range
"""        

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def dfs(l=float('-inf'), r=float('inf')):
            nonlocal i
            if i >= N:
                return
            
            if not(l < preorder[i] < r):
                return
            
            node = TreeNode(val=preorder[i])
            i += 1
            
            node.left = dfs(l, node.val)
            node.right = dfs(node.val, r)
            
            return node
        
        N=len(preorder)
        i = 0
        return dfs()

s = Solution()
# print(s.bstFromPreorder([8,5,1,7,10,12]))
print(s.bstFromPreorder([4,2]))

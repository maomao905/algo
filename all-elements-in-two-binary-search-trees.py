"""
binary search tree
inorder traversal(left -> root -> right)
"""

from typing import List
from lib.Tree import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(node, nums):
            if node is None:
                return []
            
            dfs(node.left, nums)
            nums.append(node.val)
            dfs(node.right, nums)
            return nums
        
        nums1, nums2 = dfs(root1, []), dfs(root2, [])
        
        i = j = 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        
        res.extend(nums1[i:])
        res.extend(nums2[j:])
        return res

s = Solution()
print(s.getAllElements(make([2,1,4]), make([1,0,3])))
print(s.getAllElements(make([0,-10,10]), make([5,1,7,0,2])))
print(s.getAllElements(make([]), make([5,1,7,0,2])))
        

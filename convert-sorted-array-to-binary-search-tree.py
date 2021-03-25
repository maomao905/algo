# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
sorted array = pre-order traversal
1. find the root node
    - find the middle index node
2. build the binary search tree recursively
    - left middle(root) right
    - root.left = (left + middle)//2
time: O(N)
space: O(logN)
"""

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def recursive(left, right):
            if left >= right:
                return None
            root_index = (left+right) // 2
            root = TreeNode(val=nums[root_index])
            root.left = recursive(left, root_index)
            root.right = recursive(root_index+1, right)
            return root
            
        
        return recursive(0, len(nums))

s = Solution()
print(s.sortedArrayToBST([-10,-3,0,5,9]))
        
        

"""
we use monotonically decreasing stack
1. if stack is empty, push the value into stack
2. if the value is smaller than stack[-1], push the value into stack
3. if the value is larger than stack[-1], pop the value until the value is smaller than stack[-1]
    while popping, TreeNode(new_value).left = popped node
to connect current node
stack[-1].right = TreeNode(new_value)

      [3,2,1,6,0,5]
root   
stack 3->2->1
          3<-6
             6->0
              0<-5
             6->5
stack[0] is the root node

time O(N) space O(N)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        stack = []
        for n in nums:
            node = TreeNode(n)
            while stack and stack[-1].val < n:
                node.left = stack.pop()
            
            if stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]
            
            
        
        
        
        
        

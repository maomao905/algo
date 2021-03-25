"""
inorder left -> root -> right
DFS

yield -> how to handle when hasNext is called

binary search tree -> number is sorted

move pointer when next is called

time: O(N)
space: O(N)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from lib.Tree import *

from collections import deque
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.nodes = []
        self.ptr = -1
        stack = deque([root])
        cur = root.left
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            self.nodes.append(cur.val)
            cur = cur.right
        # print(self.nodes)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.ptr += 1
        return self.nodes[self.ptr]
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.ptr + 1 < len(self.nodes)
        


# Your BSTIterator object will be instantiated and called as such:
root = make([7, 3, 15, None, None, 9, 20])
bSTIterator = BSTIterator(root)
print(bSTIterator.next())    # return 3
print(bSTIterator.next())    # return 7
print(bSTIterator.hasNext()) # return True
print(bSTIterator.next())    # return 9
print(bSTIterator.hasNext()) # return True
print(bSTIterator.next())    # return 15
print(bSTIterator.hasNext()) # return True
print(bSTIterator.next())    # return 20
print(bSTIterator.hasNext()) # return False

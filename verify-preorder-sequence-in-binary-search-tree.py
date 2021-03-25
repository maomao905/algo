"""
preorder
root -> left -> right
[5,2,1,3,6]

bst = inorder
left -> root -> right
[1,2,3,5,6]


     5
    / \
   2   6
  / \
 1   3
 
  5
 / \
2   6
preorder     5,2,6
bst(inorder) 2,5,6

use stack to keep left subtree

[5,2,6,1,3] -> false
stack
5
5,2
6 <-- in order to push i, pop nodes less than i (it's kind of reconstructing left subtree)
        we never have the node less than or equal to 5 because we finished traversing left subtree containing less than or equal to 5
1 <-- it's incorrect 1 <= 5

"""


from typing import List

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        min_value = float('-inf')
        for n in preorder:
            if n <= min_value:
                return False
            while stack and stack[-1] < n:
                min_value = max(stack.pop(), min_value)
            
            stack.append(n)
        
        return True

s = Solution()
print(s.verifyPreorder([5,2,6,1,3]))
print(s.verifyPreorder([5,2,1,3,6]))

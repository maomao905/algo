"""
brute-force
visit all leaf nodes (preorder traversal) and check the path is palindrome

O(N^2) visit all nodes O(n) and palindrome check O(n)

how to check palindrome more efficiently?
we need counter because it is not exactly palindrome but only the count is the same as palindrome
if odd num, one odd + all other even
if even num, all even
-> odd num <= 1

we don't have to store all nums but we only need to know the number of odd nums
we use hash map to store odd nums and if it becomes even nums, we delete from hash map

when we go back from leaf node, we have to backtrack the hashmap
if child node value exist in hashmap, we delete
if child node value does not exist, we add

time: O(N), space: O(H)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from lib.Tree import * 
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        odd_nums = set()
        cnt = 0
        
        def keep_odd_num(n):
            if n in odd_nums:
                odd_nums.remove(n)
            else:
                odd_nums.add(n)
        
        def backtrack(n, is_odd):
            if is_odd and n not in odd_nums:
                odd_nums.add(n)
            elif not is_odd and n in odd_nums:
                odd_nums.remove(n)
                
        def dfs(node):
            nonlocal cnt
            keep_odd_num(node.val)
            # print(node.val,odd_nums)
            # leaf node
            if not node.left and not node.right:
                if len(odd_nums) <= 1:
                    
                    cnt += 1
            is_odd = node.val in odd_nums
            if node.left:
                dfs(node.left)
                backtrack(node.val, is_odd)
            if node.right:
                dfs(node.right)
            
            backtrack(node.val, not is_odd)
        
        dfs(root)
        return cnt

"""
save odd occurence with bit vector because 1 <= node.val <= 9
use xor to toggle odd/even occurence
if node.val == 3:
    bit_vector ^= (1 << 3) # 100 3rd digit will be one

if bit_vector has single 1 bit (single odd occurence), it is palindrome,
    -> check if we unset right-most 1 bit vector and become 0
    bit_vector & (bit_vector-1)
time: O(N) space: O(H)
"""            

class Solution:
    def pseudoPalindromicPaths(self, root):
        cnt = 0
        def dfs(node, x):
            nonlocal cnt
            x ^= (1 << node.val)
            # leaf
            if not node.left and not node.right:
                # chekc if single odd occurence
                if x & (x-1) == 0:
                    cnt += 1
                return
            
            if node.left:
                dfs(node.left, x)
            if node.right:
                dfs(node.right, x)
            
        dfs(root, 0)
        return cnt    

s = Solution()
print(s.pseudoPalindromicPaths(make([2,3,1,3,1,None,1])))
print(s.pseudoPalindromicPaths(make([2,1,1,1,3,None,None,None,None,None,1])))
print(s.pseudoPalindromicPaths(make([9])))

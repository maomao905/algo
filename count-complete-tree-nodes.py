"""
traverse all nodes takes O(N)

except for the leaf nodes, we have the following count
1 + 2 + 4 + 8 + 16 + ... + leaf nodes

if we know the height, we know the count of nodes except for the leaf nodes
how do we know the height?
    -> just dfs and only search left nodes, which takes O(logN)
how do we know the number of all nodes?
1 + 2 + 4 + 8 + 16 = 2^5-1 = 2^H -1

how do we know the number of leaf nodes?
    -> binary search
    -> if it's perfect tree, we have M leaf nodes
    -> if we can check M/2 th node actually exists, going right and binary search again
        - what is the range of leaf nodes?
            - 8 ~ 15 = 2^3 ~ 2^4-1 = 2^(H-1) ~ 2^H - 1
    -> it takes O(logN)
how do we check M/2 th leaf node exists?
    -> if we know we shold go left or right from root node, we can reach the M/2 th node

    1
   / \
  2   3
 / \  /
4  5 6

M/2 th node = 5
1 -> 2 -> 5
[1,2,3,4,5,6]
 ^ ^     ^
5 // 2 = 2
2 // 1 = 1

we can use binary representation
bin(5) = '0b101' -> '01' -> left -> right


         1
      /    \
     2       3
    / \     /  \
  4    5   6    7
 /\   / \  /\    / \
8 9 10 11 12 13 14  15
  
bin(11) = '0b1011' -> '011' -> left -> right -> right
overall, O(logN) for binary search and each binary search needs to traverse the mid node, which takes O(logN)
time: (logN)^2
space: O(1)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def get_height(node):
            if node is None:
                return 0
            return get_height(node.left) + 1
        
        def exist(n):
            node = root
            for i in bin(n)[3:]:
                if i == '0':
                    node = node.left
                else:
                    node = node.right
                
            return bool(node)

        if root is None:
            return 0
        
        h = get_height(root)
        l, r = 2**(h-1), 2**h - 1
        
        while l < r:
            mid = l + (r-l)//2 + (r-l)%2
            # check node exists
            if exist(mid):
                l = mid
            else:
                r = mid - 1
        
        return l                
        

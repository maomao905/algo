"""
- in-order traversal (left -> root -> right)
- keep track of the largest leaf value of left and right subtree

O(N^3)
"""
from typing import List
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        def dfs(i,j):
            # leaf node
            if i==j:
                return (0, arr[i]) # (smallest sum, largest leaf value)
            
            if (i,j) not in memo:
                cost = float('inf')
                for k in range(i,j):
                    left_sum, left = dfs(i,k)
                    right_sum, right = dfs(k+1,j)
                    cost = min(cost, left * right + left_sum + right_sum)
                memo[i,j] = (cost, max(arr[i:j+1]))
            return memo[i,j]
        
        memo = {}
        N=len(arr)
        return dfs(0,N-1)[0]

"""
if arr[i] is min
    cost = min(arr[i-1], arr[i+1]) * arr[i]
then pop arr[i]

continue this process until we do not have two leaf nodes

O(N^2)
"""
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        cost = 0
        while len(arr) >= 2:
            i = arr.index(min(arr))
            larger = float('inf')
            if 0<=i-1:
                larger = min(larger, arr[i-1])
            if i+1<len(arr):
                larger = min(larger, arr[i+1])
            cost += larger * arr.pop(i)
        return cost

"""
monotonically decreasing stack
larger1,small,large2 -> choose min(large1, large2)

O(N)
"""
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = []
        cost = 0
        for n in arr:
            while stack and stack[-1] < n:
                cost += stack.pop() * min(stack[-1] if stack else float('inf'), n)
            stack.append(n)
        
        while len(stack) > 1:
            cost += stack.pop() * stack[-1]
        
        return cost


s = Solution()
print(s.mctFromLeafValues([6,2,4]))
print(s.mctFromLeafValues([15,13,5,3,15]))
print(s.mctFromLeafValues([6,9,6,15,15]))
            
            
        

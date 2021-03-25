"""
[1,-2,0,3]
[1,-1,-1,2]
every time, we choose the element or not
[1] max(1) = 1
[1,-1] max(-1,-2) = -1
[1,-1,-1] max(-2,0,-1) = 0
[1,-2,0,3] max(2,)

cumulative sum
every time, check the current cumulative sum - one deleted element value
O(N^2)

-> it failed
"""
# from typing import List
# class Solution:
#     def maximumSum(self, arr: List[int]) -> int:
#         cum_sum = [0] * len(arr)
#         for i in range(len(arr)):
#             if i == 0:
#                 cum_sum[i] = arr[i]
#             else:
#                 cum_sum[i] = cum_sum[i-1] + arr[i]
# 
#         ans = float('-inf')
#         for i in range(len(cum_sum)):
#             ans = max(cum_sum[i], arr[i], ans)
#             for el in arr[:i]:
#                 ans = max(cum_sum[i] - el, ans)
#         return ans

"""
maximum subarray sum -> Kadane's algorithm
max subarray sum from forward and backward
f f f f f f f f D b b b b b b b b
<-- max sum -->   <-- max sum -->  
max subarray sum with one deletion at i is max_sum_forward[i-1] + max_sum_backward[i+1]
time and space: O(N)
"""
from typing import List
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]
        
        N = len(arr)
        
        max_forward = [arr[0]] * N
        for i in range(1, N):
            max_forward[i] = max(max_forward[i-1] + arr[i], arr[i])
        
        max_backward = [arr[-1]] * N
        for i in range(N-2, -1, -1):
            max_backward[i] = max(max_backward[i+1] + arr[i], arr[i])
        
        ans = max(max_forward)
        for i in range(N):
            res = 0
            if i-1 >= 0:
                res += max_forward[i-1]
            if i+1 < N:
                res += max_backward[i+1]
            ans = max(res, ans)
        return ans

"""
DP

case1: one element is deleted
    max_sum_no_deletion[i-1] <-- no deletion until i-1 and current element (i) is deleted
    max_sum_one_deletion[i-1] + arr[i] <-- when one element is deleted before the current element
case2: no element is deleted
    max(max_sum_no_deletion[i-1] + arr[i], arr[i]) <-- Kadane's algorithm

dp[0][delete] = impossible (non-empty is allowed)
dp[0][no_delete] = arr[0]

dp[1][delete] = max(arr[0], arr[1])
dp[1][no_delete] = max(arr[0] + arr[1], arr[1]) = max(dp[0][no_delete] + arr[1], arr[1])
dp[2][delete] = max(dp[1][delete] + arr[2], dp[1][no_delete]) <-- dp[1][no_delete] means current element is deleted
dp[2][no_delete] = max(dp[1][no_delete] + arr[2], arr[2]) <-- Kadane's algorithm

time and space: O(N)
"""

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        N = len(arr)
        if N == 1:
            return arr[0]
        
        dp = [[arr[0]] * 2 for _ in range(N)]
        
        delete = 0
        no_delete = 1
        
        dp[1][delete] = max(arr[0], arr[1])
        dp[1][no_delete] = max(arr[0] + arr[1], arr[1])
        
        for i in range(2, N):
            dp[i][delete] = max(dp[i-1][delete] + arr[i], dp[i-1][no_delete])
            dp[i][no_delete] = max(dp[i-1][no_delete] + arr[i], arr[i])
        
        ans = arr[0]
        for i in range(N):
            ans = max(ans, max(dp[i][delete], dp[i][no_delete]))
        
        return ans

s = Solution()
print(s.maximumSum([1,-2,0,3]))
print(s.maximumSum([1,-2,-2,3]))
print(s.maximumSum([-1,-1,-1,-1]))
print(s.maximumSum([1,-4,-5,-2,5,0,-1,2]))
print(s.maximumSum([8,-1,6,-7,-4,5,-4,7,-6]))

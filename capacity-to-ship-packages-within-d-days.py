"""
brute-force
backtrack
D回選択
time: O(n^D)
space: O(n)
"""
from typing import List
# class Solution:
#     def shipWithinDays(self, weights: List[int], D: int) -> int:
#         result = []
#         def backtrack(comb, d, next_start):
#             # define the goal
#             if d == D-1 and next_start == len(weights):
#                 capacity = max(sum(c) for c in comb)
#                 result.append(capacity)
#                 return
# 
#             # validate the constrants
#             if next_start >= len(weights) or d >= D:
#                 return
# 
#             for _d in range(d, D):
#                 comb[_d].append(weights[next_start])
#                 backtrack(comb, _d, next_start+1)
#                 comb[_d].pop()
# 
#         comb = [[] for _ in range(D)]
#         backtrack(comb, 0, 0)
# 
#         return min(result)
"""
top-down recursive approach
"""
# from copy import deepcopy
# class Solution:
#     def shipWithinDays(self, weights: List[int], D: int) -> int:
#         result = []
#         def recursive(comb, d, next_start):
#             # validate the constrants
#             if next_start >= len(weights) or d >= D:
#                 return
# 
#             comb[d].append(weights[next_start])
# 
#             # define the goal
#             if d == D-1 and next_start == len(weights)-1:
#                 capacity = max(sum(c) for c in comb)
#                 result.append(capacity)
#                 return
# 
#             # include i in d
#             recursive(deepcopy(comb), d, next_start+1)
#             # exclude i from d
#             recursive(deepcopy(comb), d+1, next_start+1)
# 
#         comb = [[] for _ in range(D)]
#         # comb[0].append(weights[0])
#         recursive(comb, 0, 0)
# 
#         return min(result)
"""
binary search
min M: max of weights -> left
max S: sum of weights -> right
time: O(N*log(S-M)) N: size of weights
space: O(1)
"""

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            capacity = left + (right-left)//2
            d = 1
            cur = 0
            # check how many days it takes with the capacity O(N)
            for w in weights:
                cur += w
                if cur > capacity:
                    d += 1
                    cur = w
            # it takes too many days -> too small capacity -> need to increase capacity
            if d > D:
                left = capacity+1
            else:
                right = capacity
        
        return left


s = Solution()
print(s.shipWithinDays( [1,2,3,4,5,6,7,8,9,10], 5))
        
                
        
